---
title: "Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations"
date: 2026-07-06T18:34:26+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

An Iranian hacking group, affiliated with Iran's Ministry of Intelligence and Security (MOIS), has been using a new command-and-control (C2) framework called Cavern to target Israeli organizations. The framework is modular and adaptable, with multiple compilation formats, making it difficult for reverse engineers to analyze. The hacking group, tracked by Check Point Research as Cavern Manticore, has primarily targeted IT providers and government sectors, using the Cavern framework to gain persistent access and steal data.

The Cavern framework consists of multiple components, including a Cavern Agent and various modules, each with specific responsibilities. The agent loads a communication DLL module to contact the C2 server and fetch additional post-exploitation modules. The modules include tools for file operations, database enumeration, Active Directory reconnaissance, and network reconnaissance. The framework's use of different .NET compilation targets and anti-analysis techniques makes it challenging to detect and analyze. The hacking group has used the Cavern framework to attack Israeli organizations, often by exploiting trusted relationships in the software supply chain.

The attacks attributed to Cavern Manticore are part of a broader campaign by Iranian state-sponsored threat actors, including MuddyWater, which has been conducting reconnaissance and targeted attacks against organizations in the Middle East. The campaign has involved exploiting known vulnerabilities in internet-exposed systems, including SmarterMail, n8n, and Laravel Livewire. The attacks have resulted in the exfiltration of sensitive data from compromised environments, highlighting the need for organizations to be vigilant and take measures to protect themselves against these types of threats. The ongoing joint military operation between Israel and the US against Iran may be contributing to the increased cyber activity by Iranian threat actors.

---

> *You have to believe in yourself.
Author: Sun Tzu*

Source: [Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html)
