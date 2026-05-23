---
title: "MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems"
date: 2026-05-18T08:57:34+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

A recently disclosed Windows zero-day flaw, codenamed MiniPlasma, enables attackers to escalate privileges to SYSTEM level on fully patched Windows systems. The vulnerability affects the Windows Cloud Files Mini Filter Driver, specifically the "cldflt.sys" component, and resides in the "HsmOsBlockPlaceholderAccess" routine. This issue was initially reported to Microsoft by Google Project Zero researcher James Forshaw in September 2020 and was believed to have been fixed in December 2020 as part of CVE-2020-17103.

However, further investigation by security researcher Chaotic Eclipse has revealed that the issue remains unpatched, allowing attackers to exploit it and gain SYSTEM privileges. Chaotic Eclipse has released a proof-of-concept (PoC) for the vulnerability, which has been shown to work reliably on Windows 11 systems running the latest May 2026 updates. The PoC can spawn a SYSTEM shell, although the success rate may vary due to the nature of the vulnerability being a race condition.

The MiniPlasma vulnerability is likely to affect all Windows versions, making it a significant concern for system administrators and security professionals. The fact that Microsoft had previously addressed a similar privilege escalation flaw in the same component in December 2025, which was identified as being exploited by unknown threat actors, highlights the importance of prompt patching and ongoing vulnerability management. Security researcher Will Dormann has confirmed that the MiniPlasma exploit works reliably on Windows 11 systems, but noted that it does not seem to work on the latest Insider Preview Canary Windows 11.

The release of the MiniPlasma PoC serves as a reminder of the ongoing need for vigilance in maintaining system security and the importance of keeping systems up to date with the latest patches and security updates. As the vulnerability is still present in fully patched Windows systems, it is essential for organizations to be aware of the potential risks and take steps to mitigate them. This may include implementing additional security controls, such as privilege restriction and monitoring for suspicious activity, to reduce the potential impact of the vulnerability.

---

> *In separateness lies the world's great misery, in compassion lies the world's true strength.
Author: Buddha*

Source: [MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)
