---
title: "ZDI-26-295: (0Day) PublicCMS getXml Server-Side Request Forgery Information Disclosure Vulnerability"
date: 2026-04-21T05:00:00+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A recently discovered vulnerability in PublicCMS, identified as ZDI-26-295, allows remote attackers to disclose sensitive information without requiring authentication. The flaw exists within the getXml method, where a lack of authorization enables unauthorized access to functionality. This vulnerability can be exploited by attackers to obtain information within the context of the application, posing a significant security risk.

The vulnerability was first reported to the vendor by the Zero Day Initiative (ZDI) on April 26, 2024. Following this initial report, ZDI sent subsequent requests for updates on August 21, 2024, and November 10, 2025. After receiving no resolution, ZDI notified the vendor of their intention to publish the case as a 0-day advisory on April 17, 2026. This decision was made due to the prolonged lack of response and the potential risks associated with the vulnerability.

Given the nature of this vulnerability, the most effective mitigation strategy is to restrict interaction with the affected product. This can help prevent remote attackers from exploiting the vulnerability and disclosing sensitive information. It is essential for users and administrators to be aware of this vulnerability and take necessary precautions to minimize potential risks. By limiting access to the product, users can reduce the likelihood of exploitation and protect sensitive information.

The fact that this vulnerability can be exploited without authentication makes it particularly concerning, as it can be leveraged by attackers without requiring any prior access or credentials. As a result, it is crucial for the vendor to release a patch or update to address this issue and prevent potential exploits. Until a fix is available, users must rely on mitigation strategies to protect themselves from the risks associated with this vulnerability.

---

> *Bodily exercise, when compulsory, does no harm to the body; but knowledge which is acquired under compulsion obtains no hold on the mind.
Author: Plato*

Source: [ZDI-26-295: (0Day) PublicCMS getXml Server-Side Request Forgery Information Disclosure Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-295/)
