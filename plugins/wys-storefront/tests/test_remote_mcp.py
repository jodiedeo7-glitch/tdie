"""Protected HTTP transport and signed-token tests; synthetic tenants only."""
import json
from pathlib import Path
import sys
import tempfile
import time
import unittest
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'server'))
from remote_server import JWTVerifier, create_app
from mcp.server.auth.provider import AccessToken
from starlette.testclient import TestClient
import jwt
from cryptography.hazmat.primitives.asymmetric import rsa

RESOURCE = 'https://mcp.test/mcp'
ISSUER = 'https://issuer.test'


class FixtureVerifier:
    async def verify_token(self, token):
        if token == 'invalid': return None
        return AccessToken(token=token, client_id='synthetic-client',
            subject='customer-b' if token == 'b' else 'customer-a',
            scopes=[] if token == 'no-scope' else ['wys:state'],
            expires_at=int(time.time()) + (-100 if token == 'expired' else 300),
            resource='https://wrong.test/mcp' if token == 'wrong-resource' else RESOURCE)


class ProtectedHTTPTests(unittest.TestCase):
    def test_http_authorization_and_two_customer_isolation(self):
        with tempfile.TemporaryDirectory() as directory:
            app = create_app(directory, FixtureVerifier(), ISSUER, RESOURCE, ['wys:state'])
            with TestClient(app, base_url='https://mcp.test') as client:
                def call(name, arguments=None, token=None):
                    headers = {'Accept': 'application/json, text/event-stream'}
                    if token: headers['Authorization'] = 'Bearer ' + token
                    return client.post('/mcp', headers=headers, json={
                        'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
                        'params': {'name': name, 'arguments': arguments or {}}})
                for token in (None, 'invalid', 'expired', 'wrong-resource', 'no-scope'):
                    with self.subTest(token=token):
                        response = call('wys_start_session', token=token)
                        self.assertIn(response.status_code, (401,403))
                self.assertEqual(list(Path(directory).rglob('session.json')), [])
                def data(response):
                    self.assertEqual(response.status_code, 200, response.text)
                    body = response.json()['result']
                    self.assertFalse(body.get('isError', False), body)
                    return body['structuredContent']
                a = data(call('wys_start_session', token='a'))
                b = data(call('wys_start_session', token='b'))
                self.assertNotEqual(a['customer_id'], b['customer_id'])
                q = a['next']
                answer = {'value': {'selected': q['options'][:1], 'detail': 'Exact customer A text'},
                    'evidence': 'synthetic A source', 'answered_at': '2026-10-09T20:00:00+00:00'}
                data(call('wys_save_answer', {'question_id': q['id'], 'answer': answer,
                                             'expected_revision': 0}, token='a'))
                self.assertEqual(data(call('wys_get_session', token='a'))['answers'][q['id']], answer)
                self.assertEqual(data(call('wys_get_session', token='b'))['answers'], {})
                response = call('wys_verify_input_application',
                    {'payload': {'customer_id': a['customer_id'], 'scope': 'production'}, 'coverage': {}}, token='b')
                self.assertTrue(response.json()['result']['isError'])
                self.assertEqual(len(list(Path(directory).rglob('session.json'))), 2)
                wrong_host = client.post('/mcp', headers={'Host':'attacker.test',
                    'Authorization':'Bearer a','Accept':'application/json, text/event-stream'},
                    json={'jsonrpc':'2.0','id':1,'method':'tools/list'})
                self.assertNotEqual(wrong_host.status_code,200)

    def test_real_signed_jwt_rejects_bad_signature_issuer_audience_expiry_and_missing_subject(self):
        key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
        other = rsa.generate_private_key(public_exponent=65537,key_size=2048)
        verifier = JWTVerifier(ISSUER,RESOURCE,'https://issuer.test/jwks',['RS256'])
        class Keys:
            def get_signing_key_from_jwt(self,token): return SimpleNamespace(key=key.public_key())
        verifier.keys=Keys()
        claims={'iss':ISSUER,'aud':RESOURCE,'sub':'synthetic-a','iat':int(time.time()),
                'exp':int(time.time())+300,'azp':'synthetic-client','scope':'wys:state'}
        valid=verifier.checked(jwt.encode(claims,key,algorithm='RS256'))
        self.assertEqual(valid.subject,'synthetic-a');self.assertEqual(valid.resource,RESOURCE)
        for changed in ({'iss':'https://wrong.test'},{'aud':'https://wrong.test'},
                        {'exp':int(time.time())-10},{'sub':''},{'scope':''}):
            with self.subTest(changed=changed):
                self.assertIsNone(verifier.checked(jwt.encode(dict(claims,**changed),key,algorithm='RS256')))
        missing=dict(claims);missing.pop('sub')
        self.assertIsNone(verifier.checked(jwt.encode(missing,key,algorithm='RS256')))
        self.assertIsNone(verifier.checked(jwt.encode(claims,other,algorithm='RS256')))


if __name__=='__main__': unittest.main()
