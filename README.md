# FlashData for Make

Native Make integration for 15 Google and YouTube data tasks. Each source has its own module and task blueprint; jobs and universal calls are separate utilities.

The existing app is available through its [invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d). The initial review was requested on 2026-10-10 and the supplementary vendor form was submitted on 2026-10-11. Make posted **Changes required** on 2026-10-11. The requested corrections and 15-capability expansion are saved in the Make editor. Fifteen independent private template drafts exist; public templates remain 0/15. The first template publication attempt failed with “Template uses app which can't be upgraded to compiled app.” App approval and live validation remain outstanding. See the [deployment record](docs/platform-state-2026-10-14.md).

## Task modules

| Module | FlashData source | Inputs, outputs and workflow |
| --- | --- | --- |
| Search web results | `google_search` | [Task guide](examples/tasks/google_search.md) |
| Search news | `google_news` | [Task guide](examples/tasks/google_news.md) |
| Search images | `google_images` | [Task guide](examples/tasks/google_images.md) |
| Search products | `google_shopping` | [Task guide](examples/tasks/google_shopping.md) |
| Search web videos | `google_videos` | [Task guide](examples/tasks/google_videos.md) |
| Search places | `google_places` | [Task guide](examples/tasks/google_places.md) |
| Search videos | `youtube_search` | [Task guide](examples/tasks/youtube_search.md) |
| Search videos (extended) | `youtube_search_extended` | [Task guide](examples/tasks/youtube_search_extended.md) |
| Get video metadata | `youtube_metadata` | [Task guide](examples/tasks/youtube_metadata.md) |
| Get a video transcript | `youtube_transcript` | [Task guide](examples/tasks/youtube_transcript.md) |
| Get video captions | `youtube_captions` | [Task guide](examples/tasks/youtube_captions.md) |
| Get video license metadata | `youtube_trainability` | [Task guide](examples/tasks/youtube_trainability.md) |
| Get a channel | `youtube_channel` | [Task guide](examples/tasks/youtube_channel.md) |
| Search suggestions | `youtube_suggestions` | [Task guide](examples/tasks/youtube_suggestions.md) |
| Download a video | `youtube_download` | [Task guide](examples/tasks/youtube_download.md) |

The app also includes **Get a job status**, **Get a job result**, and **Make an API call**. JSON files map to editor tabs; metadata files are editor form values, not a CLI manifest. Samples are illustrative, not proof of API execution.

## Connect and run

1. Install the app using the invitation above. The public Make catalogue is a separate review milestone.
2. Create a key at [FlashData API keys](https://flashdata.dev/app/api-keys), granting the sources you use. Select your own connection on every module after importing a task blueprint.
3. Set the query, video ID or channel handle. Keep scheduling inactive and inspect inputs before Run once. Download workflows also require your private writable storage configuration.
4. Read the task guide for output fields and limits. Add downstream actions deliberately: search results are separate bundles and can multiply subsequent paid operations.

Templates and the integration are free to install. **FlashData API calls are paid.** [FlashData pricing](https://flashdata.dev/pricing), Make credits, and customer-storage charges are separate. Free connection verification and job reads do not spend FlashData query credits; Make can still charge its own credits.

## Query and download behavior

Google searches use Make pagination and request up to 100 results per page. Limit caps emitted bundles; it defaults to 10 and can be cleared. **Maximum paid pages defaults to 1**, bounds requests when Limit is empty or unmet, and must be raised explicitly for more pages. Each page is a paid request, including a possible empty final page. Make execution limits can stop long searches earlier. Result count is not guaranteed.

YouTube Search supports up to 20 results and Extended Search up to 700, with a separate source and price. Neither invents a pagination token. Transcript defaults to automatic captions; Captions defaults to uploader-provided captions. The requested language/track must exist. No automatic fallback, translation or speech recognition is performed.

Download submits an asynchronous job. Get a job status reads that existing job; Get a job result reads its completed JSON manifest. Files go to customer storage, not a public Make attachment. The template reads status once; if still processing, use the [reader blueprint](examples/read-download-job.blueprint.json) later with the same job ID. Do not repeat the submission to poll. Charges settle by delivered bytes; storage privacy, access and retention remain controlled by the storage owner.

The source named youtube_trainability checks a Creative Commons license label. It does not read YouTube third-party-training settings or grant training rights.

## Safety and migration

Authentication uses a password connection field, free `GET https://api.flashdata.dev/v2/api-access`, and lowercase-header log masking. HTTP redirects are disabled. The result reader checks the signed URL against the trusted HTTPS result origin and removes all inherited headers before fetching stored JSON. Download storage credentials and signed URLs are excluded from HTTP logs; shared templates contain neither credentials nor saved connection IDs.

HTTP errors preserve the status, API message and field detail. `RuntimeError` deliberately avoids automatic rate/connection retry selection for paid POSTs. A 429 can be an uncharged admission rejection; this does not authorize an automatic retry. Platform/network recovery and scenario error handlers remain outside these definitions. Inspect Jobs after an uncertain submission before rerunning it.

Outputs now expose result fields directly: map `title` instead of `result.title`; `raw` and repeated query usage are removed. Google Page is replaced by bounded pagination starting at page 1. Existing manually configured scenarios must review field mappings and pagination settings before rerunning. See [review changes and migration](docs/review-update.md).

## Development and verification

See [deployment](docs/development.md), [historical platform validation](docs/validation.md), and [task templates](examples/README.md). Run `python3 -m unittest discover -s test -v` for offline artifact safety checks. These checks do not execute Make IML or establish that the new modules or public templates are deployed and working.
