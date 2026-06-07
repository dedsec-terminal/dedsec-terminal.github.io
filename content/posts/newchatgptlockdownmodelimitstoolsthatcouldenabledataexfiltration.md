---
title: "New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration"
date: 2026-06-06T13:36:57+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

OpenAI has introduced a new "Lockdown Mode" for ChatGPT, designed to reduce the risk of data exfiltration from prompt injection attacks. This feature is primarily aimed at individuals and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across various plans, including Free, Go, Plus, and Pro, as well as self-serve ChatGPT Business plans.

Lockdown Mode limits several tools and capabilities in ChatGPT that can connect to the web or external services, including live web browsing, image support, deep research, agent mode, and file downloads. By disabling these features, Lockdown Mode reduces the risk of data exfiltration by limiting outbound network requests that could potentially transmit sensitive data to attacker-controlled infrastructure. However, OpenAI notes that Lockdown Mode is not intended for everyone and cannot be used simultaneously with Developer Mode.

The introduction of Lockdown Mode is part of OpenAI's efforts to harden the attack surface against prompt injections, a ongoing problem affecting large language models. While Lockdown Mode substantially reduces the risk of prompt injection-based data exfiltration, it does not guarantee complete security. OpenAI also launched a new account management feature that allows users to review active ChatGPT sessions and log out of individual or all sessions if signs of unauthorized account activity are detected, providing an additional layer of security and control.

---

> *Progress always involves risks. You can't steal second base and keep your foot on first.
Author: Frederick Wilcox*

Source: [New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration](https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html)
