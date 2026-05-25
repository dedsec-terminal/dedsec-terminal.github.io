---
title: "Tracking TamperedChef Clusters via Certificate and Code Reuse"
date: 2026-05-20T10:00:46+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Researchers have identified novel activity clusters related to the TamperedChef (aka EvilAI) threat, which involves trojanized productivity software delivering malicious payloads. These campaigns use malicious ads to direct users to sites hosting the applications, which share characteristics with potentially unwanted programs (PUPs) and adware. However, TamperedChef-style malware is more stealthy, remaining dormant for weeks to months before activating and using continuous command and control (C2) methods to retrieve additional payloads.

The researchers have tracked three distinct clusters of TamperedChef-style activity, identified as CL-CRI-1089, CL-UNK-1090, and CL-UNK-1110, with over 4,000 samples across 100 unique variants. These clusters employ similar tactics, techniques, and procedures (TTPs) but have distinct infrastructure, code quality, and organizations tied to code signing. The actors behind these campaigns take steps to remain undetected, including using code signing, rebuilding binaries with minor changes, and remaining dormant for long periods. They also use social engineering tactics, such as distributing via legitimate-looking websites and providing promised functionality with minimal bloat.

The researchers have observed approximately 12,000 unique instances of this fake productivity software across their customer base, with a global reach and no significant geographic or sector targeting. The clusters have been identified as active since early 2023, with CL-CRI-1089 being the most diverse in terms of deployment methods and malware techniques. The CL-UNK-1110 cluster is most commonly associated with the TamperedChef alias, while CL-UNK-1090 shows evidence of vertical integration between marketing and malware creation. The researchers emphasize the importance of understanding these differences to separate the attackers' motivations, capability, and risks.

---

> *Better than a thousand hollow words, is one word that brings peace.
Author: Buddha*

Source: [Tracking TamperedChef Clusters via Certificate and Code Reuse](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/)
