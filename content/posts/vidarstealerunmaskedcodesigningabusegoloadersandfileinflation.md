---
title: "Vidar Stealer Unmasked: Code Signing Abuse, Go Loaders and File Inflation"
date: 2026-07-07T22:00:21+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a 3-paragraph summary of the article:

In April 2026, researchers at Unit 42 discovered a financially motivated campaign delivering Vidar stealer and the XMRig cryptocurrency miner to victims worldwide. The attackers lure victims through malvertising, leading them to download password-protected archives that impersonate cracked versions of copyright-protected software. Once executed, the loader drops and runs both Vidar stealer and XMRig, targeting browser credentials, cookies, and crypto wallets, as well as mining Monero cryptocurrency.

The campaign uses a loader binary signed with a fabricated Authenticode certificate impersonating JustWatch GmbH, a legitimate German streaming guide service. The loader binaries are built using the Factory-v3 framework, a malware-as-a-service (MaaS) builder used for different families of stealer malware. The loaders employ anti-forensic measures, such as zeroing the PE TimeDateStamp and reducing DLL imports, to evade detection. The campaign also uses file-size inflation, appending hundreds of megabytes of null bytes to the loader binaries to bypass automated sandbox environments.

The attack chain begins with malvertising, followed by the execution of the loader binary, which drops multiple payloads, including Vidar stealer and XMRig. The malware establishes persistence mechanisms, gathers information about the victim's system, and exfiltrates sensitive data to a command-and-control (C2) server. The attacker is notified of new activity via Telegram, and the XMRig miner begins mining Monero using a mining pool. The campaign is believed to be operated by a Vidar stealer MaaS affiliate, targeting victims in the U.S. and European Union. Palo Alto Networks customers are protected from these threats through various products and services, including Cortex XDR and Advanced WildFire.

---

> *To live a pure unselfish life, one must count nothing as ones own in the midst of abundance.
Author: Buddha*

Source: [Vidar Stealer Unmasked: Code Signing Abuse, Go Loaders and File Inflation](https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/)
