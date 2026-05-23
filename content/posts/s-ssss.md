---
title: "Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets"
date: 2026-05-14T17:22:43+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered malicious activity in three versions of the node-ipc npm package, specifically node-ipc@9.1.6, node-ipc@9.2.3, and node-ipc@12.0.1. These versions contain obfuscated stealer/backdoor behavior that attempts to exfiltrate a broad set of developer and cloud secrets to an external command-and-control server. The malware is triggered when the package is required at runtime and can harvest over 90 categories of credentials, including Amazon Web Services, Google Cloud, and Microsoft Azure.

The malicious payload is appended as an Immediately Invoked Function Expression (IIFE) to the end of "node-ipc.cjs," causing it to fire unconditionally on every require('node-ipc'). The payload performs a SHA-256 fingerprint check and compares it against a hard-coded hash before proceeding with system enumeration and credential harvesting. Notably, version 12.0.1 is entirely inert on any machine whose primary module path does not hash to the target value, suggesting that the attacker knows exactly which project or developer is being targeted.

The malware incorporates multiple exfiltration channels, including issuing an HTTPS POST to a fake Azure domain and encoding chunks of the archive as a DNS TXT record. The latter involves overriding the system's DNS resolver with Google Public DNS to sidestep local DNS-based security controls. The malware also attempts to continue execution independently of the original Node.js process by forking itself into a detached background child process, allowing exfiltration activity to continue silently after the parent application is terminated.

The incident highlights the evolving nature of software supply chain attacks, which are increasingly targeting identities and automation systems powering modern software delivery pipelines. Users are advised to remove the compromised node-ipc versions, re-install a known clean version, and rotate credentials and secrets. Additionally, users should audit npm publish activity, review workflow run logs, and block egress traffic to the command-and-control domain. The investigation suggests that the dormant maintainer's account may have been taken over via an expired email domain, allowing the attacker to gain publish rights without compromising the maintainer's infrastructure.

---

> *As long as your going to be thinking anyway, think big.
Author: Donald Trump*

Source: [Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)
