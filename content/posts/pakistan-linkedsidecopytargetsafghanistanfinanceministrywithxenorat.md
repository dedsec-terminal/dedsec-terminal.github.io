---
title: "Pakistan-Linked SideCopy Targets Afghanistan Finance Ministry with Xeno RAT"
date: 2026-06-02T09:05:40+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have uncovered a spear-phishing campaign, codenamed Operation XENOFISCAL, targeting Afghanistan's Ministry of Finance with the Xeno RAT remote access trojan. The campaign, attributed to the Pakistan-aligned SideCopy group, begins with a ZIP archive containing a malicious LNK file with a Pashto-language filename. This deliberate choice of language reflects the attacker's familiarity with the target environment, as Pashto is the main language spoken in Afghan government circles.

The campaign also targets provincial revenue and finance directorates, Pashto-speaking government officials, and provincial-level government employees. Once executed, the malware establishes persistence, drops a decoy document, and connects to a remote server to receive commands. Xeno RAT is equipped with various capabilities, including loading external DLL modules, transmitting data, launching malware, and logging keystrokes. This campaign is part of a broader cluster of malicious cyber activity aimed at South Asian entities, with SideCopy previously targeting various sectors in India with Xeno RAT and other malware.

The disclosure of Operation XENOFISCAL comes as another targeted phishing operation has been reported, this time targeting the Indian military infrastructure using weaponized Linux .desktop files. This campaign, assessed to be the work of Transparent Tribe, uses WhatsApp-based social engineering and staged shell payload delivery to target individuals connected to Indian military and defense infrastructure ecosystems. The campaign involves a heavily obfuscated shell-based infection chain and the deployment of a Golang-based ELF implant, highlighting the ongoing threat posed by these groups to South Asian entities.

---

> *Stay committed to your decisions, but stay flexible in your approach.
Author: Tony Robbins*

Source: [Pakistan-Linked SideCopy Targets Afghanistan Finance Ministry with Xeno RAT](https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html)
