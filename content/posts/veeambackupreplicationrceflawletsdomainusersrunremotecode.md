---
title: "Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code"
date: 2026-06-09T16:39:47+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Veeam has released security patches to address a critical flaw in its Backup & Replication software, tracked as CVE-2026-44963, with a CVSS score of 9.4 out of 10.0. This vulnerability allows remote code execution (RCE) on the Backup Server by an authenticated domain user, posing a significant security risk.

The vulnerability affects Veeam Backup & Replication version 12.3.2.4465 and all earlier versions of 12 builds. However, it does not impact version 13.x builds due to architectural changes introduced in version 13. The issue was discovered and reported by watchTowr researcher Sina Kheirkhah, and Veeam has credited him for his responsible disclosure.

To address the vulnerability, Veeam has released an updated version, 12.3.2.4854, which users are advised to install for optimal security. This is particularly important given that prior vulnerabilities in the software have been exploited by malicious actors, including ransomware groups. Users are urged to update to the latest version to prevent potential remote code execution attacks.

---

> *One who asks a question is a fool for five minutes; one who does not ask a question remains a fool forever.*

Source: [Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html)
