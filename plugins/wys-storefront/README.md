# While-You-Sleep Storefront development plugin

This is a development package with a private session MCP server, not a verified customer product.
The repository catalog at `.agents/plugins/marketplace.json` points to this
plugin and deliberately sets installation to `NOT_AVAILABLE` while the founder
release hold remains active. A catalog entry does not install a plugin.

Build a marked development ZIP from the package source:

```bash
python plugins/wys-storefront/build_package.py --output /private/build/wys-development.zip
```

The build uses an explicit fourteen-file allowlist, rejects symlinked sources,
checks onboarding, recomputes source hashes, reads back every archive entry and
refuses to overwrite an existing output. It does not include customer answers,
uploads, private evidence, credentials or arbitrary repository contents. The four
runtime guard files come from this same repository checkout and are bundled in
`server/runtime/`; a mismatched questionnaire bank blocks the build. Build
and inspect it as development evidence only; do not send it to customers.

## Remaining installation and execution work

Official packaging guidance supports a repository marketplace for local
authoring/testing and a separate developer upload/review route for public
directory distribution. Workspace publication is limited to that workspace;
it does not distribute the plugin to outside customers. No route is completed
by committing this folder. Host installation and onboarding must be tested in
both fresh and existing conversations using the actual installed copy.

The package includes `server/session_server.py` using the official Python
MCP SDK pinned in `server/requirements.txt`. Its eight tools create/resume
the configured private session, read exact state/next topic, save answers,
record events and record separate operator evidence. With the actual runtime
from PR31 configured, they also prepare all nine operation inputs and verify
per-answer application through that runtime against the same session file.
The runtime and authority paths come from trusted operator launch configuration;
they cannot be replaced through tool arguments. Each stdio server is bound to
one launch-configured customer and absolute state path; tool arguments cannot
choose a different customer or file. Writes check identity under the session's
OS lease and read back the resulting state. Repository storage, symlinked
state and relative state paths are rejected.

There is no deployed remote endpoint, registered server mapping, production
provider/publishing adapter or automatic whole-conversation capture. State is
a local file; remote durability is not established by this server. Exact tool
inputs retained in session history are not an archive of messages the server
never received. The actual SDK/client subprocess tests verify local tool calls
and restart/resume, not ChatGPT installation or external workflow execution.
Adding an MCP server
to an already-submitted skills-only plugin is currently unsupported according
to the submission guidance, so resolve the real execution architecture before
submitting a customer draft.

For operator development, install `server/requirements.txt` into an isolated
Python environment, then launch the stdio server with that environment's Python:

```bash
python /absolute/plugin/path/server/session_server.py --state /private/state/session.json --customer ACTUAL_CUSTOMER_ID
python -m unittest discover -s plugins/wys-storefront/tests -p 'test_mcp_session.py' -v
```

The customer ID and private file path come from actual authorized configuration.
They are not credentials or a remote authentication system. Production remote
MCP requires verified HTTPS hosting, per-customer authentication/authorization
and durable storage. Hosting and actual customer identity-provider configuration
remain unfinished.

## Protected HTTP development implementation

`server/remote_server.py` builds an SDK Streamable HTTP app. It accepts only
authenticated, unexpired, correctly scoped tokens bound to the configured MCP
resource. Its JWT verifier checks an explicitly configured signature algorithm,
issuer, audience, expiration, issued time, subject and client identity against
the configured JWKS endpoint. Customer state identity derives from the verified
issuer and subject, never from model-supplied paths or customer IDs. Anonymous,
expired, wrong-resource and insufficient-scope calls cannot create private state.

The synthetic HTTP tests exercised two distinct authenticated customers, separate
saved answers, cross-customer payload rejection, invalid Host rejection and real
RSA-signed token acceptance/rejection. This does not verify a live OAuth issuer,
network JWKS lookup, production TLS, durable host volume or ChatGPT installation.

The remote launcher requires a private operator JSON configuration containing
`issuer`, `resource`, `jwks_uri`, `algorithms`, `required_scopes`, `state_root` and
`port`. Optional paired `runtime` and `authority` paths enable input preparation.
No production endpoint, credentials or example customer answers are supplied.
It listens on 127.0.0.1 behind a verified HTTPS proxy; it is not a deployed public
service. Do not add a fictitious endpoint to mcp.json or distribute it as connected.
Provider/publisher/scheduler execution remains unfinished.

Customer distribution remains held until the actual six buyer paths,
installation, publication, separate scheduled execution, independent review
and explicit founder release clearance have passed. Never change the catalog
policy merely because a development ZIP built successfully.

Verified platform references, 9 October 2026:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/mcp-server
