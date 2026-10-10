# FlashData for Make

Native Make custom app source for the [FlashData API](https://flashdata.dev/docs/api-reference).

This app is published for installation through an [invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). Technical review was requested on 2026-10-10; Make shows `pending approval`. It is not yet approved or listed in Make's public catalogue.

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
| Search Videos | `youtube_search` | One bundle per video |
| Get Video Metadata | `youtube_metadata` | One bundle with video details |
| Get Video Transcript | `youtube_transcript` | One bundle with segments and full text |
| Make an API call | Relative paths on `data.flashdata.dev` | Response body, headers and status code |

See [validation results](docs/validation.md) for which modules have been tested on Make. Source implementation and platform verification are separate milestones.

## Credentials and query costs

Create an API key in the FlashData console and grant it the sources you intend to use. The connection verifies the key with `GET https://api.flashdata.dev/v2/api-access`, which does not consume query credits. Queries use `POST https://data.flashdata.dev/v1/queries/realtime` and consume FlashData credits. Make credits are separate.

One search execution requests one page. `Limit` maps to FlashData `params.num`; `Page` maps to `params.page`. Pagination is explicit: changing the page triggers another paid query. There is no request repeat/pagination loop. Video search uses `Limit` as `max_results` and has no page control. A search with no matches is intended to produce zero bundles; a live zero-result case is still pending verification.

Every output bundle repeats the **same query's** usage and raw response. Do not sum the usage across those bundles. Downstream modules execute once per bundle, so keep paid downstream calls outside an unintended fan-out.

HTTP error responses use `RuntimeError`, including 429 and 5xx, to avoid Make's default rate/connection retry behavior. Redirects are disabled and API keys are sanitized in request logs. The module does not add a repeat loop. Make's network failure and scenario-level recovery behavior is controlled by the platform: before rerunning an uncertain paid query, inspect FlashData Jobs. Do not enable automatic error-handler retries for paid queries without accepting possible duplicate charges.

## Development

Use the official [Make Custom Apps editor](https://developers.make.com/custom-apps-documentation/create-your-first-app/create-your-app) or the official Make Apps Editor extension. Follow [the deployment guide](docs/development.md); do not paste credentials into Base, Common data, module code or this repository.

Run local safety checks with `python3 -m unittest discover -s test -v`. These checks do not substitute for real Make scenario execution.

## Video inputs and universal calls

Video actions take an 11-character video ID. Metadata preserves the Include Chapters and Include Formats choices. Transcript requires an explicit language and automatic/manual subtitle choice; unavailable subtitles do not trigger a fallback or a second query.

The universal module accepts a relative path such as `/v1/queries/realtime`, a method, query-string items and a JSON text body. It always uses `https://data.flashdata.dev`; authentication and content-type headers are provided by the app. It does not accept arbitrary origins or user-supplied authentication headers. Inspect the returned body for application-level status, as the universal module cannot interpret every endpoint's response contract.
