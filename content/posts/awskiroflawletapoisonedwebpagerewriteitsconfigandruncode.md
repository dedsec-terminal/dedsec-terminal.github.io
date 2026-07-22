---
title: "AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code"
date: 2026-07-21T16:06:12+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

A vulnerability was discovered in AWS Kiro, a coding IDE, that allowed a poisoned web page to rewrite its configuration file and run an attacker's code on a developer's machine without approval. The flaw was found by Intezer and Kodem Security, who demonstrated that a request to summarize a web page could lead to remote code execution. The issue was patched by AWS, but no CVE was assigned to it.

The vulnerability exploited Kiro's safety model, which relies on a human approving potentially risky actions. However, the flaw allowed an attacker to slip past this approval step by modifying the `mcp.json` file, which tells Kiro which external tools to load. By hiding malicious instructions in a web page, an attacker could trick Kiro into writing to the `mcp.json` file and reloading it, allowing arbitrary code to be executed with the developer's privileges.

The issue has been patched by AWS, which has implemented a new security model that marks sensitive files as protected paths, requiring explicit approval before a write. This fix closes the vulnerability and prevents similar attacks in the future. The incident highlights the importance of platform-level security controls in AI-powered coding tools, which can be vulnerable to prompt-injection attacks that exploit legitimate editor features. The fix is available in the latest version of Kiro, and users are advised to update to the latest version to ensure their security.

---

> *Sometimes our fate resembles a fruit tree in winter. Who would think that those branches would turn green again and blossom, but we hope it, we know it.
Author: Johann Wolfgang von Goethe*

Source: [AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code](https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html)
