---
title: "MuddyWater Uses DLL Side-Loading in Espionage Campaign Targeting 9 Countries"
date: 2026-05-26T15:48:41+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The Iranian hacking group MuddyWater has been linked to a new espionage campaign targeting at least nine organizations across nine countries on four continents. The campaign, which occurred in the first quarter of 2026, targeted various sectors including industrial and electronics manufacturing, education, public-sector bodies, financial services, and professional services. Victims include a major South Korean electronics manufacturer, an international airport in the Middle East, and a Latin American financial-services provider.

The attackers used DLL side-loading techniques to execute malicious code, masquerading as legitimate software. They used signed binaries from Fortemedia and SentinelOne to load rogue DLLs, which contained code to connect to attacker-controlled IP addresses and steal sensitive data from Chromium-based browsers. The attackers also used Node.js scripts to launch PowerShell code for discovery and information gathering operations. Additionally, they employed open-source tools like ChromElevator to siphon passwords, cookies, and payment card data.

The campaign is notable for its use of sophisticated techniques, including the use of legitimate software to bypass signature-based detection and the employment of a bespoke C++ file collection and exfiltration tool. The attacks are also characterized by efforts to dump credentials, move laterally across networks, and stage stolen data on public file-transfer services. The campaign is consistent with MuddyWater's history of quieter, more disciplined operations, and highlights the group's continued evolution and sophistication. The attacks have been linked to Iran's Islamic Revolutionary Guard Corps Cyber-Electronic Command (IRGC-CEC) and the country's Ministry of Intelligence and Security (MOIS).

---

> *Every time you smile at someone, it is an action of love, a gift to that person, a beautiful thing.
Author: Mother Teresa*

Source: [MuddyWater Uses DLL Side-Loading in Espionage Campaign Targeting 9 Countries](https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html)
