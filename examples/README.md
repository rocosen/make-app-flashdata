# Manual Make example

`video-tools.blueprint.json` is exported from the tested app scenario and has its saved connection reference removed. Import it into Make, install/access the FlashData app, and select your own FlashData connection on every module. Install the app through its [invite link](https://www.make.com/en/hq/app-invitation/22c4a874cb7ddbf30b9f20e0e270477d) first; this file alone does not grant app access.

The chain runs metadata, transcript, a universal metadata request, then video search. Each module runs once; search is last so its two bundles cannot multiply paid downstream calls. The universal metadata call is included to demonstrate that module and is redundant for a production workflow. One full test run consumed 4 Make credits and 0.016 FlashData credits on 2026-10-10; actual pricing and results can change.

Keep scheduling inactive and use Run once. Use the 11-character video ID, explicit language and subtitle type. Before retrying an uncertain request, check FlashData Jobs.
