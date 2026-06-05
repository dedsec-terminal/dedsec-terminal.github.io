---
title: "New Threat Cluster OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework"
date: 2026-06-05T12:33:38+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a new threat cluster called OP-512, which targets Microsoft Internet Information Services (IIS) servers to deploy a custom web shell framework. ReliaQuest has linked this activity to China with moderate to high confidence, suggesting that OP-512 is conducting espionage through compromised IIS web servers. This is the fourth China-linked threat group to target IIS servers in the past 12 months, following CL-STA-0048, DragonRank, and GhostRedirector.

The OP-512 threat cluster uses a bespoke web shell framework consisting of three web shells that grant remote access to the compromised host while evading signature-based detection. The framework takes steps to complicate forensic timelines by manipulating timestamps and using techniques like timestomping. The web shells are uniquely generated, and access is restricted to the attacker through cryptographic controls. The compromised servers also automatically report back for centralized management at scale. This framework combines capabilities that are rarely seen together, making OP-512 a distinct and autonomous threat cluster.

The attack observed by ReliaQuest involved targeting a legacy IIS server running Windows Server 2016 with end-of-life .NET Framework 4.0. The threat actor used the web server's worker process to drop one of the web shells, triggering a self-reporting mechanism that transmitted the web shell's location to an attacker-controlled domain. OP-512 then attempted to escalate privileges to the SYSTEM level and ran commands to confirm system rights. The fact that four China-linked clusters have targeted IIS servers in under a year suggests that this is a preferred entry point for these threat actors, and organizations should be concerned about OP-512's purpose-built framework designed to defeat detection methods.

---

> *Think for yourselves and let others enjoy the privilege to do so too.
Author: Voltaire*

Source: [New Threat Cluster OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework](https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html)
