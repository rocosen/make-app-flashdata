# Collect a larger YouTube search result set

Build a broader video research set when the standard 20-result search is too small. Choose a keyword and limit, up to 700, then process the returned video IDs, titles, channel details and thumbnails as separate bundles.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

This uses the separate youtube_search_extended source and price. The result cap is not a promise that 700 matches exist. A large response or slow source can reach Make execution limits; start with a smaller batch.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/youtube_search_extended

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `youtube_search_extended.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. A search emits multiple bundles.

This is prepared template source, not proof of a public Make template or successful platform execution.
