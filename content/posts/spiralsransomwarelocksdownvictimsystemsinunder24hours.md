---
title: "Spirals ransomware locks down victim systems in under 24 hours"
date: 2026-07-17T12:25:24+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new ransomware strain called Spirals was used in an attack against an IT services company in South Asia, where attackers gained initial access and encrypted the network in under 24 hours. The Spirals ransomware is written in Rust and uses a separate AES-128 key per file, with files larger than 5 MB being encrypted in chunks to speed up the process. The attackers left a ransom note directing victims to a Tor negotiation site, threatening to leak stolen data if no payment was made.

The attackers gained initial access by compromising an internet-facing IIS web server and uploading an ASP.NET web shell. They then escalated privileges, turned on Remote Desktop Protocol (RDP), and created a local account to maintain persistent access. The attackers also dumped credential material, set up a reverse SOCKS proxy, and used tunneling tools to keep lines of communication open with the compromised network. Some of the tools used in the attack were hosted externally with .jpg file extensions to evade basic file-type filtering.

The attackers used a PowerShell payload to disable Windows Defender and stop services tied to backup, database, and virtualization products, clearing the way for the ransomware to encrypt files. Symantec's Threat Hunter Team notes that the capabilities and stealth of the Spirals ransomware suggest that the actors behind it are skilled operators who could launch more wide-ranging campaigns. The company has shared indicators of compromise tied to the attack, allowing organizations to check their environments for related activity. While only one victim network has been reported so far, the potential for further attacks is a concern.

---

> *Everything is perfect in the universe � even your desire to improve it.
Author: Wayne Dyer*

Source: [Spirals ransomware locks down victim systems in under 24 hours](https://www.helpnetsecurity.com/2026/07/17/spirals-ransomware-south-asia/)
