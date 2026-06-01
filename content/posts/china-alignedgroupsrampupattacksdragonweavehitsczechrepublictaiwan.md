---
title: "China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan"
date: 2026-06-01T11:54:24+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**China-Aligned Cyber Attacks Intensify**: A new cyber espionage campaign, Operation Dragon Weave, has been detected targeting officials and citizens in the Czech Republic and Taiwan. The campaign uses spear-phishing emails with ZIP attachments to deliver an AdaptixC2 agent, allowing for data exfiltration and remote control. The attack chain involves a Rust loader and a malicious DLL, with the final payload using Microsoft Azure Blob Storage for command-and-control (C2) communications.

**Attack Techniques and Tools**: The Operation Dragon Weave campaign uses two different pathways to launch the final-stage malware, including a PowerShell script and a self-contained Rust-based dropper. The malware, codenamed AZUREVEIL, supports 36 commands, allowing for a wide range of post-compromise actions, including file operations, shell command execution, and process termination. The campaign is attributed to a China-aligned threat actor, with similar attacks detected against an Indian manufacturing company using a previously undocumented Go-based implant called TencShell.

**Global China-Aligned Threat Activity**: The Operation Dragon Weave campaign is part of a larger trend of China-aligned threat activity, with multiple groups and toolkits identified in recent months. These include SteppeDriver, which has targeted entities in France, Mongolia, and South America, and NegativeGlimmer, which has breached government and critical infrastructure organizations across 37 countries. The use of various tools, such as ShadowPad, COOLCLIENT, and Cobalt Strike, highlights the sophistication and diversity of China-aligned threat actors, posing a significant threat to global cybersecurity.

---

> *Practice yourself, for heavens sake in little things, and then proceed to greater.
Author: Epictetus*

Source: [China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html)
