---
title: "Tracking Iranian APT Screening Serpens’ 2026 Espionage Campaigns"
date: 2026-05-22T13:00:42+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the report on Screening Serpens' 2026 espionage campaigns:

Unit 42 researchers have observed evidence of cyberattacks by the Iran-nexus advanced persistent threat (APT) group Screening Serpens, targeting entities in the U.S., Israel, and the United Arab Emirates, as well as two additional Middle Eastern entities. The group's recent activity demonstrates an increase in technical capabilities and operational resilience, with six new remote access Trojan (RAT) variants developed and deployed between February and April 2026. The timing of these campaigns aligns closely with the regional conflict that started in the Middle East on February 28, 2026.

Screening Serpens primarily targets technology sector professionals using highly tailored social engineering tactics, including personalized recruitment lures that impersonate trusted brands and hiring platforms. The group's infection chains begin with targeted spear phishing lures, leveraging DLL sideloading for execution, and route command and control (C2) traffic through a set of unique domains, mostly hosted by Azure. The researchers identified two new malware families, MiniUpdate and MiniJunk V2, which were deployed in concurrent espionage campaigns, with the most critical evolution being the use of AppDomainManager hijacking to disable security mechanisms in .NET applications.

The researchers analyzed the MiniUpdate and MiniJunk V2 malware families, which were used in coordinated attacks against targets in the U.S., Israel, and the UAE. The MiniUpdate family was used in two sets of coordinated attacks, with the malware variants showing continued refinement of their abilities over the course of a month. The researchers observed superficial changes to the malware, such as opcode mappings and specific functionalities, as well as rotation of C2 domains. The attacks were delivered via archive files, with tailored social engineering traps aimed at technical personnel, and used spoofed error windows and phishing landing pages to establish legitimacy with the target.

---

> *Logic will get you from A to B. Imagination will take you everywhere.
Author: Albert Einstein*

Source: [Tracking Iranian APT Screening Serpens’ 2026 Espionage Campaigns](https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/)
