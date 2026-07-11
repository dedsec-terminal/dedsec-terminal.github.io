---
title: "Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot"
date: 2026-07-10T15:57:14+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers at Binarly, a firmware security firm, have discovered six new vulnerabilities in U-Boot, a widely used bootloader that starts up hardware such as home routers, smart cameras, and data-center servers. The flaws can be exploited to crash devices or run malicious code at boot time, potentially undermining the entire chain of trust. Four of the bugs can cause a device to crash, while the other two could allow an attacker to run their own code before the device has confirmed the software's authenticity.

The vulnerabilities, tracked as BRLY-2026-037 through BRLY-2026-042, are related to weak spots in U-Boot's digital signature check. The bugs can be exploited when U-Boot is reading an untrusted image, before it has checked the signature. The two most severe bugs, BRLY-2026-037 and BRLY-2026-038, can allow an attacker to run code on the device, while the other four can only cause a crash. The vulnerabilities have been present in U-Boot since version 2013.07 and affect over 50 stable releases, as well as many vendor firmwares built on top of U-Boot.

The impact of these vulnerabilities is significant, as they can allow an attacker to subvert the entire chain of trust on a device. In the worst case, recovering a device that will not boot may require physical access and reflashing its memory chip with a clean image. While there is no stable release with the fix yet, vendors and maintainers of U-Boot-based products are advised to pull the upstream fixes now and track them by advisory ID. Users of devices built on U-Boot should watch for firmware updates from their product vendors, which will be necessary to fix the vulnerabilities.

---

> *Nothing diminishes anxiety faster than action.
Author: Walter Anderson*

Source: [Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot](https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html)
