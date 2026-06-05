---
title: "Claude Code GitHub Action Flaw Let One Malicious Issue Hijack Repositories"
date: 2026-06-04T15:15:26+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A security researcher, RyotaK, discovered a flaw in Anthropic's Claude Code GitHub Action that allowed an attacker to take over vulnerable public repositories with just a single opened GitHub issue. The issue was caused by a hole in the trigger check, which assumed that any actor with a name ending in "[bot]" was trusted. This allowed an attacker to register a GitHub App, install it on a repo they owned, and use its token to open an issue or pull request on any public repository, bypassing the action's permissions.

The attacker could then use indirect prompt injection to plant instructions inside content that the AI reads, causing it to follow the attacker's commands instead of its actual task. RyotaK demonstrated how an attacker could use this technique to steal environment variables, including GitHub Actions credentials, and gain write access to the target repository. The researcher also identified other vulnerabilities, including a softer route that skipped the bot trick entirely and a path for an attacker who can edit issues but can't trigger Claude on their own.

The issue has been fixed in claude-code-action v1.0.94 or later, and Anthropic has paid a bug bounty to RyotaK. To protect themselves, users should update to the latest version and audit any workflow that lets users without write access or bots trigger Claude. RyotaK has reported around 50 separate ways to bypass Claude Code's permission system, highlighting the ongoing issue of prompt injection flaws in AI coding agents. The researcher's findings demonstrate the importance of securing AI-powered tools and the need for continued vigilance in protecting against these types of vulnerabilities.

---

> *If one is lucky, a solitary fantasy can totally transform one million realities.
Author: Maya Angelou*

Source: [Claude Code GitHub Action Flaw Let One Malicious Issue Hijack Repositories](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html)
