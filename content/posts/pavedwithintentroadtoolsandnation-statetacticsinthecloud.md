---
title: "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud"
date: 2026-05-22T10:00:24+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud":

ROADtools is a publicly available toolkit used for offensive and defensive security purposes, which has been integrated into cloud attacks by attackers. The tool is designed to enumerate Entra ID, register devices, and acquire, exchange, and manipulate Microsoft Entra ID tokens. ROADtools operates through legitimate Microsoft APIs, making it difficult to detect, and can mimic typical traffic by configuring request attributes such as user-agent strings. Nation-state threat actors have used ROADtools in recent cloud intrusions for discovery, persistence, and defense evasion.

The ROADtools framework consists of several modules, including roadrecon and roadtx, which provide internal discovery and enumeration, and token acquisition and exchange capabilities, respectively. The roadrecon module gathers organizational data and identity information from Entra ID, while the roadtx module facilitates token acquisition and exchange, enabling attackers to interact with Entra ID's authentication endpoints. The tool also includes a library layer, roadlib, which handles low-level authentication and API requests, making it easy to adapt to other security tooling and target a wider range of authentication systems.

Nation-state threat actors have leveraged ROADtools to conduct malicious activity, including discovery, enumeration, and persistence in cloud environments. The tool's capabilities have been used to register rogue devices, acquire tokens, and bypass multi-factor authentication (MFA). To protect against ROADtools, defenders can use straightforward hunting queries to reveal its usage and implement practical recommendations to detect and prevent its effectiveness. Palo Alto Networks customers can also utilize products and services such as Cortex Cloud, Cortex XDR, and XSIAM to better protect themselves against the threats described.

---

> *Work out your own salvation. Do not depend on others.
Author: Buddha*

Source: [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)
