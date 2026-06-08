---
title: "OpenAI is locking down parts of ChatGPT to reduce data theft risks"
date: 2026-06-08T07:58:46+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

OpenAI has introduced Lockdown Mode for ChatGPT, a security setting designed to reduce data theft risks by restricting access to external resources and certain product capabilities. This optional feature is available for personal accounts, including Free, Go, Plus, and Pro plans, as well as self-serve ChatGPT Business accounts. Lockdown Mode is intended for individuals and organizations that handle sensitive data and want stronger protection against data exfiltration risks associated with prompt injection.

When Lockdown Mode is enabled, several ChatGPT capabilities are restricted, including web browsing, search results, and file downloads. Deep Research and Agent Mode are also disabled, and users cannot approve Canvas-generated code that requires network access. However, Lockdown Mode does not affect memory, file uploads, conversation sharing, or model improvement. Additionally, workspace administrators can manage these settings separately, and the feature does not affect network access in Codex.

Lockdown Mode combines sandboxing, protections against URL-based data exfiltration, monitoring, and enforcement mechanisms to provide protection at the model, product, and system levels. Administrators are advised to review the data exfiltration risk of each app and action before enabling them for members using Lockdown Mode. The feature also provides visibility into app usage, shared data, and connected sources through the Compliance API Logs Platform. It's worth noting that Lockdown Mode and Developer Mode cannot be enabled simultaneously, and enabling one will disable the other.

---

> *I think somehow we learn who we really are and then live with that decision.
Author: Eleanor Roosevelt*

Source: [OpenAI is locking down parts of ChatGPT to reduce data theft risks](https://www.helpnetsecurity.com/2026/06/08/openai-lockdown-mode-available/)
