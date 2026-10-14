# Research Google Places and local business listings

Build a local-business research list from a phrase such as coffee in san francisco. Each bundle can include name, address, coordinates, ratings, category, website and phone number. Map only fields needed by your business workflow.

Setup: install the FlashData app, select your own connection and configure the inputs. Create an API key at https://flashdata.dev/app/api-keys with this source enabled.

Contact fields are optional, and a listing is not a verified lead or permission to contact it. Use query and location consistently when comparing snapshots. Maximum paid pages defaults to 1. Increasing it adds separately charged calls; Limit stops the output once reached.

Templates and the integration are free to install. FlashData API requests are paid; Make charges separately. Pricing: https://flashdata.dev/pricing
API and fields: https://flashdata.dev/docs/sources/google_places

## Run this workflow

1. Install the app through the [current invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Approval and public-template listing are separate.
2. Import `google_places.blueprint.json` and select your own FlashData connection on every module. No connection ID or API key is included.
3. Review the inputs, keep scheduling inactive and use Run once only when ready to pay for the query.
4. Inspect the output before adding downstream actions. A search emits multiple bundles.

This is prepared template source, not proof of a public Make template or successful platform execution.
