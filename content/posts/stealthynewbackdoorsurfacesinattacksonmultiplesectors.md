---
title: "Stealthy new backdoor surfaces in attacks on multiple sectors"
date: 2026-06-25T14:07:46+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A new backdoor called Mistic has been discovered, targeting organizations in various sectors including insurance, education, IT, and professional services. According to Symantec, Mistic has been deployed in multiple attacks since April 2026 and is associated with Woodgnat, a financially motivated initial access broker (IAB) that has been connected to ransomware operations. Woodgnat's primary goal is to establish durable remote access within an enterprise and sell it to ransomware affiliates and other attackers.

Mistic is a stealthy backdoor that can blend in with trusted software, making it difficult to detect. It was observed being deployed alongside ModeloRAT, a Python-based remote access trojan developed by Woodgnat. The backdoor can communicate with its command-and-control infrastructure, upload and download files, execute code, and terminate itself from an infected system. Its capabilities also include creating folders, modifying files, and stealing user credentials. The fact that Mistic executes in memory and has a kill switch built-in makes it a highly stealthy and potentially long-term threat.

The attackers using Mistic and ModeloRAT also utilized several legitimate tools to carry out their attacks, including Curl, Reg.exe, and PowerShell. Symantec has published a list of indicators of compromise for Mistic, along with malicious files and IP addresses used in the recent Woodgnat attacks. The victim selection of Woodgnat is largely opportunistic, and the group's geographic location remains unknown. The discovery of Mistic highlights the need for organizations to be vigilant and proactive in detecting and preventing such attacks, and to stay informed about the latest threats and indicators of compromise.

---

> *I cannot always control what goes on outside. But I can always control what goes on inside.
Author: Wayne Dyer*

Source: [Stealthy new backdoor surfaces in attacks on multiple sectors](https://www.helpnetsecurity.com/2026/06/25/mistic-backdoor-woodgnat-attacks/)
