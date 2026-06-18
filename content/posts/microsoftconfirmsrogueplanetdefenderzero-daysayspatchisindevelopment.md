---
title: "Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development"
date: 2026-06-17T17:36:28+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft has confirmed the existence of a zero-day vulnerability in its Defender software, codenamed RoguePlanet. The vulnerability, assigned the CVE identifier CVE-2026-50656 with a CVSS score of 7.8, is a privilege escalation flaw in the Microsoft Malware Protection Engine. This allows attackers to potentially gain SYSTEM-level privileges.

The vulnerability was first disclosed by security researcher Chaotic Eclipse, who released a proof-of-concept (PoC) exploit that takes advantage of a race condition to grant attackers a shell with elevated privileges. The researcher noted that the exploit has a varying success rate, with some machines being more vulnerable than others. Additionally, the PoC was found to work even when real-time protection is enabled, which was unexpected.

Microsoft is currently working on a patch to address the RoguePlanet vulnerability and has stated that it is committed to providing a high-quality security update. This is the fourth Defender vulnerability disclosed by Chaotic Eclipse, following BlueHammer, UnDefend, and RedSun, all of which have been patched by Microsoft. The company is actively investigating the issue and will release a patch to protect users from potential attacks exploiting the RoguePlanet vulnerability.

---

> *From error to error one discovers the entire truth.
Author: Sigmund Freud*

Source: [Microsoft Confirms RoguePlanet Defender Zero-Day, Says Patch is in Development](https://thehackernews.com/2026/06/microsoft-confirms-rogueplanet-defender_02022423645.html)
