---
title: "Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack"
date: 2026-07-14T20:25:47+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Microsoft has released its largest Patch Tuesday update to date, addressing 622 vulnerabilities, including two zero-day flaws that are being actively exploited. The two zero-day vulnerabilities, CVE-2026-56164 and CVE-2026-56155, are elevation-of-privilege flaws in SharePoint Server and Active Directory Federation Services, respectively. These vulnerabilities allow attackers to escalate privileges, with CVE-2026-56164 enabling unauthenticated attackers to escalate privileges over the network, while CVE-2026-56155 allows already-authenticated attackers to elevate privileges locally.

In addition to the two zero-day vulnerabilities, the update also addresses a third zero-day vulnerability, CVE-2026-50661, which is a BitLocker bypass that requires physical access to the device. The update also includes a fix for a SharePoint vulnerability, CVE-2026-55040, which can be chained with a separate remote code execution bug to achieve unauthenticated RCE against a vulnerable server. Microsoft has also completed its multi-year Kerberos RC4 hardening, which may break logins for services that still rely on RC4.

The large number of vulnerabilities addressed in this update highlights the importance of prioritizing patching based on exploitation status rather than severity score. With 416 of the 622 vulnerabilities affecting Windows, and 95 remote code execution bugs across the release, the update is a significant one. Microsoft has credited its AI-powered bug detection tools, including MDASH, with helping to identify many of the vulnerabilities addressed in this update. As attackers can quickly develop exploits for newly patched vulnerabilities, it is essential for organizations to patch quickly and prioritize vulnerabilities that are being actively exploited.

---

> *Change is the law of life. And those who look only to the past or present are certain to miss the future.
Author: John Kennedy*

Source: [Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack](https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html)
