---
title: "New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic"
date: 2026-07-10T13:15:23+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new remote access trojan (RAT) called MODBEACON has been discovered, attributed to the China-linked cybercrime group Silver Fox. MODBEACON is a Rust-based RAT that uses gRPC streaming for encrypted command-and-control (C2) traffic, making it a sophisticated threat. The malware is delivered through counterfeit software installers, often using search engine optimization (SEO) poisoning techniques to trick users into downloading malicious files.

The Silver Fox group is believed to have a complex organizational structure, with multiple distributors conducting activities across Asia. These distributors use various tactics, including SEO campaigns and counterfeit software installers, to spread malware such as Gh0st RAT and WinOS (ValleyRAT) trojan families. One distributor, assessed to be a hybrid threat actor, has been observed delivering MODBEACON to target technology, education, and state-owned enterprises in the region. The C2 infrastructure for MODBEACON is hosted on Amazon and Cloudflare's Content Delivery Network (CDN).

MODBEACON has several core capabilities, including fingerprinting the host, loading plugins in memory, sending heartbeat messages, and reporting the results of command execution. The malware can also set persistence using scheduled tasks, allowing for subsequent expansion of information theft, lateral movement, proxy forwarding, or other payloads. The discovery of MODBEACON is part of a broader trend of Silver Fox refining its tradecraft, with the group having deployed other malware families such as Atlas RAT, ABCDoor, RomulusLoader, and SilentRunLoader. The use of gRPC streaming for C2 traffic and the reuse of open-source anti-censorship proxy frameworks highlight the sophistication and professionalism of the MODBEACON malware.

---

> *Great acts are made up of small deeds.
Author: Lao Tzu*

Source: [New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic](https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html)
