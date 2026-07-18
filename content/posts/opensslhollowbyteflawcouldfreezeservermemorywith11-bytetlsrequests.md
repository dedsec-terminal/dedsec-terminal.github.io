---
title: "OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests"
date: 2026-07-17T20:20:53+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the OpenSSL HollowByte flaw in three concise paragraphs:

A recently discovered flaw in OpenSSL, dubbed HollowByte, allows an attacker to freeze up to 131 KB of server memory with just an 11-byte TLS request. This denial-of-service bug occurs because OpenSSL allocates memory based on the declared size of the TLS handshake message, even if the message body never arrives. On systems using glibc, this allocated memory is not released back to the kernel, leading to memory fragmentation and potential connection exhaustion attacks.

The HollowByte flaw was fixed by OpenSSL in June, but the fix was not accompanied by a CVE, advisory, or changelog entry. The fixed releases are OpenSSL 4.0.1, 3.6.3, 3.5.7, 3.4.6, and 3.0.21. Okta's Red Team, which reported the bug, found that the flaw can be exploited to lock up significant amounts of system memory, with tests showing that a 1 GB server can be OOM-killed with 547 MB of memory frozen in fragments. The attack can vary the claimed size on every connection, making it difficult for the allocator to reuse freed memory.

OpenSSL's decision not to classify the HollowByte flaw as a vulnerability has raised questions, as it meets the criteria for a Low-severity issue. The project's security policy defines four severity tiers, but the HollowByte fix was handled as a "bug or hardening" fix, which does not earn a CVE or advisory. The Hacker News has asked OpenSSL for clarification on this decision and whether the fix will be applied to other branches. Additionally, the DTLS path in OpenSSL remains vulnerable to the HollowByte flaw, and it is unclear whether the project plans to address this issue.

---

> *Don't let today's disappointments cast a shadow on tomorrow's dreams.*

Source: [OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests](https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html)
