# Check YouTube Creative Commons license metadata

Inspect the license label for a known video before your own rights review. Enter the video ID; the response includes videoId, kind, etag and permitted. A detected Creative Commons label yields ["all"]; other or missing metadata yields ["none"].

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

The API source is called youtube_trainability, but this checks license metadata only. It does not report creator third-party-training settings or grant permission to train, download or reuse a video.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_trainability

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_trainability.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. This task returns one result bundle.

This is prepared template source, not proof of a public Make template or successful platform execution.
