# Task blueprints

**Current limitation (2026-10-14):** Fourteen data capabilities passed live Make tests. Video download/storage execution remains unverified. Get a job result is temporarily disabled before requesting the signed result link because Make still followed redirects with both documented flags set to false. Keep the job ID and use the FlashData console for stored results; do not resubmit paid work.

`tasks.json` holds 15 task-specific descriptions, 30 natural queries and source deep links. `tasks/` contains one blueprint and guide per source. The 15 platform IDs now identify private team drafts, not public entries. Public URLs remain null because publication is blocked. See the [platform record](../docs/platform-state-2026-10-14.md).

Install the [invite app](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d), import a blueprint and select your own connection. Free installation does not include paid FlashData requests or Make credits. No template runs a language model or includes a saved connection or key.

Google task blueprints default to one paid page. Search modules are terminal so they do not fan out into paid enrichment calls. The download draft requires private customer storage and is not ready for execution. Its intended flow reads status and then a manifest, but result retrieval is currently disabled. `read-download-job.blueprint.json` contains no submission module; it can read status but now stops with the explicit result-reader limitation. Inspect existing results in the FlashData console. The source download blueprint omits storage values and sets confidential execution metadata. Make requires a provider and bucket to save its wizard, so the private platform draft uses an S3 example with nonfunctional credential/bucket placeholders. Those private fields are not wizard defaults; users must supply their own destination. The platform draft also has Keep data confidential enabled.

`video-tools.blueprint.json` is the historical four-module review export. It uses old output metadata and costs four query calls. It is preserved for evidence, not the recommended new task entry.

Make template descriptions are limited to 1,500 characters and scenario descriptions to 240. Team templates, published share links, approval requests and inclusion in the public library are separate milestones. See [Make template rules](https://help.make.com/create-and-manage-scenario-templates).
