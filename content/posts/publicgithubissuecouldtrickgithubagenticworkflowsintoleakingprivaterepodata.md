---
title: "Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data"
date: 2026-07-07T14:04:50+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Vulnerability Overview**
Researchers at Noma Security have discovered a vulnerability in GitHub Agentic Workflows, a feature that allows users to write instructions to an AI agent in plain English. The vulnerability, dubbed "GitLost," can trick the agent into leaking private repository data by creating a public issue with malicious instructions. This can be done without stolen credentials or access to the organization, as long as the agent has read access to the organization's repositories.

**How the Attack Works**
The attack exploits a known weakness called indirect prompt injection, where an AI agent cannot distinguish between instructions from its owner and those hidden in the content it reads. By writing malicious instructions into a public issue, an attacker can manipulate the agent into pulling private data and posting it in a public comment. GitHub has built guardrails to prevent this, including sandboxing and input cleaning, but Noma's researchers found that a one-word change was enough to bypass these defenses.

**Implications and Mitigations**
The GitLost vulnerability is particularly concerning because it allows an attacker to control what an agent does with its permissions, rather than just manipulating what it says. To mitigate this risk, organizations can scope agent tokens to specific repositories rather than granting broad org-wide read access. They can also limit what a public-facing workflow can post and restrict which authors' content the agent will act on. Ultimately, the fix relies on architecture, isolation, scoped credentials, and staged review, rather than just filtering out malicious input.

---

> *The best thing in every noble dream is the dreamer...
Author: Moncure Conway*

Source: [Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data](https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html)
