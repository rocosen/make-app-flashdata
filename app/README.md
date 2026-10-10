# FlashData

Search Google web results and retrieve YouTube video search results, metadata and transcripts using the FlashData API.

## Connect your account

1. Create an account at https://flashdata.dev and create a FlashData API key with access to the sources you need.
2. Add a FlashData module to your Make scenario, select Add under Connection, and enter your API key.
3. The connection uses the free API access endpoint to verify the key. Keep the key private.

API documentation: https://flashdata.dev/docs/api-reference

## Modules

- Search Web Results: enter a query, limit and page. Each organic result is a separate bundle. Page changes make a separate request; pages are not fetched automatically.
- Search Videos: enter a query and limit. Each video is a separate bundle.
- Get Video Metadata: enter an 11-character video ID and choose whether to include chapters and formats.
- Get Video Transcript: enter a video ID, language and automatic/manual subtitle choice. Missing subtitles do not trigger a fallback query.
- Make an API call: use a relative path on data.flashdata.dev, an HTTP method and, where required, a JSON body. The app adds authentication; arbitrary external URLs are not accepted.

## Costs and troubleshooting

Queries consume FlashData credits. Make credits are billed separately. Start with Run once and a small result limit. Each output bundle repeats the usage of the same query; do not sum those values across bundles. Paid modules after a search execute once per returned bundle.

If a query fails or its outcome is uncertain, inspect Jobs in the FlashData console before running it again. Do not add automatic retries unless you accept possible duplicate charges. A 401 error indicates an invalid key; 402 indicates insufficient credits; 404 indicates an unknown path or resource.

Source and examples: https://github.com/flashdata-dev/make-app-flashdata

This app uses FlashData's API and does not imply endorsement by Google or YouTube.
