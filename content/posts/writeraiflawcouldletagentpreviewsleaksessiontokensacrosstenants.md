---
title: "Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants"
date: 2026-07-07T13:27:09+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers at Sand Security have discovered a critical vulnerability in Writer, an enterprise generative AI platform. The flaw, codenamed "WriteOut," allows an attacker to hijack a victim's Writer account and access sensitive data, including private chats, documents, and administrative controls. This can be done by creating an agent in the attacker's own Writer account, sharing a preview link, and tricking a victim into clicking on it while signed in with their own session.

The vulnerability exploits Writer's live preview feature, which allows users to preview applications via the Writer Framework. When a logged-in Writer user opens the malicious link, their browser attaches their Writer session cookie to the request, which is then sent to the attacker's sandbox. The attacker can then read the forwarded session token, exfiltrate it, and replay it to gain control of the victim's Writer account. This attack chain can be carried out without the attacker and victim belonging to the same organization, making it a significant threat to tenant isolation protections.

The issue has been addressed by Writer following responsible disclosure. The company has prevented user session cookies from being forwarded into sandbox previews and moved them to an isolated origin. The vulnerability was able to bypass Writer's guardrails, which were designed to block malicious code, by fetching and running a remote script instead of pasting the payload inline. Sand Security noted that Writer was not careless, but the checks in place looked at the instruction rather than the runtime behavior, making it relatively straightforward to bypass the guardrail and exploit the vulnerability.

---

> *Don't wait. The time will never be just right.
Author: Napoleon Hill*

Source: [Writer AI Flaw Could Let Agent Previews Leak Session Tokens Across Tenants](https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html)
