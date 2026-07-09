---
title: "Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS"
date: 2026-07-08T14:38:05+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Ubiquiti has released updates to address multiple critical security flaws in its UniFi product line, including UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS. The vulnerabilities, which have CVSS scores ranging from 9.0 to 10.0, could allow attackers to escalate privileges, execute arbitrary commands, and make unauthorized changes to devices. The flaws can be exploited by attackers with access to the network, and some require low privileges to execute.

The list of vulnerabilities includes improper access control, SQL injection, and input validation flaws, as well as a Server-Side Request Forgery (SSRF) vulnerability. The affected versions of the software range from 3.4.16 to 7.1.77, and the updates fix these vulnerabilities in versions 3.4.20, 5.2.2, 4.2.29, 7.1.83, and 5.1.19. While there is no evidence that these specific flaws have been exploited in the wild, a set of three vulnerabilities in UniFi OS was previously flagged by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) as having been used in real-world attacks.

The updates are critical, given the potential for attackers to exploit these vulnerabilities to gain control of devices and networks. Additionally, Russian state-sponsored threat actors have been observed compromising Ubiquiti Edge OS routers and using them to proxy malicious traffic as part of a botnet called MooBot. The botnet was dismantled in a law enforcement operation in February 2024, but the incident highlights the importance of keeping Ubiquiti devices and software up to date to prevent similar attacks. Users are advised to apply the updates as soon as possible to protect their devices and networks from potential exploitation.

---

> *Action may not always bring happiness; but there is no happiness without action.
Author: Benjamin Disraeli*

Source: [Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS](https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html)
