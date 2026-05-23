---
title: "Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws"
date: 2026-05-18T10:54:05+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Ivanti, Fortinet, SAP, VMware, and n8n have recently released security patches to address various vulnerabilities that could be exploited by malicious actors to bypass authentication, execute arbitrary code, and gain unauthorized access. One critical flaw, affecting Ivanti Xtraction, could allow a remote authenticated attacker to read sensitive files and write arbitrary HTML files to a web directory, leading to information disclosure and possible client-side attacks. This vulnerability has a CVSS score of 9.6, indicating a high level of severity.

Fortinet has also published advisories for two critical vulnerabilities affecting FortiAuthenticator and FortiSandbox, which could result in code execution. These vulnerabilities, with CVSS scores of 9.1, may allow an unauthenticated attacker to execute unauthorized code or commands via crafted requests. SAP has shipped fixes for two critical vulnerabilities, including an SQL injection vulnerability in SAP S/4HANA and a missing authentication check in the SAP Commerce cloud configuration. These vulnerabilities have CVSS scores of 9.6, highlighting their critical nature.

In addition to these vulnerabilities, VMware has released a patch for a high-severity flaw in VMware Fusion that could allow local privilege escalation. This issue, with a CVSS score of 7.8, has been addressed in version 26H1. n8n has also released patches for five critical vulnerabilities, including a vulnerability in the xml2js library used to parse XML request bodies in n8n's webhook handler. These vulnerabilities, with CVSS scores of 9.4, could allow an authenticated user to achieve remote code execution on the n8n host.

Other vendors, including ABB, Adobe, Amazon Web Services, and Apple, have also released security updates to rectify various vulnerabilities over the past several weeks. These updates demonstrate the ongoing efforts of vendors to address security concerns and protect their users from potential threats. It is essential for users to apply these patches and updates to ensure the security and integrity of their systems. By doing so, they can mitigate the risks associated with these vulnerabilities and prevent malicious actors from exploiting them.

---

> *To accomplish great things, we must dream as well as act.
Author: Anatole France*

Source: [Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws](https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
