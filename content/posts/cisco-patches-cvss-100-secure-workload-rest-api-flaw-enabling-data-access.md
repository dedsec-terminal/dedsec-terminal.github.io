---
title: "Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Enabling Data Access"
date: 2026-05-22T05:36:18+00:00
draft: false
categories:
  - cves
---

**Cisco Patches Critical Security Flaw in Secure Workload**

Cisco has released updates to fix a maximum-severity security vulnerability (CVE-2026-20223, CVSS score: 10.0) in its Secure Workload product. The flaw, which affects both SaaS and on-prem deployments, allows an unauthenticated, remote attacker to access sensitive data by sending a crafted API request. A successful exploit could enable the attacker to read sensitive information and make configuration changes with the privileges of the Site Admin user.

**Key Points:**

* The vulnerability is due to insufficient validation and authentication in REST API endpoints.
* There are no workarounds to address the issue.
* The flaw affects Cisco Secure Workload Cluster Software, regardless of device configuration.
* Cisco has released fixed versions: 3.10.8.3, 4.0.3.17, and recommends migrating from Release 3.9 and earlier.
* The vulnerability was discovered during internal security testing, and there is no evidence of it being exploited in the wild.

**Context:**

This disclosure comes a week after Cisco revealed another maximum-severity authentication bypass flaw (CVE-2026-20182) in its Catalyst SD-WAN Controller, which has been exploited by a threat actor. Users are advised to update their Secure Workload software to the latest fixed versions to prevent potential attacks.

---

> *The greatest way to live with honour in this world is to be what we pretend to be.
Author: Socrates*

Source: [Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Enabling Data Access](https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html)
