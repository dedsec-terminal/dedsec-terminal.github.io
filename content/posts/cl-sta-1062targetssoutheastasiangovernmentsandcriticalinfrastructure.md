---
title: "CL-STA-1062 Targets Southeast Asian Governments and Critical Infrastructure"
date: 2026-06-25T22:00:52+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the report:

A Chinese-speaking threat actor, tracked as CL-STA-1062, has been targeting government entities and critical infrastructure in Southeast Asia since at least March 2022. The group's activities were observed in 2025, with a focus on state-owned enterprises in the energy and government sectors. CL-STA-1062 is believed to be the same cluster as UAT-7237, which was previously reported for its campaigns against web hosting infrastructure in Taiwan.

The attackers use a hybrid toolkit, including common open-source tools such as SoftEther VPN, Mimikatz, and VNT, as well as a bespoke backdoor called TinyRCT. TinyRCT is a lightweight, C#-based remote access Trojan (RAT) that enables attackers to execute arbitrary system commands, exfiltrate files, capture screenshots, and remotely manage the infected host. The malware uses AES-128 encryption and operates on a beaconing model, polling the command and control (C2) server for instructions.

The threat actor's tactics, techniques, and procedures (TTPs) include exploiting web applications to deploy ASPX web shells, using tunneling tools for command and control and data exfiltration, and disguising malware as legitimate system files. The attackers also use open-source tools such as JuicyPotato to escalate privileges and compress findings into password-protected RAR archives. The discovery of TinyRCT highlights the evolving nature of CL-STA-1062's TTPs and the need for organizations to implement strict behavioral monitoring and execution restrictions on untrusted binaries to prevent similar attacks.

---

> *Silence is a source of great strength.
Author: Lao Tzu*

Source: [CL-STA-1062 Targets Southeast Asian Governments and Critical Infrastructure](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/)
