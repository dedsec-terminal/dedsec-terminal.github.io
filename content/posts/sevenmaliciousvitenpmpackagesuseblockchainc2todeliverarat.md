---
title: "Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT"
date: 2026-07-17T18:54:51+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered seven malicious npm packages targeting the Vite frontend tooling ecosystem as part of a software supply chain attack. The packages, codenamed ViteVenom, use a blockchain-based command-and-control (C2) infrastructure to deliver a remote access trojan (RAT) capable of reverse shell, credential harvesting, file exfiltration, and persistent backdoor injection. The malicious packages were published between June 29 and July 3, 2026, and have been downloaded a total of over 2,500 times.

The ViteVenom campaign is an expansion of the ChainVeil campaign, which was observed using a four-tier blockchain-based C2 infrastructure spanning Tron, Aptos, and Binance Smart Chain. The malicious packages use scoped package names to impersonate the "@vitejs/*" namespace and lend a veneer of legitimacy. The code doesn't execute at install time but at import time, limiting endpoint security detections. The malware acts as a loader, reaching out to the blockchain infrastructure to obtain the next-stage payload, which is then decrypted using a hard-coded key.

The activity has been attributed to a threat actor named SuccessKey, with evidence of malicious activity detected as far back as February 27, 2026. Users who have installed the packages are advised to remove them immediately, audit dependencies, rotate all credentials, and look for unauthorized modifications to system files. The use of blockchain-based C2 infrastructure makes it extremely difficult to disable or destroy the infrastructure, and the malware's ability to fetch the RAT directly from the C2 server over HTTP bypasses the blockchain, making it a significant threat to users.

---

> *If the shoe doesn't fit, must we change the foot?
Author: Gloria Steinem*

Source: [Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT](https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html)
