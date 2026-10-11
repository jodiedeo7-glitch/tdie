"""OAuth-protected MCP HTTP app; requires verified operator deployment config.

No unauthenticated private-data mode or example production credentials.
This resource server uses an existing configured OAuth issuer; it is not an IdP.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import urlsplit

import anyio
import jwt
from mcp.server.auth.middleware.auth_context import get_access_token
from mcp.server.auth.provider import AccessToken
from mcp.server.auth.settings import AuthSettings
from mcp.server.transport_security import TransportSecuritySettings
from pydantic import AnyHttpUrl
import uvicorn

from session_server import create_server, private_binding


def https_url(value):
    parts = urlsplit(value)
    if (parts.scheme != 'https' or not parts.hostname or parts.username
            or parts.password or parts.fragment):
        raise ValueError('VERIFIED_HTTPS_URL_REQUIRED')
    return value


class JWTVerifier:
    def __init__(self, issuer, resource, jwks_uri, algorithms):
        self.issuer, self.resource = https_url(issuer), https_url(resource)
        https_url(jwks_uri)
        if (not algorithms or not isinstance(algorithms, list)
                or any(a not in ('RS256', 'RS384', 'RS512', 'ES256', 'ES384', 'ES512', 'EdDSA')
                       for a in algorithms)):
            raise ValueError('EXPLICIT_SUPPORTED_SIGNATURE_ALGORITHMS_REQUIRED')
        self.algorithms = algorithms
        self.keys = jwt.PyJWKClient(jwks_uri, timeout=5)

    def checked(self, token):
        try:
            key = self.keys.get_signing_key_from_jwt(token).key
            claims = jwt.decode(token, key, algorithms=self.algorithms,
                issuer=self.issuer, audience=self.resource,
                options={'require': ['exp', 'iat', 'iss', 'aud', 'sub']})
            subject, scope = claims.get('sub'), claims.get('scope')
            client_id = claims.get('azp') or claims.get('client_id')
            if (not isinstance(subject, str) or not subject.strip()
                    or not isinstance(scope, str) or not scope.strip()
                    or not isinstance(client_id, str) or not client_id.strip()):
                return None
            return AccessToken(token=token, client_id=client_id, subject=subject,
                scopes=scope.split(), expires_at=int(claims['exp']), resource=self.resource)
        except (jwt.PyJWTError, ValueError, TypeError, OSError):
            return None

    async def verify_token(self, token):
        return await anyio.to_thread.run_sync(self.checked, token)


def create_app(state_root, verifier, issuer, resource, required_scopes,
               runtime_dir=None, master_path=None):
    https_url(issuer); https_url(resource)
    if (not isinstance(required_scopes, list) or not required_scopes
            or not all(isinstance(s, str) and s.strip() for s in required_scopes)):
        raise ValueError('EXPLICIT_REQUIRED_SCOPES_REQUIRED')
    root, _ = private_binding(Path(state_root) / 'unbound.json', 'unbound')
    root = root.parent

    def authenticated_binding():
        token = get_access_token()
        if (token is None or not token.subject or token.resource != resource
                or token.expires_at is None or token.expires_at <= time.time()
                or not set(required_scopes).issubset(token.scopes)):
            raise ValueError('AUTHENTICATED_CUSTOMER_REQUIRED')
        # Identity derives from validated issuer + subject, NEVER tool arguments.
        identity = hashlib.sha256((issuer + '\0' + token.subject).encode()).hexdigest()
        return root / identity / 'session.json', identity

    auth = AuthSettings(issuer_url=AnyHttpUrl(issuer), resource_server_url=AnyHttpUrl(resource),
                        required_scopes=required_scopes, validate_token_resource=True)
    server = create_server(root / 'unbound.json', 'unbound', runtime_dir, master_path,
        binding_resolver=authenticated_binding,
        server_options={'token_verifier': verifier, 'auth': auth})
    host = urlsplit(resource).hostname
    security = TransportSecuritySettings(enable_dns_rebinding_protection=True,
                                        allowed_hosts=[host, host + ':*'])
    return server.streamable_http_app(stateless_http=True, json_response=True,
        transport_security=security, max_request_body_size=1024 * 1024)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    try:
        config = json.loads(Path(args.config).read_text(encoding='utf-8'))
        verifier = JWTVerifier(config['issuer'], config['resource'], config['jwks_uri'], config['algorithms'])
        app = create_app(config['state_root'], verifier, config['issuer'], config['resource'],
            config['required_scopes'], config.get('runtime'), config.get('authority'))
        port = config['port']
        if type(port) is not int or not 1024 <= port <= 65535:
            raise ValueError('EXPLICIT_VALID_LOCAL_PORT_REQUIRED')
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(2, 'BLOCKED: ' + str(error) + '\n')
    # HTTPS must terminate at a verified trusted deployment proxy. Never expose
    # this development listener on all interfaces or claim it is public TLS.
    uvicorn.run(app, host='127.0.0.1', port=port, log_level='warning', access_log=False)


if __name__ == '__main__':
    main()
