# While-You-Sleep Storefront development plugin

This is a skills-based development package, not a verified customer product.
The repository catalog at `.agents/plugins/marketplace.json` points to this
plugin and deliberately sets installation to `NOT_AVAILABLE` while the founder
release hold remains active. A catalog entry does not install a plugin.

Build a marked development ZIP from the package source:

```bash
python plugins/wys-storefront/build_package.py --output /private/build/wys-development.zip
```

The build uses an explicit seven-file allowlist, rejects symlinked sources,
checks onboarding, recomputes source hashes, reads back every archive entry and
refuses to overwrite an existing output. It does not include customer answers,
uploads, private evidence, credentials or arbitrary repository contents. Build
and inspect it as development evidence only; do not send it to customers.

## Remaining installation and execution work

Official packaging guidance supports a repository marketplace for local
authoring/testing and a separate developer upload/review route for public
directory distribution. Workspace publication is limited to that workspace;
it does not distribute the plugin to outside customers. No route is completed
by committing this folder. Host installation and onboarding must be tested in
both fresh and existing conversations using the actual installed copy.

This package has no MCP server, registered server mapping, production
provider/publishing adapter or automatic conversation capture. Private state
must still be saved through a verified durable mechanism. The session CLI and
runtime bridge tests are source/component evidence only. Adding an MCP server
to an already-submitted skills-only plugin is currently unsupported according
to the submission guidance, so resolve the real execution architecture before
submitting a customer draft.

Customer distribution remains held until the actual six buyer paths,
installation, publication, separate scheduled execution, independent review
and explicit founder release clearance have passed. Never change the catalog
policy merely because a development ZIP built successfully.

Verified platform references, 9 October 2026:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
