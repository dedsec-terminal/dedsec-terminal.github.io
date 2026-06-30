---
title: "Factoring RSA Keys with Many Zeros"
date: 2026-06-29T16:05:18+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers have discovered a new class of weak RSA keys that contain many zeros, which can be factored more easily. These keys have been found in the wild, including in Certificate Transparency logs, internet-wide TLS and SSH scans, and PGP keys. The researchers used the open-source Badkeys project to collect and analyze a large dataset of real-world keys, where they identified two patterns of weak keys with regularly spaced blocks of zeros.

The first pattern was found in certificates issued to large organizations such as Yahoo and Verizon, as well as on devices running NetApp software. Fortunately, these certificates have already expired. The second pattern was found on SSH hosts running the CompleteFTP software from EnterpriseDT, which affects RSA keys generated between December 2016 and March 2019, and DSA keys generated between December 2016 and December 2023. The researchers notified the affected companies but did not receive a response.

The discovery of these weak keys raises concerns about the security of RSA implementations and the potential for deliberate backdoors. The fact that independent cryptographic implementations failed in similar ways suggests that more implementations may be vulnerable to the same type of attack. This has led to speculation about the possibility of government agencies exploiting this vulnerability to break certain classes of RSA keys. The incident highlights the importance of proper cryptographic implementation and the need for ongoing monitoring and analysis of public keys to identify potential security risks.

---

> *By letting it go it all gets done. The world is won by those who let it go. But when you try and try. The world is beyond the winning.
Author: Lao Tzu*

Source: [Factoring RSA Keys with Many Zeros](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html)
