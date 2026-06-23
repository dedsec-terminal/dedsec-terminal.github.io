---
title: "29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests"
date: 2026-06-22T14:29:46+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A 29-year-old bug, dubbed "Squidbleed" (CVE-2026-47729), has been discovered in the Squid web proxy. The bug is a heap over-read that can leak another user's cleartext HTTP request, including credentials or session tokens, to anyone allowed to send traffic through the same proxy. This bug is particularly concerning in shared networks such as schools, offices, and public Wi-Fi, where an attacker can be another user of the same proxy.

The bug is located in Squid's FTP directory-listing parser, which was introduced in 1997. An attacker can exploit this bug by sending a specially crafted FTP listing line that causes the parser to walk off the end of the buffer, revealing sensitive information. The leaked bytes can include a victim's HTTP request, which can be used to act as that user. A proof-of-concept code is public, but no in-the-wild exploitation has been reported.

To mitigate this bug, users can either patch their Squid version or disable FTP altogether. The fix is a small null-terminator check that has been merged to the development branch. Disabling FTP is a recommended solution, as it removes the attack surface and is a relatively simple step. The risk associated with this bug is moderate, with a CVSS score of 6.5, and is bounded by the need for an attacker to have proxy access and the limited impact on confidentiality.

---

> *If you light a lamp for somebody, it will also brighten your path.
Author: Buddha*

Source: [29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests](https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html)
