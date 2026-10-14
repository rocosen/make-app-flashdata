# Deliver YouTube video or audio to your cloud storage

Submit a video ID with your own writable storage destination. Choose video/audio format and optional clip times. The workflow returns a job ID and reads status once. If completed, it reads the JSON manifest containing file_url, file_size and downloaded_bytes.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

The platform draft uses nonfunctional S3 placeholders; the source blueprint leaves storage empty. Fill your own private storage configuration before running. If processing, keep the job ID and use the companion reader later; do not resubmit. Downloads are charged by delivered bytes. File privacy and retention follow your storage configuration.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_download

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_download.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the job ID and status. The manifest is emitted only when the job is completed; otherwise read that same job later with the companion reader.

This is prepared template source, not proof of a public Make template or successful platform execution.
