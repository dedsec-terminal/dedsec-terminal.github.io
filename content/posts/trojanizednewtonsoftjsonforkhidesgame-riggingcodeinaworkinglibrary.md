---
title: "Trojanized Newtonsoft.Json Fork Hides Game-Rigging Code in a Working Library"
date: 2026-07-22T06:00:06+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a malicious NuGet package called "Newtonsoftt.Json.Net" that masquerades as the legitimate Newtonsoft.Json library. The package is a trojanized fork that has been downloaded around 1,200 times and has been unlisted by its owner. However, the package is still available for download from the registry, and its artifacts can be accessed.

The package is designed to rig live game results on Digitain, an online betting platform, by exfiltrating rigged round results to an attacker-controlled server. The malicious behavior is triggered after the host initializes JsonConvert.DefaultSettings, and it can only succeed on systems that expose the target's specific game backend method. The package functions as expected for other users, making it a targeted and stealthy attack. The backdoor initiates itself via the DefaultSettings property setter, which has been altered to invoke attacker-controlled code and introduce a randomized delay to sidestep detection.

The package has undergone three generations of development, with each version containing the same trojanized fork of Newtonsoft.Json 13.0. The author has iteratively hardened the payload, adding exfiltration capabilities and obfuscation techniques. The primary victim of the rigging is Digitain, and the package metadata has been found to leak an internal Digitain repository URL. To counter the threat, developers are advised to remove the typosquat package, block the command-and-control address, and pin Newtonsoft.Json to a known-good version. Digitain has revealed that it is aware of the issue and has taken steps to resolve it, but the full extent of the exposure remains unknown.

---

> *It all depends on how we look at things, and not how they are in themselves.
Author: Carl Jung*

Source: [Trojanized Newtonsoft.Json Fork Hides Game-Rigging Code in a Working Library](https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html)
