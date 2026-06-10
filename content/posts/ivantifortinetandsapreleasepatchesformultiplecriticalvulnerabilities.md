---
title: "Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities"
date: 2026-06-10T15:10:59+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Fortinet, Ivanti, and SAP have released security patches to address multiple critical vulnerabilities that could lead to arbitrary code execution and information disclosure. Fortinet's patch fixes a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI, tracked as CVE-2026-25089 with a CVSS score of 9.1. This vulnerability allows an unauthenticated attacker to execute unauthorized commands via specifically crafted HTTP requests.

Ivanti has published fixes for two critical security flaws impacting Ivanti Sentry, formerly MobileIron Sentry. The first flaw, CVE-2026-10520, is an operating system command injection vulnerability that allows a remote unauthenticated user to achieve root-level remote code execution. The second flaw, CVE-2026-10523, is an authentication bypass vulnerability that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access. Ivanti's patch incorporates additional controls to block access to the vulnerable endpoint and adds a layer of protection to make reaching the endpoint more difficult.

SAP has also released fixes for four critical vulnerabilities in NetWeaver AS ABAP and ABAP Platform, as well as SAP Commerce Cloud and SAP Data Hub. These vulnerabilities include an XML signature wrapping vulnerability, a memory corruption vulnerability, a potential Spring security vulnerability, and a directory traversal vulnerability. While there is no evidence that any of these flaws have been exploited in the wild, it is recommended to update to the latest version for optimal protection. Users are advised to upgrade to the patched versions to prevent potential attacks and ensure the security of their systems.

---

> *What matters is the value we've created in our lives, the people we've made happy and how much we've grown as people.
Author: Daisaku Ikeda*

Source: [Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities](https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html)
