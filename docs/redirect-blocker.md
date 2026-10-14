# Result-reader runtime blocker — 2026-10-14

The reader is intentionally guarded after the free api-access request, before the job result endpoint. Do not remove that guard based only on an offline test. The Universal URL field rejects result paths during this limitation. Use the FlashData console for existing stored results; do not resubmit paid work.

## Evidence and implementation

The API contract returns 302 from `GET api.flashdata.dev/v2/jobs/{id}/results`. Make DevTool instead showed 200, JSON content, Cloudflare/R2 headers and the stored artifact's last-modified timestamp. This happened both with the original Base-only flags and after both flags were saved and reread on every communication request. The response-origin guard rejected the unexpected response. No successful storage-header verification was possible, and earlier hop forwarding remains unknown.

The final guard run produced the explicit temporary-unavailability error. DevTool contained only `GET /v2/api-access`, with `x-api-key` masked as `***`; there was no job-results or storage request in that module. Job status, in the separate module, succeeded.

The [request documentation](https://developers.make.com/custom-apps-documentation/component-blocks/api/making-requests) says `followRedirect` controls GET 3xx and `followAllRedirect` controls non-GET 3xx. Both default true and only accept static booleans. Each communication request now explicitly sets both false. The [Base documentation](https://developers.make.com/custom-apps-documentation/app-components/base) does not list those options as inherited; they were removed from Base. [App maintenance](https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app) says private/public app changes take effect immediately. No official cache explanation or alternate redirect mechanism was found.

The intended downstream chain remains in the module for diagnosis: exact trusted HTTPS origin plus slash, then empty request headers and explicit false flags. It is unreachable while the first response validation is false. This is temporary containment, not proof the downstream implementation works.

## Resume criteria

Obtain a verified Make configuration or platform clarification that exposes the original 302 without following it. Test without credentials to external test services. Then validate the trusted origin and prove the storage GET carries no API key, before removing the guard or exercising a download. Any required product API change is outside this channel's deployment authorization.

The separate template publication error (`Template uses app which can't be upgraded to compiled app.`) also remains unresolved. No evidence establishes a one-pending-template quota on Make. Neither issue is assumed to be a cache delay.
