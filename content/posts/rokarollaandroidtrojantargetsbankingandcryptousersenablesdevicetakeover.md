---
title: "Rokarolla Android trojan targets banking and crypto users, enables device takeover"
date: 2026-06-17T13:23:46+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A newly discovered Android banking trojan, dubbed Rokarolla, has been found to target 217 banking and cryptocurrency applications. The malware is primarily distributed through malicious websites that impersonate popular apps such as TikTok and Google Chrome, tricking users into downloading what appears to be a legitimate app. Once installed, Rokarolla requests access to Android Accessibility Services and other permissions, allowing it to steal financial information and gain broad control over compromised devices.

Rokarolla's malicious capabilities include harvesting lock screen credentials, exfiltrating sensitive contact lists and SMS data, and utilizing keyloggers to record user input. The malware also conceals its operations and disrupts user intervention by blocking incoming calls, deploying fraudulent screen overlays, and suppressing device audio. The attack begins with a dropper that poses as Google Play Protect, which delivers a second-stage payload containing the Rokarolla malware. The malware then checks infected devices for target applications and downloads phishing pages to steal financial data.

The malware can receive 137 commands from its operators, allowing for extensive control over infected devices. Rokarolla's capabilities include SMS interception, device surveillance, and the ability to extract text from screens and messaging applications. The malware can also modify clipboard contents, block and intercept phone calls, and mute device audio and vibrations. Zimperium has published a list of indicators of compromise (IoCs) and MITRE ATT&CK tactics and techniques associated with the Rokarolla attack chain to help users and organizations detect and prevent the malware.

---

> *He who knows, does not speak. He who speaks, does not know.
Author: Lao Tzu*

Source: [Rokarolla Android trojan targets banking and crypto users, enables device takeover](https://www.helpnetsecurity.com/2026/06/17/rokarolla-android-banking-trojan-device-takeover/)
