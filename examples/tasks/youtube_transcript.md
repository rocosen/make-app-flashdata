# Get a YouTube transcript with timestamps

Retrieve existing automatic captions for a known YouTube video in a chosen language. Map fullText into your own document or analysis step, or use segments with start/end seconds to build timestamped references. The template selects automatic captions explicitly.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

The language and automatic caption track must exist. FlashData does not run speech recognition, translate text or fall back to uploader captions. Installing this template does not include a language model.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_transcript

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_transcript.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. This task returns one result bundle.

This is prepared template source, not proof of a public Make template or successful platform execution.
