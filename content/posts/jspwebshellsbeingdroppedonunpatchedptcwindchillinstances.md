---
title: "JSP webshells being dropped on unpatched PTC Windchill instances"
date: 2026-06-29T16:18:49+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

The US Cybersecurity and Infrastructure Security Agency (CISA) has added a vulnerability (CVE-2026-12569) in PTC's Windchill and FlexPLM software platforms to its Known Exploited Vulnerabilities (KEV) catalog. This vulnerability allows unauthenticated, remote attackers to execute arbitrary code by sending a malicious request to the network. As a result, attackers are dropping JSP webshells on unpatched systems, prompting CISA to order US federal civilian government agencies to address the issue by June 28.

PTC Windchill is a product lifecycle management platform for manufacturing and engineering-intensive industries, while FlexPLM is used in the retail, footwear, apparel, and consumer goods industries. The vulnerability, an improper input validation flaw, was first warned about by PTC on June 17, with a patch released the following day. However, it appears that attackers are actively exploiting the vulnerability, with PTC's advisory being updated with indicators of compromise and advice for defenders.

All organizations using Windchill or FlexPLM are advised to patch the vulnerability and check for indicators of compromise. This is not the first time these platforms have been targeted, with a similar code injection vulnerability (CVE-2026-4681) being publicly disclosed in late March 2026. German authorities had warned companies of impending cyberattacks on vulnerable Windchill instances around June 17, highlighting the need for prompt action to address the vulnerability and prevent potential attacks.

---

> *Yesterday I dared to struggle. Today I dare to win.
Author: Bernadette Devlin*

Source: [JSP webshells being dropped on unpatched PTC Windchill instances](https://www.helpnetsecurity.com/2026/06/29/ptc-windchill-cve-2026-12569-exploited/)
