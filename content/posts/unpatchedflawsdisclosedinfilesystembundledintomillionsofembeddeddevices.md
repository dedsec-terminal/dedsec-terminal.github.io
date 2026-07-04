---
title: "Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices"
date: 2026-07-03T20:19:31+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

**Vulnerabilities in FatFs Filesystem Library**
Security firm runZero has disclosed seven vulnerabilities in the FatFs filesystem library, which is widely used in millions of embedded devices, including security cameras, drones, and industrial controllers. The flaws allow an attacker to corrupt memory and run their own code on affected devices by using a booby-trapped USB drive, SD card, or update file. The vulnerabilities are particularly concerning because many embedded devices lack memory protections, making them more susceptible to attacks.

**Impact and Affected Devices**
The vulnerabilities affect a wide range of devices, including those from Espressif, STMicroelectronics, Zephyr, MicroPython, and Samsung, among others. The flaws can be exploited by an attacker with physical access to the device, allowing them to gain full control over the device. runZero has rated the vulnerabilities as Medium to High severity, with the most severe flaw having a CVSS score of 7.6. The company has released proof-of-concept disk images and a test harness to demonstrate the vulnerabilities.

**Patch Availability and Response**
The FatFs maintainer has not responded to runZero's attempts to contact them, and there is no upstream fix available for the vulnerabilities. As a result, downstream vendors will need to patch the vulnerabilities on their own, a process that is expected to take years. runZero is advising device manufacturers to audit their code and plan to patch the vulnerabilities, while users are advised to limit physical access to their devices and watch for vendor firmware updates. The incident highlights the challenges of securing widely used open-source libraries and the need for more effective vulnerability disclosure and patching processes.

---

> *Every adversity, every failure, every heartache carries with it the seed of an equal or greater benefit.
Author: Napoleon Hill*

Source: [Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices](https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html)
