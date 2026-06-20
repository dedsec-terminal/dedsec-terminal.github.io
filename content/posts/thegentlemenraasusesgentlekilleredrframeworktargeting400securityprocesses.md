---
title: "The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes"
date: 2026-06-19T18:33:07+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The Gentlemen ransomware-as-a-service (RaaS) operation has been found to be actively developing and maintaining a suite of endpoint detection and response (EDR) killers. These tools, centered around a framework known as GentleKiller, are used to impair system defenses before deploying the encryptor. The GentleKiller framework incorporates third-party or leaked tools, such as HexKiller, ThrottleBlood, and HavocKiller, which are standardized through a shared defense-evasion layer. This layer impersonates security vendors using fake version information, copied legitimate certificates, and icons.

The Gentlemen RaaS operation has been identified as one of the most technically agile RaaS groups, using a set of techniques to ensure that the compiled EDR killer samples sidestep detection. The group's EDR killers, including GentleKiller, target 400 processes associated with 48 distinct security programs from various vendors. The operation has also been found to quickly operationalize newly disclosed proof-of-concept (PoC) exploits, often within days of their public release. This has allowed the group to swiftly rise up the ranks and claim 504 victims to date, with most of them located in Southeast Asia, South America, and Western Europe.

The use of GentleKiller and other EDR killers by The Gentlemen RaaS operation has significant implications for system security. The group's ability to centralize the EDR-killing function and offer affiliates a ready-to-use, standardized EDR-killer suite makes it an attractive operator for affiliates. This decision also lowers the entry barrier for affiliates, making their job easier. To mitigate the risk of BYOVD attacks, system administrators should apply updates to the UEFI Forbidden Signature Database (DBX) that revoke trust in affected vendor-signed binaries, preventing vulnerable applications from executing during the boot process. Additionally, users should be aware of the potential for ransomware attacks and take steps to protect their systems, including keeping software up to date and using robust security measures

---

> *It is better to take many small steps in the right direction than to make a great leap forward only to stumble backward.*

Source: [The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html)
