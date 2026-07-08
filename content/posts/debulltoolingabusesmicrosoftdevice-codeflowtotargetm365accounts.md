---
title: "DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts"
date: 2026-07-07T15:14:14+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A recent Microsoft 365 device code phishing campaign has been observed, leveraging collaboration-themed lures to target victim accounts. The campaign uses a malicious collaboration-style lure to push users into the legitimate Microsoft device login experience, while a backend broker generates and polls Microsoft Authentication Broker device-code tokens. This technique, known as device code phishing, exploits a legitimate OAuth 2.0 authentication mechanism to bypass multi-factor authentication (MFA) and gain persistent account access without stealing user passwords.

The campaign is assessed to share strong overlaps with a previous campaign documented by Microsoft in February 2025, known as Storm-2372. However, the threat actors are now employing Storm-2372-style tradecraft through a reusable tooling layer called DEBULL. DEBULL is a phishing-as-a-service (PhaaS) platform that uses GraphSpy or a GraphSpy-derived workflow for Microsoft 365 and Entra post-exploitation. The platform allows operators to define a page name and slug, edit HTML, CSS, and JavaScript, and choose how the lure is published, making it a flexible and reusable tool for phishing attacks.

The discovery of DEBULL and other PhaaS platforms like ARToken and EvilTokens highlights the growing threat of device code phishing attacks. These platforms enable attackers to weaponize harvested tokens to exfiltrate emails, files, and other sensitive data from compromised Microsoft accounts, carry out reconnaissance, and establish persistence access. The surge in device code phishing attacks has led to a broader shift within the threat landscape, with other PhaaS kits adopting the technique to hijack Microsoft 365 accounts. As a result, it is essential for organizations to be aware of these threats and take measures to protect their Microsoft 365 accounts and sensitive data.

---

> *All children are artists. The problem is how to remain an artist once he grows up.
Author: Pablo Picasso*

Source: [DEBULL Tooling Abuses Microsoft Device-Code Flow to Target M365 Accounts](https://thehackernews.com/2026/07/debull-tooling-abuses-microsoft-device.html)
