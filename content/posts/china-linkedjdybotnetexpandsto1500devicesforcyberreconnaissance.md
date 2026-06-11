---
title: "China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance"
date: 2026-06-10T16:08:42+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Introduction to JDY Botnet**
The JDY botnet, a covert network linked to China-nexus state-sponsored threat actors, has experienced a resurgence and expansion. According to Lumen's Black Lotus Labs, the botnet now comprises over 1,500 small office and home office (SOHO) and Internet of Things (IoT) devices. These devices operate as a centrally controlled, high-performance scanner to discover, fingerprint, and continuously map exposed services at scale.

**Expansion and Operations**
The JDY botnet was initially flagged in mid-December 2023 as a cluster within the KV-botnet. Following the KV-botnet's takedown in early 2024, the botnet operators made behavioral changes, and the JDY cluster expanded to infect a broader range of devices. The malware now acts as a conduit to feed "structured reconnaissance data" into a larger scanning ecosystem for follow-on target identification and exploitation. The botnet's size has surged from 650 bots to over 1,500 compromised devices, with most located in the US, Brazil, Europe, and Asia.

**Architecture and Implications**
The botnet's architecture is layered, using Tor nodes to manage infected infrastructure, including command-and-control (C2) and payload servers. The C2 servers direct bots to perform targeted reconnaissance and system profiling. The malware is designed to fingerprint hosts, receive scanning tasks, and report results back to the dispatch server. The goal is to conduct infrastructure reconnaissance rather than exploitation. The JDY botnet's growth and continued operation demonstrate how modern reconnaissance networks persist despite takedowns and adapt as a durable capability within a broader adversary ecosystem, providing timely targeting data to Chinese nation-state groups.

---

> *If we are facing in the right direction, all we have to do is keep on walking.*

Source: [China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance](https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html)
