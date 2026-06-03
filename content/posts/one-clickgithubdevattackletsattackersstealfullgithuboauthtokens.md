---
title: "One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens"
date: 2026-06-03T12:58:22+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a one-click attack that can steal a user's GitHub token through Microsoft Visual Studio Code (VS Code). This attack is made possible by exploiting a vulnerability in the GitHub.dev feature, which runs a lightweight web-based source code editor in the browser's sandbox. By clicking a link, an attacker can steal a GitHub token that has full access to all of a user's repositories, including private ones.

The vulnerability allows attackers to install malicious VS Code extensions that steal GitHub OAuth tokens when they are passed to GitHub.dev. This is achieved by exploiting a message-passing mechanism between the main VS Code window and webviews, which are used to render Markdown previews or edit Jupyter notebooks. The exploit runs malicious JavaScript inside an untrusted webview, simulating keypresses to install an attacker-controlled extension that extracts the GitHub OAuth token and queries the GitHub API to enumerate all private repositories the victim can access.

GitHub was notified of the vulnerability on June 2, 2026, and Microsoft has acknowledged the issue and is working on a fix. The vulnerability does not affect VS Code Desktop, according to Microsoft. The researcher who discovered the vulnerability noted that they made the details public an hour after notifying GitHub, citing Microsoft's handling of VS Code-related bugs in the past. The attack highlights the importance of being cautious when clicking links and installing extensions, and the need for developers to prioritize security when building features like GitHub.dev.

---

> *Good instincts usually tell you what to do long before your head has figured it out.
Author: Michael Burke*

Source: [One-Click GitHub Dev Attack Lets Attackers Steal Full GitHub OAuth Tokens](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html)
