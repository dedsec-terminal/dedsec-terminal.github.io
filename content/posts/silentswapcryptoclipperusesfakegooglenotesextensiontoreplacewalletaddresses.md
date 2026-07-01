---
title: "Silent Swap Crypto Clipper Uses Fake Google Notes Extension to Replace Wallet Addresses"
date: 2026-06-30T15:40:18+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Silent Swap Crypto Clipper Campaign**
A recent cybersecurity report by McAfee Labs has uncovered a malicious browser extension campaign, dubbed Silent Swap, designed to steal cryptocurrency by replacing wallet addresses. The campaign uses a fake Google Notes extension to intercept and manipulate wallet addresses copied into the system clipboard, rerouting funds to an attacker-controlled wallet. The extension requests permissions to access the clipboard, URLs, and browsing history, allowing it to act as a clipper and steal sensitive information.

**Techniques and Evasion Methods**
The Silent Swap campaign employs various techniques to evade detection, including the use of EtherHiding, which utilizes the blockchain as a dead drop resolver to retrieve command-and-control server details. The malware also modifies protected browser settings files to install the extension on Chromium-based browsers, such as Google Chrome, Microsoft Edge, and Brave, without user approval. Additionally, the campaign uses dynamic wallet substitution, which fetches a replacement address corresponding to a victim's original address, and registers the extension to load silently on subsequent browser launches.

**Global Impact and Related Threats**
The Silent Swap campaign has been found to have a global distribution, with a higher concentration of victims reported in India, the US, Brazil, Indonesia, and Spain. The campaign's techniques and evasion methods have been characterized as deliberate and layered, with a primary focus on maintaining low visibility and high resilience against takedown and static analysis. Meanwhile, another report by Socket has revealed a pair of malicious Chrome and Firefox extensions, posing as free VPNs, which contain clipboard-stealing logic that exfiltrates sensitive data, including passwords, authentication codes, and wallet addresses, to threat actor-controlled infrastructure.

---

> *Cherish your visions and your dreams as they are the children of your soul; the blueprints of your ultimate achievements.
Author: Napoleon Hill*

Source: [Silent Swap Crypto Clipper Uses Fake Google Notes Extension to Replace Wallet Addresses](https://thehackernews.com/2026/06/silent-swap-crypto-clipper-uses-fake.html)
