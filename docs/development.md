# Development and deployment

This source uses Make's native declarative custom-app format. No external runtime, CLI, MCP server or npm package is required to run it on Make.

## Current review work

Make posted Changes required on 2026-10-11. This expansion must use the same app and original review. The 18 modules and 15 private task-template drafts are now saved separately in the editor; see [actual platform state](platform-state-2026-10-14.md). Creating source alone does not create platform objects. Complete the [review checklist](review-update.md), and record each saved component and template ID. Preserve source before modifying the live editor because unapproved-app changes take effect immediately. Do not run paid queries or storage writes beyond the agreed test budget.

## Published app

The development app was created on 2026-10-10 (Asia/Singapore) with internal identifier `flashdata-g6iv9y`, version `1.0.0`, region US2. This identifier is assigned by Make; it differs from the requested name `flashdata`. The app was published on 2026-10-10 for [invite-link installation](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d); technical review was requested on the same date and the platform shows `pending approval`. Official approval and directory listing are separate.

Developer editor (owner login required): https://us2.make.com/apps/flashdata-g6iv9y/1/base

The API Key connection was assigned identifier `flashdata-g6iv9y`. Bind modules to the connection labelled **FlashData** when creating them. The `connection` value in local module metadata is a logical source reference, not an already-deployed Make connection ID.

## Edit through the web UI

1. Open the app and paste `app/base.json` into Base. Keep Common data empty.
2. Create a connection labelled FlashData, type API Key. Paste its `communication.json` and `parameters.json` into their matching tabs. Common data stays empty.
3. Create a module using its metadata label/type/description; bind the FlashData connection. Paste the communication, static parameters, mappable parameters, interface and samples files into their matching tabs.
4. Save each tab and verify the save completed before leaving it. A source file on GitHub does not prove the platform saved it.
5. Add the module to a manually run scenario. Create a connection with a user-owned FlashData API key. Test the free connection first, then a small paid query.
6. Record scenario IDs, execution results, module version and cost in the private GTM issue. Public evidence must exclude credentials and account data.

No Make management token is needed for this web-editor workflow. The official VS Code extension is an optional future development tool and requires separately configured `sdk-apps:read` and `sdk-apps:write` access.

## Release milestones

Private testing, GitHub source publication, Make Publish/invite link, technical review and public catalogue listing are separate milestones. Publishing a Make app cannot simply be reversed to private. Complete validation and remove temporary components before using Publish.

Search/video data app eligibility has not yet been confirmed by Make. Neutral app/module labels avoid third-party brand names; descriptions and documentation accurately identify Google/YouTube sources. Do not imply endorsement by those services or Make.

## Authoritative references

- [Basic connection](https://developers.make.com/custom-apps-documentation/app-components/connections/basic-connection)
- [Requests, redirects and log sanitization](https://developers.make.com/custom-apps-documentation/component-blocks/api/making-requests)
- [Error types and retry behavior](https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/error)
- [Search modules](https://developers.make.com/custom-apps-documentation/app-components/modules/search)
- [Interfaces](https://developers.make.com/custom-apps-documentation/component-blocks/interface)
- [Review prerequisites](https://developers.make.com/custom-apps-documentation/app-review/prerequisites)
