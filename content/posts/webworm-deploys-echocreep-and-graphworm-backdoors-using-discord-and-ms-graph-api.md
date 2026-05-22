---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API"
date: 2026-05-20T12:51:43+00:00
draft: false
categories:
  - malware
---

**Summary of Cybersecurity Article: Webworm Deploys Custom Backdoors Using Discord and MS Graph API**

Cybersecurity researchers have identified new activity from the China-aligned threat actor Webworm, which has been active since at least 2022. Webworm has been targeting government agencies and enterprises in various sectors, including IT services, aerospace, and electric power, in countries such as Russia, Georgia, Mongolia, and several other Asian nations.

**New Backdoors: EchoCreep and GraphWorm**

Webworm has added two new custom backdoors to its toolkit: EchoCreep and GraphWorm. EchoCreep uses Discord for command-and-control (C2) communications, while GraphWorm uses Microsoft Graph API. These backdoors allow for file upload/download, command execution, and other malicious activities.

**Tactics, Techniques, and Procedures (TTPs)**

Webworm's TTPs include:

1. Using GitHub repositories to host malware and tools, such as SoftEther VPN.
2. Leveraging open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories.
3. Employing custom proxy tools, such as WormFrp, ChainWorm, SmuxProxy, and WormSocket, to encrypt communications and chain across multiple hosts.
4. Utilizing Discord and Microsoft Graph API for C2 communications.

**Overlaps with Other Threat Actors**

Webworm's links to other threat actors, such as Space Pirates, are tenuous at best, with the use of open-source RATs being the primary connection.

**Implications**

The discovery of EchoCreep and GraphWorm marks an expansion of Webworm's arsenal, highlighting the group's continued evolution and adaptation. The use of custom backdoors and proxy tools demonstrates Webworm's efforts to remain stealthy and evade detection.

**Recommendations**

Organizations should be aware of Webworm's TTPs and take measures to prevent and detect these types of attacks, including:

1. Monitoring for suspicious activity on Discord and Microsoft Graph API.
2. Implementing security controls to prevent brute-force attacks and unauthorized access.
3. Using threat intelligence to stay informed about Webworm's evolving TTPs.

By understanding Webworm's tactics and techniques, organizations can better protect themselves against these types of cyber threats.

---

> *A man is not where he lives but where he loves.*

Source: [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
