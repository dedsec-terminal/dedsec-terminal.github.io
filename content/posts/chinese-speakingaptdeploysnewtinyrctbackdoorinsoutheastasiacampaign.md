---
title: "Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia Campaign"
date: 2026-06-26T16:21:25+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A Chinese-speaking advanced persistent threat (APT) actor, known as CL-STA-1062, has been linked to a new custom backdoor called TinyRCT. This backdoor is part of a cyber attack campaign targeting government entities and critical infrastructure in Southeast Asia, particularly state-owned enterprises in the energy and government sectors. The campaign has been ongoing since at least March 2022, with a sustained focus on the region.

The TinyRCT backdoor is a bespoke, previously undocumented malware that allows the attackers to run arbitrary commands, enumerate files, exfiltrate data, capture device screens, and delete itself from compromised hosts. It establishes a persistent communication channel with a remote server over HTTP, using AES-128 encryption to exchange data. The backdoor is delivered through a malicious archive containing a legitimate executable and a rogue DLL, which triggers an AppDomainManager injection attack to load the malicious DLL.

The CL-STA-1062 threat actor has been observed using a hybrid toolkit, combining common open-source tools like SoftEther VPN and VNT with custom malware like TinyRCT. The campaign has resulted in the breach of at least 10 organizations in Southeast Asia between October and December 2025. The attackers' ability to customize tools and develop custom malware, such as TinyRCT, suggests that CL-STA-1062 activity will continue to pose a threat to the region. The discovery of TinyRCT underscores the importance of monitoring and detecting such threats to prevent further attacks on critical infrastructure.

---

> *Only do what your heart tells you.
Author: Princess Diana*

Source: [Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia Campaign](https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html)
