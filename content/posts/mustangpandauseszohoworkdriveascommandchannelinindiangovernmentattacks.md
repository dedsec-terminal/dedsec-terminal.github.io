---
title: "Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks"
date: 2026-06-29T15:03:40+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The China-aligned espionage group Mustang Panda has launched two campaigns against the Indian government and hydropower targets, utilizing new malware and exploiting a legitimate cloud service as a command channel. The group has compromised Indian government networks, including machines used by senior administrative staff, and has been using Zoho WorkDrive, a cloud storage platform, to pass commands and exfiltrate data. This tactic allows the malicious traffic to blend in with ordinary cloud activity, making it difficult to detect.

The malware used in the campaigns includes three new tools: SHARDLOADER, MINIRECON, and ZOHOMURK. SHARDLOADER is a loader that runs by sideloading a malicious DLL through a legitimate binary, while MINIRECON is a reworked variant of the Toneshell backdoor. ZOHOMURK is a novel piece of malware that uses hardcoded Zoho OAuth credentials to control a WorkDrive account, reading commands from an inbox folder and writing stolen output to an outbox. The campaigns are believed to have been delivered through spear-phishing emails with lures themed around hydropower cooperation and memorandums of understanding between Indian and Taiwanese institutions.

The goal of the campaigns is to gather intelligence on India's hydropower plans and its defense ties with Taiwan. Acronis attributes the activity to Mustang Panda with high confidence, citing reused infrastructure, code overlap, and a recurring typo. The report includes indicators and hunting tips to help organizations detect and prevent similar attacks. Government and energy organizations, particularly those involved in cross-border deals, are advised to watch for geopolitical lures and sideloading from signed binaries, and to flag any endpoint process calling cloud APIs that it has no reason to touch.

---

> *If you let go a little, you will have a little peace. If you let go a lot, you will have a lot of peace.
Author: Ajahn Chah*

Source: [Mustang Panda Uses Zoho WorkDrive as Command Channel in Indian Government Attacks](https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html)
