# FlashData

Use Google Search, News, Images, Shopping, Videos and Places, or YouTube Search, Extended Search, Metadata, Transcript, Captions, License Metadata, Channel, Suggestions and Download in Make.

**Current limitation (2026-10-14):** Fourteen data capabilities passed live Make tests. Video download/storage execution remains unverified. Get a job result is temporarily disabled before requesting the signed result link because Make still followed redirects with both documented flags set to false. Keep the job ID and use the FlashData console for stored results; do not resubmit paid work.

## Setup and cost

Create an API key at https://flashdata.dev/app/api-keys, grant the required source and select a FlashData connection. Verification is free of FlashData query charges. The integration and templates are free to install; FlashData API calls are paid. Make and storage-provider charges are separate. Prices: https://flashdata.dev/pricing

## Choose a task

- **Search web results**: https://flashdata.dev/docs/sources/google_search
- **Search news**: https://flashdata.dev/docs/sources/google_news
- **Search images**: https://flashdata.dev/docs/sources/google_images
- **Search products**: https://flashdata.dev/docs/sources/google_shopping
- **Search web videos**: https://flashdata.dev/docs/sources/google_videos
- **Search places**: https://flashdata.dev/docs/sources/google_places
- **Search videos**: https://flashdata.dev/docs/sources/youtube_search
- **Search videos (extended)**: https://flashdata.dev/docs/sources/youtube_search_extended
- **Get video metadata**: https://flashdata.dev/docs/sources/youtube_metadata
- **Get a video transcript**: https://flashdata.dev/docs/sources/youtube_transcript
- **Get video captions**: https://flashdata.dev/docs/sources/youtube_captions
- **Get video license metadata**: https://flashdata.dev/docs/sources/youtube_trainability
- **Get a channel**: https://flashdata.dev/docs/sources/youtube_channel
- **Search suggestions**: https://flashdata.dev/docs/sources/youtube_suggestions
- **Download a video**: https://flashdata.dev/docs/sources/youtube_download

Each search returns a separate bundle per result. Keep paid downstream operations out of unintended fan-out. Google searches default to at most one paid page; raise Maximum paid pages explicitly to allow further pages. Limit defaults to 10; fewer results may exist.

Transcript defaults to automatic captions; Captions defaults to uploader tracks. No caption-source fallback or translation occurs. License Metadata reads a Creative Commons label, not creator training permission.

Download requires your own writable storage. Submission returns a job ID. Read status until completed; use the FlashData console for the stored result while the Make result reader is unavailable. Do not submit again to check progress. Completed JSON describes the file in your storage. Credentials must stay out of public templates.

## Utilities

Get a job status reads existing work without creating another paid query. Get a job result currently stops before the result-link request. The universal URL field rejects results paths during this limitation. Make an API call selects either the fixed Data or Management API origin. Use Management API with /v2/api-access for a harmless access check. Authorization comes from the connection; arbitrary external URLs are rejected.

Errors retain the API status and explanation. Paid submissions are not automatically retried by these module definitions. After a timeout, inspect Jobs before running again. Current outputs are direct fields; remap older result.field paths to field and remove uses of raw.

Documentation: https://flashdata.dev/docs/api-reference
Source and task blueprints: https://github.com/flashdata-dev/make-app-flashdata

This integration does not imply endorsement by Google or YouTube.
