---
title: "Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy"
date: 2026-07-17T10:00:24+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

Researchers at Palo Alto Networks, in partnership with Siemens, have discovered three zero-day vulnerabilities in Siemens ROX II operational technology (OT) switches. The vulnerabilities, identified as CVE-2025-40948, CVE-2025-40947, and CVE-2025-40949, can be chained together to allow an attacker to achieve full privilege escalation and persistent root-level access on these devices. The vulnerabilities range from Medium to Critical severity, with CVSS 3.1 scores of 6.8, 7.5, and 9.1, respectively.

The attack vector proceeds in three stages, starting with arbitrary file disclosure (CVE-2025-40948), which allows an attacker to read any file on the switch's file system. This is followed by privilege escalation via command injection (CVE-2025-40947), which enables an attacker to gain full root access. Finally, the attacker can establish persistent root code execution (CVE-2025-40949) by injecting malicious commands into the system's root cron table, allowing for ongoing malicious activity even after a reboot. Siemens has released security advisories to address these issues, recommending that customers update their affected ROX II devices to firmware version V2.17.1.

The discovery of these vulnerabilities highlights the importance of securing OT switches, which are critical components of industrial control networks. OT switches can become attack surfaces, allowing an unprivileged attacker to exploit software flaws and disrupt OT communication. The partnership between Palo Alto Networks and Siemens demonstrates the value of collaborative research and responsible disclosure in advancing the security and resilience of critical infrastructure. Palo Alto Networks customers are better protected against these threats through various products and services, including virtual patching detection signatures and OT Device Security.

---

> *It's easier to see the mistakes on someone else's paper.*

Source: [Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/)
