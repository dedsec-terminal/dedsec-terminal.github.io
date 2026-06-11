---
title: "Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs"
date: 2026-06-10T09:38:13+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Microsoft has released a record 206 security patches to address vulnerabilities in its software portfolio, including three zero-day flaws that were publicly disclosed at the time of release. The patches include fixes for 39 critical and 167 important vulnerabilities, with the most severe being a use-after-free flaw in the Windows Kernel that could allow remote code execution. Other notable vulnerabilities include integer overflow and stack-based buffer overflow flaws in Windows HTTP.sys and DHCP Client, which could also allow unauthorized code execution over a network.

The patches also address several security feature bypass vulnerabilities, including a Windows BitLocker vulnerability for which a proof-of-concept exploit was released last month. Additionally, Microsoft has fixed several publicly disclosed zero-day vulnerabilities, including a privilege escalation vulnerability in the Windows Collaborative Translation Framework and a denial-of-service vulnerability in HTTP.sys. The company has also introduced a new registry setting to limit the number of headers in HTTP/2 and HTTP/3 requests, which can help protect systems from excessive memory use and denial-of-service attacks.

The large number of patches is attributed to the increasing use of artificial intelligence (AI)-assisted vulnerability discovery approaches, which is expected to continue in the future. Security experts have noted that the number of vulnerabilities being discovered is increasing at an unprecedented scale, with the current number of CVEs shipped by Microsoft this year exceeding the total number of CVEs shipped in all of 2018. The patches are a testament to the importance of regular software updates and the need for organizations to prioritize vulnerability management to protect against potential security threats.

---

> *Reviewing what you have learned and learning anew, you are fit to be a teacher.
Author: Confucius*

Source: [Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)
