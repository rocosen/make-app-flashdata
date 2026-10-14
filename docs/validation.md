# Platform validation

**Current correction (2026-10-14):** The vendor form was submitted on 2026-10-11. Make posted Changes required that day; the previous statement that the form was unsubmitted is historical and superseded. Fifteen business modules, two job readers and a universal module are now saved in the Make editor, with 15 private task-template drafts. Ten offline tests pass; the new definitions have not yet received complete live validation. See [review update](review-update.md).

Recorded 2026-10-10 (Asia/Singapore), Make US2 app 1.0.0. All scenarios are manual and inactive. Private scenario/account identifiers and screenshots are kept in the internal GTM workspace.

| Component | Verified result |
| --- | --- |
| API Key connection | Free `GET /v2/api-access` accepted the test connection |
| Search Web Results | Query `FlashData API`, limit 3, pages 1 and 2 tested separately, autocorrect false; each returned 3 output bundles, 1 Make credit, FlashData usage 0.008 |
| Get Video Metadata | Video `dQw4w9WgXcQ`, chapters true / formats false; 1 bundle with 21 result fields, 1 Make credit, FlashData 0.004 |
| Get Video Transcript | Same video, en / auto false; 1 bundle, 61 segments, fullText length 2089, 1 Make credit, FlashData 0.004 |
| Make an API call | POST /v1/queries/realtime with metadata source and both flags false; statusCode 200, body status done, 1 bundle, 1 Make credit, FlashData 0.004 |
| Search Videos | Query LangGraph / limit 2; 2 bundles with 11 video fields, 1 Make credit, FlashData 0.004 |
| HTTP error | GET /v1/make-validation-not-found returns 404 RuntimeError, one operation and no output bundles; 1 Make credit, no paid query submitted; corrected endpoint/resource error message verified on a second run |

The video/universal scenario completed with 4 Make operations and 0.016 FlashData credits. Exported output JSON was inspected locally: source/status/usage were correct, complete raw response fields were retained, and the transcript's explicit false was preserved. Exported output content is not committed; the public blueprint removes connection IDs and connection restore data.

Seven local safety checks pass. They do not execute Make IML. A live zero-result search and malformed-response simulation have not been verified. The error test proves the HTTP error is represented as RuntimeError with no second operation observed; it does not prove that all platform/network failure recovery can never retry.

## Publication and review

On 2026-10-10, Make confirmed app 1.0.0 as published for invite-link installation, then `pending approval` / `Review process started` after submission of the API documentation and all five module scenario links plus the HTTP error scenario. This confirms the initial review request, not review completion or catalogue listing. Make acknowledged receipt by email and requires a supplementary vendor form before review can proceed; the form was subsequently submitted on 2026-10-11. Make then requested changes; see the current correction above.
