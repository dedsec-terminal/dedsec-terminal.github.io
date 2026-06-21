---
title: "Apple Patches Beats Studio Buds Flaw Letting Nearby Attackers Spy via Microphone"
date: 2026-06-19T06:36:09+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Apple has released a firmware update for its Beats Studio Buds wireless earbuds to patch a high-severity vulnerability that could allow nearby attackers to eavesdrop on users. The vulnerability, tracked as CVE-2025-20701, is related to incorrect authorization in the Airoha Bluetooth audio SDK, which enables pairing without user consent. This flaw could be exploited by attackers within Bluetooth range to listen through the microphone of the earbuds without requiring any additional execution privileges or user interaction.

The vulnerability was first discovered by researchers Dennis Heinze and Frieder Steinmetz in June 2025, who also identified two other flaws in Airoha SoCs. The researchers noted that these vulnerabilities could allow attackers to fully take over the headphones via Bluetooth, read and write the device's RAM and flash, and hijack established trust relationships with other devices. Apple has addressed the issue in Beats Firmware Update 1B211, and similar patches were released by Jabra in December 2025.

In a separate development, a novel iPhone SecureROM vulnerability has been discovered in Apple's A12 and A13 chips, which could allow attackers to compromise the entire device. The vulnerability, exploited by the usbliter8 proof-of-concept, leverages a hardware bug in the USB controller and a configuration flaw in the device firmware. As the vulnerability resides in immutable code, affected users are advised to migrate to newer hardware as the most effective mitigation. The usbliter8 exploit is comparable to the checkm8 exploit, which impacted earlier iPhone models, and demonstrates that subtle hardware bugs can still be leveraged to achieve full code execution and break the chain of trust.

---

> *Wherever a man may happen to turn, whatever a man may undertake, he will always end up by returning to the path which nature has marked out for him.
Author: Johann Wolfgang von Goethe*

Source: [Apple Patches Beats Studio Buds Flaw Letting Nearby Attackers Spy via Microphone](https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html)
