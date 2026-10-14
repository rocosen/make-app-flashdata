# Deliver YouTube video or audio to your cloud storage

**Current limitation (2026-10-14):** Fourteen data capabilities passed live Make tests. Video download/storage execution remains unverified. Get a job result is temporarily disabled before requesting the signed result link because Make still followed redirects with both documented flags set to false. Keep the job ID and use the FlashData console for stored results; do not resubmit paid work.

Submit a video ID with your own writable storage destination. Choose video/audio format and optional clip times. The prepared workflow submits a job and reads status once, but its result-reader step is currently disabled. Do not run this draft until download/storage validation and result retrieval are complete. The API manifest is documented with file_url, file_size and downloaded_bytes; that output has not been verified through this Make workflow.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

The platform draft uses nonfunctional S3 placeholders; the source blueprint leaves storage empty. Fill your own private storage configuration before running. For an existing job, keep its ID and inspect status/results in the FlashData console; do not resubmit. Downloads are charged by delivered bytes. File privacy and retention follow your storage configuration.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_download

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_download.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Keep scheduling inactive. This draft is not ready for execution while the limitations above remain.
4. For work already submitted, inspect the existing job ID in the FlashData console. The current Make companion reader stops with an explicit limitation error.

This is prepared template source, not proof of a public Make template or successful platform execution.
