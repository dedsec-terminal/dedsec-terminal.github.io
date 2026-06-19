---
title: "F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution"
date: 2026-06-18T17:32:14+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

F5 has released security updates to address two critical security flaws in NGINX Open Source, which could be exploited to achieve remote code execution on affected systems. The vulnerabilities, identified as CVE-2026-42530 and CVE-2026-42055, have CVSS v4 scores of 9.2, indicating a high level of severity. These flaws can be triggered by remote unauthenticated attackers, allowing them to execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

The first vulnerability, CVE-2026-42530, is a use-after-free vulnerability in the ngx_http_v3_module, which can be triggered when NGINX Open Source is configured to use the HTTP/3 QUIC module. The second vulnerability, CVE-2026-42055, is a heap-based buffer overflow vulnerability in the ngx_http_proxy_v2_module and ngx_http_grpc_module modules, which can be triggered when proxying HTTP/2 traffic with specific configuration settings. F5 has patched these vulnerabilities in various versions of NGINX Open Source, NGINX Plus, and other related products.

As mitigations, F5 recommends disabling HTTP/3 for CVE-2026-42530 and removing the ignore_invalid_headers off directive or reducing the large_client_header_buffers directive size for CVE-2026-42055. Although F5 has not reported any active exploitation of these vulnerabilities, the company's products have been targeted by attackers in the past. Recently, another critical security defect in NGINX Plus and NGINX Open Source was exploited in the wild, highlighting the importance of applying security updates and following mitigation guidelines to protect against potential attacks.

---

> *Action may not always bring happiness; but there is no happiness without action.
Author: Benjamin Disraeli*

Source: [F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html)
