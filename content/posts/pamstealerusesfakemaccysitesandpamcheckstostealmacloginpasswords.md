---
title: "PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords"
date: 2026-07-03T08:03:37+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers at Jamf Threat Labs have discovered a new macOS information stealer called PamStealer. This malware is distributed as a compiled AppleScript (.scpt) file that impersonates Maccy, a legitimate open-source clipboard manager. The script is designed to download and stage a follow-on payload, a Rust-based infostealer capable of credential theft, browser data collection, persistence, and exfiltration.

The malware is delivered in two stages, with the initial access vector being a fake website ("maccyapp[.]com") that mimics the legitimate Maccy website ("maccy[.]app"). The AppleScript executes a self-contained JavaScript for Automation (JXA) downloader that fetches and stages the stealer payload using native Objective-C APIs. The script also incorporates environment-aware features that allow it to execute only on Apple Silicon-based Macs and avoids execution within sandboxed or analysis environments.

Once the malware is executed, it captures the victim's system password by serving a native password prompt and validating the entered password via the macOS Pluggable Authentication Modules (PAM) API. The captured information is then encrypted and exfiltrated to attacker-controlled infrastructure. The developer of Maccy has warned users to stay away from fake websites mimicking the tool, and the discovery of PamStealer highlights the evolving nature of commodity macOS stealers, which are adopting quieter execution chains and native implementations to reduce detection opportunities.

---

> *The wise man does not lay up his own treasures. The more he gives to others, the more he has for his own.
Author: Lao Tzu*

Source: [PamStealer Uses Fake Maccy Sites and PAM Checks to Steal Mac Login Passwords](https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html)
