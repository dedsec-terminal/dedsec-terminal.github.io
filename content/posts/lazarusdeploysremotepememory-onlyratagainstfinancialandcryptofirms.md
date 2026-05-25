---
title: "Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms"
date: 2026-05-25T09:32:54+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The North Korea-linked Lazarus Group has been using a cross-platform malware called RemotePE to target financial and cryptocurrency organizations. RemotePE is a memory-only remote access trojan (RAT) that is part of a multi-stage attack chain, involving two loaders: DPAPILoader and RemotePELoader. The malware is designed to evade detection and leave no filesystem artifacts, making it difficult to track.

The attack chain begins with the compromise of an employee's device through social engineering, followed by the deployment of DPAPILoader, which decrypts and loads RemotePELoader. RemotePELoader then contacts a remote server, fetches the core module, and executes it in memory. The final stage is the RemotePE RAT, which polls a command-and-control (C2) server for further instructions and supports various commands, including file operations, process management, and network communication.

The researchers at Fox-IT, who discovered RemotePE, believe that the malware is purpose-built for long-term observation campaigns, allowing the actor to quietly maintain access over an extended period before moving to a high-impact final objective. The toolset's low detection rate and environmental keying suggest that it may be reserved for high-value targets where long-term, stealthy access is the objective. The Lazarus Group's use of RemotePE is consistent with their known focus on financial and cryptocurrency organizations, and the malware's capabilities are designed to support large-scale financial heists or data theft.

---

> *A really great talent finds its happiness in execution.
Author: Johann Wolfgang von Goethe*

Source: [Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms](https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html)
