---
title: "Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures"
date: 2026-07-01T15:26:55+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

The Ousaban banking trojan, a Brazilian malware, is targeting Windows users in Spain and Portugal. The campaign, identified by Fortinet's FortiGuard Labs in May 2026, uses a phishing PDF disguised as a corrupted file to lure victims. The PDF prompts the user to press an "Update" button, which opens a malicious webpage that screens visitors to ensure they are in Spain or Portugal before downloading the malware.

Once installed, Ousaban sits quietly on the Windows PC, waiting for the user to open a banking site. When a target bank is detected, the trojan can capture screenshots and keystrokes, tamper with the clipboard, show fake messages, and provide the attacker with remote control. Ousaban targets over two dozen banks in Spain and Portugal, including major institutions such as Banco Santander and BBVA. The malware uses steganography to hide its payload inside an image and employs geofencing to only target users in the two countries.

To avoid falling victim to Ousaban, users should be cautious of phishing PDFs and emails that claim a file is corrupted and prompt them to update. Unexpected invoice or tax-document attachments should also be treated with suspicion. Defenders can block the malware by watching for specific domains, IP addresses, and file hashes, as well as monitoring for the Financeiro registry Run key and files dropped to C:\SysMain_5874288. Fortinet's FortiGuard antivirus and FortiMail product can also detect and flag the malware and phishing emails.

---

> *Let yourself be silently drawn by the stronger pull of what you really love.
Author: Rumi*

Source: [Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures](https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html)
