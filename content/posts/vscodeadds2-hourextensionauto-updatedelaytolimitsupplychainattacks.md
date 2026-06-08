---
title: "VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks"
date: 2026-06-08T06:08:44+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Microsoft has introduced a new feature in Visual Studio Code (VS Code) to enhance security against software supply chain threats. The feature, available in VS Code 1.123, applies a two-hour delay before extensions are automatically updated to a newer version. This delay adds an extra layer of protection against potentially compromised or problematic releases.

The two-hour delay does not apply to extensions from trusted publishers, such as Microsoft, GitHub, and OpenAI, which will continue to be updated immediately. Users can still update any extension immediately by using the "Update" button, and pending updates will display a reason for the delay and the scheduled update time. This feature is part of a broader effort to mitigate software supply chain risks, which have seen a significant surge in recent times.

Similar installation controls have been introduced in other package managers, including RubyGems, Bun, npm, pnpm, and Yarn. These controls allow developers to configure a time-based install delay, reducing the exposure to newly published malicious versions. By enforcing a minimum age threshold before a package version can be installed, these defensive controls minimize the window during which malware can spread before being flagged and taken down by registry maintainers.

---

> *Fortune befriends the bold.
Author: John Dryden*

Source: [VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html)
