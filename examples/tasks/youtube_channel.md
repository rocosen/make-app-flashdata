# Snapshot a YouTube channel and recent videos

Retrieve a channel profile by handle, such as @jawed. Choose up to 100 recent videos. One result contains channel identity, description, available subscriber/video counts, avatar/banner links and the recent videos array.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

videoCount describes the channel; videos contains only the requested recent items. Counts and images can be unavailable. Nested uploadDate values remain ISO text; parse them in Make when doing date arithmetic.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_channel

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_channel.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. This task returns one result bundle.

This is prepared template source, not proof of a public Make template or successful platform execution.
