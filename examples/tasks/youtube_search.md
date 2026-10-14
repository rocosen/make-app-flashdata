# Find YouTube videos by keyword

Discover candidate videos for a topic such as python tutorial. Enter a query and a result limit up to 20. Each bundle includes a videoId, title, channel, duration, view count and available thumbnails. Add any paid enrichment step deliberately: it runs for every bundle.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

Search filters can select upload date, duration, type, sort order or features. Missing dates and counts stay unavailable. One run makes one paid request; there is no page token.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_search

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_search.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. A search emits multiple bundles.

This is prepared template source, not proof of a public Make template or successful platform execution.
