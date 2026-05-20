---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API"
date: 2026-05-20
draft: false
categories:
  - threat-intelligence
author: "DedSec-Terminal"
---

Cybersecurity researchers have flagged fresh activity from a China-aligned threat actor known as Webworm in 2025, deploying custom backdoors that employ Discord and Microsoft Graph API for command-and-control (C2 or C&C) communications.

Webworm, first publicly documented by Broadcom-owned Symantec in September 2022, is assessed to be active since at least 2022, targeting government agencies and enterprises spanning IT services, aerospace, and electric power sectors in Russia, Georgia, Mongolia, and several other Asian nations.

Attacks mounted by the group have leveraged remote access trojans (RATs) like Trochilus RAT, Gh0st RAT, and 9002 RAT (aka Hydraq and McRat). The threat actor is said to overlap with China-nexus clusters tracked as FishMonger (aka Aquatic Panda), SixLittleMonkeys, and Space Pirates. SixLittleMonkeys is best known for deploying Gh0st RAT and a RAT called Mikroceen targeting entities in Central Asia, Russia, Belarus, and Mongolia.

"In recent years, it has started moving toward both existing and custom proxy tools, which are more stealthy than full-fledged backdoors," ESET researcher Eric Howard said. "In 2025, Webworm also added two new backdoors to its toolset: EchoCreep, which uses Discord for C&C communication, and GraphWorm, which uses Microsoft Graph API for the same purpose."

Underlying these efforts is the use of a GitHub repository impersonating a WordPress fork ("github[.]com/anjsdgasdf/WordPress") as a staging ground for malware and tools like SoftEther VPN in an effort to blend in and fly under the radar. The reliance on SoftEther VPN is a tried-and-tested approach adopted by several Chinese hacking groups.

Over the past two years, the adversary has been observed shifting away from traditional backdoors to (semi-)legitimate utilities such as SOCKS proxies, while also increasingly focusing on European countries, including governmental organizations in Belgium, Italy, Serbia, Poland, and Spain, and a local university in South Africa.

*The bamboo that bends is stronger than the oak that resists. — Japanese saying*

Source: [The Hacker News](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html) · [Read Original →](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
