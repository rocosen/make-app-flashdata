# FlashData for Make

Native Make custom app source for the [FlashData API](https://flashdata.dev/docs/api-reference).

This integration is under development as a private Make app. It has not been published by invite link, submitted for app review, or listed in Make's public catalogue.

## Development layout

- `app/base.json`: shared API origin, authentication, redirection policy and HTTP error handling.
- `app/connections/api-key/`: free connection verification and a password-type API key field.
- `app/modules/`: module metadata, communication, input parameters, output interfaces and illustrative samples.
- `docs/`: deployment and verified scenario results.

The JSON files map to Make's web app editor tabs. `metadata.json` records values entered in the creation forms; it is not a Make CLI deployment manifest. This repository contains no API keys or platform tokens.

## Modules

| Module | Source | Output |
| --- | --- | --- |
| Search Web Results | `google_search` | One bundle per organic result, including the raw query response and usage |

Further video modules and the universal API module will be added before app review. No review readiness is claimed by this initial source release.

## Credentials and query costs

Create an API key in the FlashData console and grant it the sources you intend to use. The connection verifies the key with `GET https://api.flashdata.dev/v2/api-access`, which does not consume query credits. Queries use `POST https://data.flashdata.dev/v1/queries/realtime` and consume FlashData credits. Make credits are separate.

One search execution requests one page. `Limit` maps to FlashData `params.num`; `Page` maps to `params.page`. Pagination is explicit: changing the page triggers another paid query. There is no request repeat/pagination loop in this initial module.

Every output bundle repeats the **same query's** usage and raw response. Do not sum the usage across those bundles. Downstream modules execute once per bundle, so keep paid downstream calls outside an unintended fan-out.

HTTP error responses use `RuntimeError`, including 429 and 5xx, to avoid Make's default rate/connection retry behavior. Redirects are disabled and API keys are sanitized in request logs. The module does not add a repeat loop. Make's network failure and scenario-level recovery behavior is controlled by the platform: before rerunning an uncertain paid query, inspect FlashData Jobs. Do not enable automatic error-handler retries for paid queries without accepting possible duplicate charges.

## Development

Use the official [Make Custom Apps editor](https://developers.make.com/custom-apps-documentation/create-your-first-app/create-your-app) or the official Make Apps Editor extension. Follow [the deployment guide](docs/development.md); do not paste credentials into Base, Common data, module code or this repository.

Run local safety checks with `python3 -m unittest discover -s test -v`. These checks do not substitute for real Make scenario execution.
