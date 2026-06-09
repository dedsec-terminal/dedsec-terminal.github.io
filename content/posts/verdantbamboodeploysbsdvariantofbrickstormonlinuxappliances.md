---
title: "VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances"
date: 2026-06-08T10:27:32+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A China-nexus cyber espionage group, known as VerdantBamboo, has been observed deploying a BSD variant of the BRICKSTORM backdoor, as well as two other malware families, PLENET and AGENTPSD, to target Linux systems. This activity was attributed to VerdantBamboo by Volexity, a cybersecurity company that tracks the threat cluster. The group is also known by other names, including Clay Typhoon, UNC5221, and Warp Panda, and has been linked to previous hacking incidents.

The malware deployment was discovered during an incident response engagement in September 2025, when Volexity found that the adversary had compromised an unnamed victim's Egnyte Storage Sync system by exploiting a local privilege escalation flaw. The issue was addressed in a later version of Storage Sync, but not before the threat actor had used the malware to access the victim's Microsoft 365 environment. The actor used the malware's proxying capabilities and compromised credentials to blend in with legitimate network traffic and evade Conditional Access policies.

VerdantBamboo is considered a highly sophisticated threat actor that uses a combination of living-off-the-land techniques and malware deployment to target systems that do not or cannot run endpoint detection and response (EDR) software. The group has been found to have good knowledge of proprietary appliances, allowing them to deploy malware with customized persistence mechanisms. They also appear to have operational security discipline, using a limited number of domains and IP addresses per victim and setting up customized implant naming and persistence on a per-device basis. The group's activities have been linked to previous attacks, including the exploitation of a vulnerability in Dell RecoverPoint for Virtual Machines.

---

> *Blessed is the man who expects nothing, for he shall never be disappointed.
Author: Alexander Pope*

Source: [VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances](https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html)
