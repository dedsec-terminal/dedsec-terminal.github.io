---
title: "GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft"
date: 2026-07-17T16:39:16+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Cybersecurity researchers have attributed the April 2026 DigiCert security incident to a threat activity cluster known as CylindricalCanine, a sub-group of the Chinese cybercrime group GoldenEyeDog. GoldenEyeDog is known for targeting the gambling and gaming sectors using malware-laced software and has been active since at least 2015. The group used their malware to access a DigiCert support member's device and steal code-signing certificates intended for DigiCert customers.

The threat actor's operations center around a modified version of the Gh0st RAT (Remote Access Trojan) malware, referred to as Golden Gh0st RAT, which is delivered through a multi-stage loader. The malware is used to target finance organizations in the Asia-Pacific region and has been linked to previous campaigns targeting customer support staff at Web3 companies. CylindricalCanine has been observed abusing code-signing certificates, using them to sign their own malware and avoid detection.

The DigiCert compromise occurred when a threat actor contacted the company's support team via a customer chat channel and delivered a malicious payload. The actor was able to access initialization codes for code-signing certificate orders and obtain 60 certificates, 27 of which were linked to the threat actor. The stolen certificates were used to sign Zhong Stealer malware artifacts. DigiCert has since revoked the certificates and deployed a code change to mask initialization codes from compromised analyst accounts. The incident highlights the capabilities of the GoldenEyeDog group and the importance of securing code-signing certificates.

---

> *We can only be said to be alive in those moments when our hearts are conscious of our treasures.
Author: Thornton Wilder*

Source: [GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft](https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html)
