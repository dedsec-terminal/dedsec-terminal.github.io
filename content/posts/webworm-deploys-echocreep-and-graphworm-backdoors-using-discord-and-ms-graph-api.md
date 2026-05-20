---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API"
date: 2026-05-20T12:51:43+00:00
draft: false
categories:
  - malware
---

**Summary of Cybersecurity Article: Webworm Deploys Custom Backdoors Using Discord and MS Graph API**

Cybersecurity researchers have identified new activity from the China-aligned threat actor "Webworm" in 2025. Webworm has been active since at least 2022, targeting government agencies and enterprises in various sectors, including IT services, aerospace, and electric power, in several Asian nations and European countries.

**New Backdoors: EchoCreep and GraphWorm**

Webworm has deployed two new custom backdoors:

1. **EchoCreep**: Uses Discord for command-and-control (C2) communications, allowing file upload/download and command execution via "cmd.exe" capabilities.
2. **GraphWorm**: Uses Microsoft Graph API for C2 communications, enabling advanced capabilities such as spawning a new "cmd.exe" session, executing processes, uploading/downloading files to/from Microsoft OneDrive, and stopping execution after receiving a signal from operators.

**Tactics, Techniques, and Procedures (TTPs)**

Webworm's TTPs include:

* Using GitHub repositories to host malware and tools, such as SoftEther VPN, to blend in and avoid detection.
* Leveraging open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories, and search for vulnerabilities.
* Employing custom proxy tools, such as WormFrp, ChainWorm, SmuxProxy, and WormSocket, to encrypt communications and chain across multiple hosts.
* Utilizing SoftEther VPN to cover tracks and increase stealth.

**Other Findings**

* Webworm has shifted away from traditional backdoors to (semi-)legitimate utilities like SOCKS proxies.
* The threat actor has expanded its targeting to European countries, including governmental organizations and a local university in South Africa.
* The discovery of EchoCreep and GraphWorm marks an expansion of Webworm's arsenal, while Trochilus and 9002 RAT appear to have been abandoned.

**Related Malware-as-a-Service (MaaS) Model**

The article also mentions a BadIIS variant, likely sold or shared among multiple Chinese-speaking cybercrime groups under a MaaS model, which offers a set of supplementary tools for automation, survivability, and evasion.

---

> *The heart has eyes which the brain knows nothing of.
Author: Charles Perkhurst*

Source: [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
