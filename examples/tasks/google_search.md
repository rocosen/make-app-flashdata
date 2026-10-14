# Find Google Search results for a research question

Build a reference list before writing a technical brief. Enter a query such as site:docs.python.org asyncio. Each bundle contains a title, URL, snippet and position; map link and title into your destination after this search.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

Country, interface language and location change the requested search context. Optional fields can be absent. This searches results; it does not fetch full article text. Maximum paid pages defaults to 1. Increasing it adds separately charged calls; Limit stops the output once reached.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/google_search

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `google_search.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. A search emits multiple bundles.

This is prepared template source, not proof of a public Make template or successful platform execution.
