---
title: "Max severity Cisco Secure Workload flaw gives Site Admin privileges"
date: 2026-05-21T13:58:33+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cisco has released security updates to address a maximum-severity Secure Workload vulnerability that allows attackers to gain Site Admin privileges.
Formerly known as Cisco Tetration, Cisco Secure Workload helps admins reduce their network's attack surface through zero trust microsegmentation and stop lateral movement to keep business applications safe.
Tracked as CVE-2026-20223, the security flaw was found in Secure Workload's internal REST APIs, and it enables unauthenticated attackers to access resources with the privileges of the Site Admin role.
"This vulnerability is due to insufficient validation and authentication when accessing REST API endpoints. An attacker could exploit this vulnerability if they are able to send a crafted API request to an affected endpoint," Cisco explained in a Wednesday advisory.
"A successful exploit could allow the attacker to read sensitive information and make configuration changes across tenant boundaries with the privileges of the Site Admin user.

---

> *It is not enough to have a good mind; the main thing is to use it well.
Author: Rene Descartes*

Source: [Max severity Cisco Secure Workload flaw gives Site Admin privileges](https://www.bleepingcomputer.com/news/security/cisco-max-severity-secure-workload-flaw-gives-hackers-site-admin-privileges/)
