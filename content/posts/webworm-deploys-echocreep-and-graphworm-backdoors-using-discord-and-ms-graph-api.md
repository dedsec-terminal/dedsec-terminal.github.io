---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API"
date: 2026-05-20T12:51:43+00:00
draft: false
categories:
  - malware
---

**Summary of Cybersecurity Article: Webworm Deploys Custom Backdoors Using Discord and MS Graph API**

Cybersecurity researchers have identified new activity from the China-aligned threat actor "Webworm" in 2025. Webworm has been active since at least 2022, targeting government agencies and enterprises in various sectors, including IT services, aerospace, and electric power, in countries such as Russia, Georgia, Mongolia, and several other Asian nations.

**New Backdoors: EchoCreep and GraphWorm**

Webworm has added two new custom backdoors to its toolset:

1. **EchoCreep**: Uses Discord for command-and-control (C2) communications, allowing file upload/download and command execution via "cmd.exe" capabilities.
2. **GraphWorm**: Uses Microsoft Graph API for C2 communications, enabling advanced capabilities such as spawning a new "cmd.exe" session, executing newly created processes, uploading and downloading files to and from Microsoft OneDrive, and stopping its own execution after receiving a signal from the operators.

**Tactics, Techniques, and Procedures (TTPs)**

Webworm's TTPs include:

* Using a GitHub repository impersonating a WordPress fork as a staging ground for malware and tools
* Leveraging SoftEther VPN to blend in and fly under the radar
* Shifting away from traditional backdoors to (semi-)legitimate utilities such as SOCKS proxies
* Increasingly focusing on European countries, including governmental organizations and a local university in South Africa
* Using custom proxy tools, such as WormFrp, ChainWorm, SmuxProxy, and WormSocket, to encrypt communications and chain across multiple hosts

**Initial Access Pathway and Delivery**

The initial access pathway and delivery method used by Webworm are currently unknown. However, the attacker utilizes open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories and search for vulnerabilities within.

**Related Malware-as-a-Service (MaaS) Model**

The article also mentions a BadIIS variant, likely sold or shared among multiple Chinese-speaking cybercrime groups under a MaaS model, which offers a set of supplementary tools for automation, survivability, and evasion. The same malware author has made available a dedicated builder tool for generating configuration files, customizing payloads, and injecting parameters into BadIIS binaries.

---

> *Where all think alike, no one thinks very much.
Author: Walter Lippmann*

Source: [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
