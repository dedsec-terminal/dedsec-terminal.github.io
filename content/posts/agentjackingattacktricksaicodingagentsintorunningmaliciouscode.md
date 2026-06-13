---
title: "Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code"
date: 2026-06-12T12:04:33+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers at Tenet Security have discovered a new class of attack called "Agentjacking" that can trick artificial intelligence (AI) coding agents into running malicious code on developer machines. The attack exploits a flaw in the intersection of Sentry's error-tracking platform and AI agents, allowing attackers to inject crafted input into error events that are then interpreted as legitimate diagnostic steps. This can lead to the exposure of sensitive data, including environment variables, Git credentials, and developer identities, without relying on methods like phishing or prior server compromise.

The attack chain involves an attacker finding a target's Sentry Data Source Name (DSN), sending a malicious error event to Sentry's ingest endpoint, and then having the AI agent execute the malicious code when it queries Sentry via Model Context Protocol (MCP). The malicious instruction is disguised as a legitimate "Resolution" inside an ordinary error, and the AI agent runs it with the developer's full privileges. Tenet Security found that at least 2,388 organizations are exposed with valid injectable DSNs and achieved an 85% exploitation success rate against injected errors in a controlled test.

The Agentjacking attack highlights the vulnerability of AI coding agents and the trust that developers place in them. Sentry has acknowledged the issue but has not fixed it, opting instead to activate a global content filter that blocks a specific payload string. The attack bypasses traditional security measures such as EDR, WAF, IAM, VPN, and firewalls because every action in the chain is authorized. As enterprises increasingly deploy AI coding agents, this research demonstrates that the agents themselves can become the attack surface, turned against the developers who trust them using publicly available data.

---

> *Great talent finds happiness in execution.
Author: Johann Wolfgang von Goethe*

Source: [Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html)
