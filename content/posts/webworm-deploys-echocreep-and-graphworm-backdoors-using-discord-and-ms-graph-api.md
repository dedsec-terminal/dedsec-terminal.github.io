---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API"
date: 2026-05-20T12:51:43+00:00
draft: false
categories:
  - malware
---

**Summary of Cybersecurity Article: Webworm Deploys EchoCreep and GraphWorm Backdoors**

Cybersecurity researchers have identified new activity from the China-aligned threat actor Webworm, which has been active since at least 2022. Webworm has been targeting government agencies and enterprises in various sectors, including IT services, aerospace, and electric power, in countries such as Russia, Georgia, Mongolia, and several other Asian nations.

**New Backdoors: EchoCreep and GraphWorm**

Webworm has added two new custom backdoors to its toolset:

1. **EchoCreep**: Uses Discord for command-and-control (C2) communications and supports file upload/download and command execution via "cmd.exe" capabilities.
2. **GraphWorm**: Uses Microsoft Graph API for C2 communications and can spawn a new "cmd.exe" session, execute a newly created process, upload and download files to and from Microsoft OneDrive, and stop its own execution after receiving a signal from the operators.

**Tactics, Techniques, and Procedures (TTPs)**

Webworm's TTPs include:

* Using open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories, and search for vulnerabilities within.
* Leveraging a GitHub repository impersonating a WordPress fork as a staging ground for malware and tools.
* Utilizing SoftEther VPN to blend in and fly under the radar.
* Employing custom proxy tools, such as WormFrp, ChainWorm, SmuxProxy, and WormSocket, to encrypt communications and support chaining across multiple hosts.

**Relationship with Other Threat Actors**

Webworm's relationship with other threat actors, such as Space Pirates, is tenuous at best, with no concrete evidence tying the two clusters together.

**Implications**

The discovery of EchoCreep and GraphWorm marks an expansion of Webworm's arsenal, and the group's shift towards using custom proxy tools and legitimate utilities to evade detection. The use of Discord and Microsoft Graph API for C2 communications highlights the threat actor's ability to adapt and evolve its TTPs.

---

> *Argue for your limitations, and sure enough they're yours.
Author: Richard Bach*

Source: [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
