---
title: "SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data"
date: 2026-07-14T18:17:57+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

SAP has released security updates to address multiple vulnerabilities, including a critical flaw in SAP NetWeaver Application Server ABAP. The vulnerability, CVE-2026-44747, has a CVSS score of 9.9 and allows an authenticated attacker to exploit logical errors in memory management, potentially leading to unauthorized data access, modification, or system unavailability. As a temporary workaround, SAP recommends disabling specific ICF nodes, but installing the patched ABAP Kernel version is strongly advised.

In addition to the NetWeaver ABAP flaw, SAP has also addressed two other critical vulnerabilities. CVE-2026-27690 has a CVSS score of 9.1 and affects SAP Approuter deployments, allowing an unauthenticated attacker to send specially crafted HTTP requests that can lead to request-response desynchronization and expose user responses. CVE-2026-44761, also with a CVSS score of 9.1, is a use of default credentials flaw in SAP Commerce Cloud that can allow an unauthenticated attacker to obtain a valid access token and invoke certain APIs to read and modify data.

The vulnerabilities can have a significant impact on confidentiality and integrity, and it is recommended that customers apply the necessary updates for optimal protection. Although there is no evidence of the flaws being exploited in the wild, it is crucial to audit production environments for the presence of affected sample OAuth 2.0 clients and remove or replace them with strong, unique values. By installing the patched ABAP Kernel version and addressing the other vulnerabilities, customers can ensure the security and integrity of their SAP systems.

---

> *Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared.
Author: Buddha*

Source: [SAP Patches CVSS 9.9 NetWeaver ABAP Flaw That Could Expose or Modify Data](https://thehackernews.com/2026/07/sap-patches-cvss-99-netweaver-abap-flaw.html)
