---
title: "Record Microsoft Patch Tuesday, fresh zero-day"
date: 2026-06-10T10:56:37+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft has released its largest-ever Patch Tuesday, addressing nearly 200 vulnerabilities in its products. The updates include fixes for several high-priority issues, such as an actively exploited Microsoft Exchange Server vulnerability (CVE-2026-42897) and a privilege escalation vulnerability in Windows Collaborative Translation Framework (CVE-2026-45586). Additionally, a new zero-day exploit called "RoguePlanet" was released, which abuses a race condition in Windows Defender to spawn a command shell with SYSTEM-level privileges.

The Patch Tuesday releases also include fixes for other notable vulnerabilities, such as a remotely exploitable vulnerability in HTTP.sys (CVE-2026-49160) and two Windows BitLocker bypasses (CVE-2026-50507 and CVE-2026-45585). Researchers have highlighted the importance of prioritizing these patches, particularly in the age of AI-powered security research. Dustin Childs, head of threat awareness at Trend Micro's Zero Day Initiative, noted that systems using the default MaxRequestBytes registry value are not affected by the HTTP.sys flaw, but advised editing registry settings for protection.

The increasing volume of patches is attributed to the growing use of AI in security research, which is expected to continue. Satnam Narang, senior staff research engineer at Tenable, noted that AI models can produce proof-of-concept exploits by analyzing patch diffs, making it essential for organizations to rapidly close the patch gap. The use of AI in security research also raises concerns about the quality of patches and the need for sysadmins to adjust their prioritization and deployment processes. As the volume of patches continues to grow, it is crucial for organizations to stay vigilant and prioritize the most critical updates to ensure their systems remain secure.

---

> *Keep your eyes on the stars and your feet on the ground.
Author: Theodore Roosevelt*

Source: [Record Microsoft Patch Tuesday, fresh zero-day](https://www.helpnetsecurity.com/2026/06/10/microsoft-patch-tuesday-rogueplanet/)
