# Review corrections and 15-source expansion

Prepared 2026-10-14. Existing app `flashdata-g6iv9y`, v1.0.0; retain the original review. This file records implementation choices, not successful platform execution.

## Official rules and compatibility

Make [unapproved app maintenance](https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app/private-public-apps) says changes take effect immediately. No module revision isolation was found in the current editor. The three known review scenarios are inactive and their exported example uses constant inputs, not result-field references. Review corrections change output mappings and Google paging behavior; operators of any other invite-installed scenarios must migrate before running.

The previous implementation is retained in Git at the pre-expansion commit. Do not create a duplicate public app or resubmit the vendor form. The real current review is Changes required, not silent waiting. Make's email says the report was AI-generated and may contain mistakes.

## Disposition of the 16 review points

| Point | Source correction / rationale | Remaining platform evidence |
| --- | --- | --- |
| 1 Masking | Lowercase `x-api-key` header and literal `request.headers.x-api-key`; storage masked as a whole | DevTool must show `***` |
| 2 Error detail | HTTP status, body.message/detail, body.field and neutral fallback | Invalid-path / input error execution |
| 3 Pagination | Six Google modules use complete pagination request bodies, response.limit, explicit maximum paid pages (default 1) | Two-page and zero-result execution |
| 4 Limit | Optional uinteger, default 10, non-advanced, final standard field | Editor and run inspection |
| 5 Output | Direct result fields; removed raw/result wrappers and repeated usage | Remap existing consumers; inspect bundles |
| 6 Scenarios | Fifteen standalone task blueprints plus existing-job reader | Paid per-source runs and updated review links |
| 7 429 | RuntimeError retained deliberately: 429 admission rejection can be free, but paid POST retries remain an explicit operator decision | Explain in review reply; no claim all network retries are disabled |
| 8 Caption source | Transcript true; dedicated Captions false; preserve explicit false | Per-track runs |
| 9 Dates | Metadata/search uploadDate parsed as ISO timestamp; source worker emits midnight UTC from YYYYMMDD | Platform date/null validation; channel nested dates remain explicitly labelled ISO text |
| 10 Domains | Universal fixed Data/Management selection plus free job readers | Free Management request and job-reader run |
| 11 Wording | Sentence-case labels and third-person descriptions | Platform metadata readback |
| 12 Universal | Headers KV, any Body, harmless /v2/api-access help; block Host/auth headers | Header and body editor validation |
| 13 Groups | Google search, YouTube, Jobs; Universal stays Other | Platform group assignment |
| 14 Action | Data getters Read, asynchronous download Create | Platform form assignment |
| 15 Connection metadata | Remove constant FlashData API label | Connection readback |
| 16 Samples | All modules have illustrative samples | Platform samples save/readback |

## Download trust boundary

Submission is a single `POST data.flashdata.dev/v1/queries`. Both readers use `GET api.flashdata.dev/v2/jobs/{id}` endpoints. The result reader first obtains `result_origin` from api-access, verifies an HTTPS origin and exact origin-plus-slash prefix on the returned 302 Location, then fetches with `headers: {{emptycollection}}` to override all Base headers. Neither authenticated nor storage requests follow redirects. API keys never go to object storage.

Job status uses `completed`; the stored result envelope can use `done`. They are different fields, so the blueprint completion filter tests the job status only. Processing leaves the existing job ID available for the companion reader. A result URL is not the customer's media download URL: the JSON manifest describes files already delivered to customer storage.

## Source review and validation boundaries

Ten offline safety tests check bounded paid requests, exact capability/template coverage, credential destinations and template isolation. Native JSON IML expressions preserve their typed values (for example `{{parameters.auto}}`); their JSON string syntax is not evidence that Make sends a string boolean. Prior live tests already established explicit false handling. Make's response.limit automatically terminates pagination at the requested output count; the additional maxPages condition caps paid requests.

The new 11 source calls, automatic paging, revised output mappings, result reader and storage write still require live Make validation. No paid query, model call or storage write was run to prepare this source change. Do not describe these as passed.

Official references: [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination), [multiple requests](https://developers.make.com/custom-apps-documentation/component-blocks/api/multiple-requests), [sanitization](https://developers.make.com/custom-apps-documentation/app-components/base/sanitization), [error types](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/error), [REST universal](https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module/rest), [inheritance](https://developers.make.com/custom-apps-documentation/app-components/base/advanced-inheritance).
