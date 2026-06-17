---
title: "China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth"
date: 2026-06-16T09:44:34+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Introduction to SprySOCKS Backdoor**
Cybersecurity researchers have discovered two previously undocumented Windows variants of the SprySOCKS backdoor, which was initially believed to be a Linux-only malware. The Windows variants, marked as WIN_DRV and WIN_PLUS, come with a hard-coded command-and-control (C&C) configuration and support communication over TCP, UDP, and WebSocket protocols. These variants are part of version 1.8 of SprySOCKS and have been linked to a China-nexus state-sponsored threat actor known as Earth Lusca.

**Features and Capabilities**
The Windows variants of SprySOCKS support over 30 commands to facilitate system information collection, process enumeration, service management, and file system operations. The WIN_DRV variant utilizes kernel drivers to conceal the malware's network connections, processes, files, and registry keys, and enables TCP traffic diversion to send commands to the backdoor without exposing the actual listening port. Both variants are DLLs that support three channels for C2 communications and can run commands issued by the operator on the compromised host, including collecting system information, launching an interactive console, and uploading/downloading files.

**Attribution and Campaigns**
The SprySOCKS backdoor has been attributed to the FishMonger threat cluster, a cyber espionage group that falls under the broader Winnti umbrella. The group has been linked to a global campaign dubbed Operation FishMedley, targeting organizations in Taiwan, Hungary, Turkey, Thailand, France, and the U.S. between January and October 2022. The discovery of the Windows variants of SprySOCKS represents a significant expansion of FishMonger's cross-platform capabilities, with evidence indicating that the artifacts may have been deployed in attacks targeting government organizations in Honduras, Taiwan, Thailand, and Pakistan between 2023 and 2024.

---

> *The best thing about the future is that it only comes one day at a time.
Author: Abraham Lincoln*

Source: [China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth](https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html)
