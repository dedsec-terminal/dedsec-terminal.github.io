---
title: "New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions"
date: 2026-07-06T08:50:54+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Researchers at Shandong University have developed a new method called TrojPix, which allows data to be leaked from air-gapped systems via video cable emissions. This technique works by tweaking on-screen pixels to radiate a faint radio signal that can be decoded by a nearby receiver. The method requires malware to be already present on the target machine, making it a way for stolen data to be exfiltrated, rather than a means of gaining initial access.

TrojPix has been shown to achieve a peak throughput of 8.1 Mbps and can transmit data up to 208 meters. This is significantly faster than other air-gap covert channels, which typically operate at bits or kilobits per second. The researchers have demonstrated that TrojPix can work with various monitor brands and video cables, and can even hide the transmitted data by faking a powered-off display or burying the signal in ordinary-looking content.

The TrojPix attack highlights the importance of preventing malware from infecting air-gapped systems in the first place. Since the emission itself cannot be patched away, countermeasures must be physical and preventive. This includes using fiber-optic links instead of copper cables, shielding cables and rooms, and keeping malware off the machine. The researchers' work demonstrates the potential for fast and covert data exfiltration, and serves as a reminder of the need for robust security measures to protect sensitive data.

---

> *Neither genius, fame, nor love show the greatness of the soul. Only kindness can do that.
Author: Jean Lacordaire*

Source: [New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions](https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html)
