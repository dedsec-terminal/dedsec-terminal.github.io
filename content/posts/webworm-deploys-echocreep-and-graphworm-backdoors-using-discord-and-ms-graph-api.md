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

Webworm has deployed two new custom backdoors, EchoCreep and GraphWorm, which use Discord and Microsoft Graph API for command-and-control (C2) communications. EchoCreep supports file upload/download and command execution, while GraphWorm is a more advanced backdoor that can spawn new processes, execute commands, and upload/download files to/from Microsoft OneDrive.

**Tactics, Techniques, and Procedures (TTPs)**

Webworm's TTPs include:

1. Using open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories.
2. Leveraging SoftEther VPN to blend in and fly under the radar.
3. Utilizing custom proxy tools, such as WormFrp, ChainWorm, SmuxProxy, and WormSocket, to encrypt communications and chain across multiple hosts.
4. Impersonating a WordPress fork on GitHub to stage malware and tools.

**Overlaps with Other Threat Actors**

Webworm's links to other threat actors, such as Space Pirates, are tenuous at best, with the use of open-source RATs being the primary connection. However, ESET researchers believe that Webworm's activity is distinct and not directly related to other groups.

**Conclusion**

The discovery of EchoCreep and GraphWorm marks an expansion of Webworm's arsenal, highlighting the group's continued evolution and adaptation to evade detection. The use of custom backdoors and proxy tools demonstrates Webworm's sophistication and ability to operate stealthily. As the threat landscape continues to evolve, it is essential for organizations to remain vigilant and proactive in detecting and mitigating potential threats.

---

> *Let us revere, let us worship, but erect and open-eyed, the highest, not the lowest; the future, not the past!
Author: Charlotte Gilman*

Source: [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
