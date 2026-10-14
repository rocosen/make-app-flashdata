# Monitor Google News articles about a topic

Track reporting about a topic such as renewable energy. The news module returns article headlines, links, publication names and date text. Store the article URL as a deduplication key when adding your own table or digest step.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

Date values can be relative, such as 1 day ago. This retrieves search snippets, not full news articles. Date filters and available results depend on Google. Maximum paid pages defaults to 1. Increasing it adds separately charged calls; Limit stops the output once reached.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/google_news

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `google_news.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. A search emits multiple bundles.

This is prepared template source, not proof of a public Make template or successful platform execution.
