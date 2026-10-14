# Inspect YouTube video metadata and chapters

Enrich a known video ID without repeating a search. Enter its 11-character ID and select Include chapters or Include formats. One output contains title, description, channel, duration, counts, caption availability and any requested chapters/formats.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

Statistics can be null, and chapters are only returned if available. Formats describe available media; they are not a download delivered to your storage.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_metadata

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_metadata.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. This task returns one result bundle.

This is prepared template source, not proof of a public Make template or successful platform execution.
