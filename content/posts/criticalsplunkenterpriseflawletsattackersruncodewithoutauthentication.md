---
title: "Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication"
date: 2026-06-13T13:23:03+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

**Critical Splunk Enterprise Flaw Discovered**
A critical security flaw has been identified in Splunk Enterprise, allowing attackers to conduct unauthenticated file operations and potentially achieve remote code execution. The vulnerability, tracked as CVE-2026-20253, is rated 9.8 on the CVSS scoring system and affects Splunk Enterprise versions below 10.2.4 and 10.0.7. This flaw exists due to the lack of authentication controls in the PostgreSQL sidecar service endpoint, enabling any network-reachable user to invoke file operations without credentials.

**Exploitation and Impact**
The vulnerability can be exploited to achieve pre-authenticated remote code execution on susceptible systems through specific endpoints. Attackers can connect to an attacker-controlled database, dump its contents into an arbitrary file, and load the dump into the local PostgreSQL instance. By defining a new function that uses lo_export, attackers can write controlled content to a file, which can be executed during the restoration process. This can lead to arbitrary file write and remote code execution, allowing attackers to overwrite Python scripts and include malicious payloads.

**Mitigation and Recommendations**
Splunk has released security updates to address the vulnerability, and users are advised to apply the fixes to stay protected. The issue has been addressed in Splunk Enterprise versions 10.0.7 and 10.2.4. Splunk Cloud is not impacted by the vulnerability. Although there is no evidence of the flaw being exploited in the wild, the availability of exploit specifics can drive threat actors to trigger opportunistic attempts. Therefore, it is essential for users to move quickly and apply the fixes to prevent potential attacks and ensure the security of their systems.

---

> *To fly as fast as thought, you must begin by knowing that you have already arrived.
Author: Richard Bach*

Source: [Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication](https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html)
