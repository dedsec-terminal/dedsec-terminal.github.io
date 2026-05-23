---
title: "NGINX CVE-2026-42945 Exploited in the Wild, Causing Worker Crashes and Possible RCE"
date: 2026-05-17T11:57:53+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A recently disclosed vulnerability in NGINX Plus and NGINX Open, tracked as CVE-2026-42945, has been exploited in the wild. The flaw is a heap buffer overflow in the ngx_http_rewrite_module, affecting versions 0.6.27 through 1.30.0, and was introduced in 2008. Successful exploitation can allow an unauthenticated attacker to crash worker processes or execute remote code with crafted HTTP requests, although code execution is only possible on devices with Address Space Layout Randomization (ASLR) turned off.

The vulnerability requires a specific NGINX configuration to be vulnerable, and an attacker must know or discover this configuration to exploit it. Security researchers have noted that turning the heap overflow into reliable code execution is not trivial in the default configuration, and on systems with ASLR enabled, a generic exploit is unlikely to be produced. However, the worker-crash denial-of-service (DoS) aspect of the vulnerability is still exploitable and poses a significant threat. As a result, users are advised to apply the latest fixes from F5 to secure their networks against active threats.

Threat actors have begun to weaponize the flaw, with exploitation attempts detected against honeypot networks. The nature of the attack activity and the end goals are currently unknown. Meanwhile, VulnCheck has also reported exploitation efforts targeting two critical flaws in openDCIM, an open-source application used for data center infrastructure management. The vulnerabilities, rated 9.3 on the CVSS scoring system, include a missing authorization vulnerability and an operating system command injection vulnerability, which can be chained to achieve remote code execution.

The exploitation of these vulnerabilities is a concern, as they can be used to gain unauthorized access to systems and execute arbitrary code. The cluster of attacker activity observed so far originates from a single Chinese IP and uses a customized implementation of an AI-powered vulnerability discovery tool to automatically check for vulnerable installations before dropping a PHP web shell. Users of NGINX and openDCIM are urged to take immediate action to patch their systems and prevent potential attacks.

The active exploitation of these vulnerabilities highlights the importance of keeping software up to date and applying security patches in a timely manner. Users should prioritize applying the latest fixes from F5 and openDCIM to secure their networks against these threats. Additionally, implementing security measures such as ASLR and monitoring for suspicious activity can help prevent and detect potential attacks.

---

> *Victory belongs to the most persevering.
Author: Napoleon Bonaparte*

Source: [NGINX CVE-2026-42945 Exploited in the Wild, Causing Worker Crashes and Possible RCE](https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html)
