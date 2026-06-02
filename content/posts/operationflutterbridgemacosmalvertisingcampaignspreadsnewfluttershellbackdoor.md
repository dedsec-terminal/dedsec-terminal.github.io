---
title: "Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor"
date: 2026-06-02T10:00:31+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Operation FlutterBridge: Overview**
A widespread malvertising campaign, dubbed Operation FlutterBridge, is targeting macOS users with a new backdoor called FlutterShell. This campaign is an evolution of the previous JSCoreRunner campaign, which was first identified in August 2025. The attackers behind Operation FlutterBridge have transitioned from delivering standard adware to delivering adware with full backdoor capabilities.

**FlutterShell Malware**
FlutterShell is a macOS backdoor developed using the Flutter framework, which allows it to masquerade as legitimate software. The malware has a WebView-based architecture that utilizes a JavaScript-to-native bridge, enabling attackers to host malicious logic on an external website and dynamically alter the malware's behavior in real-time. FlutterShell has built-in commands that provide attackers with capabilities such as arbitrary command execution, file system interaction, and environment variables exfiltration.

**Deployment and Technical Analysis**
The malware is deployed through a Google Ads campaign, targeting a global audience with an emphasis on Anglophone and Western European markets. The attackers use shell companies to bypass ad-network vetting and distribute the ads. The malware is signed with valid Apple Developer IDs and has passed notarization, making it difficult to detect. Technical analysis of FlutterShell reveals a complex architecture, with the malicious logic stored on the attackers' website and triggered when the application loads the specific web content. The malware is likely under active development, with new variants and improvements being rapidly integrated into the code.

---

> *Make the best use of what is in your power, and take the rest as it happens.
Author: Epictetus*

Source: [Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/)
