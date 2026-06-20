---
title: "AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution"
date: 2026-06-19T15:30:47+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft researchers have discovered an exploit chain called AutoJack, which allows a web page to hijack an AI browsing agent and execute code on the host machine. The vulnerability exists in the AutoGen Studio, an open-source prototyping interface for Microsoft Research's AutoGen multi-agent framework. By loading a malicious web page, an attacker can use JavaScript to reach a privileged local service and spawn a process on the host machine without requiring any credentials or user interaction.

The AutoJack attack chain exploits three weaknesses in the Model Context Protocol (MCP) WebSocket. Firstly, the socket trusts localhost, allowing a browsing agent running on the same machine to inherit this trust. Secondly, the authentication middleware skips MCP paths, assuming that the handler will verify tokens itself. Finally, the endpoint takes a command straight from a request parameter and runs it without any allowlist or authentication. This allows a malicious web page to run an attacker-chosen command under the account running AutoGen Studio.

To mitigate the vulnerability, users who installed a pre-release version of AutoGen Studio (0.4.3.dev1 or 0.4.3.dev2) should pull the fixed code from GitHub main at or after commit b047730. Users who installed the stable release (0.4.2.2) are not affected. As a temporary workaround, users can separate the browsing agent and AutoGen Studio by running them in separate containers or VMs, or by running AutoGen Studio under a low-privilege account. Microsoft expects similar vulnerabilities to exist in other agent frameworks and emphasizes the importance of authenticating the control plane, keeping process execution behind an allowlist, and giving agents a separate identity.

---

> *Great talent finds happiness in execution.
Author: Johann Wolfgang von Goethe*

Source: [AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution](https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html)
