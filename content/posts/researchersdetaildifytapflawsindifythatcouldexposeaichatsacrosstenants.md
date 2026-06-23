---
title: "Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants"
date: 2026-06-22T16:13:28+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers at Zafran Security have discovered four vulnerabilities in Dify, an open-source agentic workflow platform, which could allow attackers to read artificial intelligence (AI) conversations from other customers' applications without authentication. The vulnerabilities, collectively codenamed DifyTap, include two critical severity flaws and three cross-tenant impact issues, allowing one customer's data to be exposed to another. This could create a covert exfiltration channel for every message and model response.

The vulnerabilities allow attackers to traverse Dify's internal Plugin Daemon API, trigger cross-tenant internal API calls, and preview documents uploaded by other tenants. They also enable attackers to leak files across users within a tenant by attaching another user's file unique identifier. Additionally, Zafran discovered that Dify's file parsing stack relied on a vulnerable version of PDFium, which could allow a remote attacker to exploit heap corruption via a crafted PDF file. The vulnerabilities have been assigned CVE numbers, including CVE-2026-41947, CVE-2026-41948, CVE-2026-41949, and CVE-2026-41950.

Following responsible disclosure, all vulnerabilities except CVE-2026-41948 have been addressed in version 1.14.2 of Dify, which was released last month. A fix for the pending flaw is expected to be made available in the next release of Dify. The discovery of DifyTap highlights the challenge of vulnerability visibility, particularly in container images, where differences between deployments can create visibility gaps that traditional scanners cannot detect. The researchers note that anyone can freely register for a Dify account, making it possible for attackers to configure their own tracing for any application they can access as a client.

---

> *The reason most goals are not achieved is that we spend our time doing second things first.
Author: Robert McKain*

Source: [Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants](https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html)
