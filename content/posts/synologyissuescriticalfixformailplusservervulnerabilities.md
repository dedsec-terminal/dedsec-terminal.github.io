---
title: "Synology issues critical fix for MailPlus Server vulnerabilities"
date: 2026-06-26T10:57:37+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Synology has released a critical security update for MailPlus Server, a software package used to run private email infrastructure on Synology NAS devices. The update fixes three vulnerabilities, including faulty authorization checks, improper restriction of communication channels, and the use of a cryptographically weak pseudo-random number generator. These flaws, identified as CVE-2026-13136, CVE-2026-13135, and CVE-2025-15660, could allow remote attackers to read or write arbitrary files, access internal services, and conduct denial-of-service (DoS) attacks.

The security update is available for users running MailPlus Server on NAS devices with DiskStation Manager v7.3, 7.2.2, or 7.2.1. Users are advised to upgrade to the recently released 4.0.1-31663 version of the software, as there is no available mitigation for the fixed issues. Details about the vulnerabilities are still not publicly disclosed, but the update is considered critical to prevent potential attacks.

Over 2,100 MailPlus Server deployments are exposed to the internet, predominantly in Germany, Asia, and the US. These deployments are used by small-to-medium businesses and individuals who want to self-host their email on-premises for privacy, cost control, or compliance reasons. The vulnerabilities pose a significant risk to these users, and it is essential to apply the security update as soon as possible to prevent potential attacks and protect sensitive email infrastructure.

---

> *It is the mark of an educated mind to be able to entertain a thought without accepting it.
Author: Aristotle*

Source: [Synology issues critical fix for MailPlus Server vulnerabilities](https://www.helpnetsecurity.com/2026/06/26/synology-mailplus-server-vulnerabilities/)
