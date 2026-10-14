# Platform validation

**Current validation (2026-10-14):** Fourteen of fifteen business sources passed live Make execution; `youtube_download` and customer storage writes were not executed. All six Google modules passed bounded two-page execution after fixing the final no-body validation check. Zero-result search emitted no bundles and made one paid request. Metadata dates, search null dates, separate automatic/manual captions, Management-domain selection, asynchronous metadata submission and the expected 404 path were verified. Job status passed; result retrieval did not.

The authorized limit was 1 FlashData credit and 50 Make credits using existing balances. The complete internal ledger records 39 Make runs, 44 Make credits and 39 paid API requests costing 0.296 FlashData credit, including failed diagnostic runs. No model call or customer media storage write occurred. One asynchronous metadata query created its ordinary FlashData JSON result artifact. All scenarios remain manual/inactive.

Make IML does not support the JavaScript ternary expressions or `startsWith` used in the earlier definitions. These were replaced with documented `if`, `substring` and `length`. Google pagination accepts an absent response body at the platform's termination step. Domain selection no longer embeds the whole ternary text in the URL.

**Result reader blocker:** Even with static `followRedirect: false` and `followAllRedirect: false` saved on every request, the result-link request returned HTTP 200 with R2 response headers in Make DevTool instead of exposing 302. We cannot verify whether the earlier automatic hop forwarded the API key. The reader now deliberately fails after free api-access verification, before requesting the redirect endpoint. A final run and DevTool trace confirmed only that access request. This is a verified guard, not a successful result read. The Universal input rejects results paths. See [redirect blocker](redirect-blocker.md).

Ten offline safety checks pass. They check definitions, explicit per-request flags, bounded billing and the current guard; they do not prove Make honors redirect flags. Public templates and template approval submissions remain 0/15. The app review still has Changes required; Update review was enabled on the final settled page, but no update was submitted with missing successful module evidence.

## Historical execution — 2026-10-10

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
