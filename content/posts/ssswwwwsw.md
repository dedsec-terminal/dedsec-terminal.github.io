---
title: "Chinese hackers target telcos with new Linux, Windows malware"
date: 2026-05-21T14:00:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A recent cybersecurity campaign attributed to the Calypso threat group, also known as Red Lamassu, has been targeting telecommunications providers in the Asia Pacific and Middle East regions. The campaign, which has been active since at least mid-2022, utilizes newly discovered Linux and Windows malware dubbed Showboat and JFMBackdoor, respectively. The threat actors have set up multiple telecom-themed domains to impersonate their targets, allowing them to gain initial access to the target systems.

The Showboat Linux malware is a modular post-exploitation framework designed for long-term persistence after initial compromise. Once deployed, it collects information about the host system and sends it to a command-and-control server. The malware also has the ability to upload or download files, hide its own process, and establish persistence via a new service. Notably, it can act as a SOCKS5 proxy and port-forwarding pivot point, enabling the attackers to move to other systems on the internal network.

The JFMBackdoor Windows malware, on the other hand, is a full-featured espionage implant that provides the attackers with a range of capabilities, including reverse shell access, file management, TCP proxying, and process/service management. It can also capture screenshots of the victim's desktop, modify Windows registry keys, and store/update malware settings in encrypted configurations. The malware can also self-remove and perform anti-forensics activities to hide its presence.

The infrastructure analysis of the campaign suggests that the hackers follow a partially decentralized operational model, with multiple clusters sharing similar certificate-generation patterns and tooling but targeting distinct victim sets. This suggests that the tooling is likely shared across multiple China-aligned threat groups, each targeting different regions and using the same malware ecosystem. The discovery of these malware variants highlights the importance of continued vigilance and monitoring of telecommunications networks to detect and prevent such attacks.

---

> *Peace is not something you wish for. It's something you make, something you do, something you are, and something you give away.
Author: Robert Fulghum*

Source: [Chinese hackers target telcos with new Linux, Windows malware](https://www.bleepingcomputer.com/news/security/chinese-hackers-target-telcos-with-new-linux-windows-malware/)
