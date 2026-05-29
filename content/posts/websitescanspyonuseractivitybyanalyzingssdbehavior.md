---
title: "Websites can spy on user activity by analyzing SSD behavior"
date: 2026-05-29T10:57:47+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers have discovered a new method for websites to collect information about users' activities by analyzing the behavior of their Solid-State Drive (SSD). This technique, called FROST, allows a website to infer information about other websites and applications running on a user's system by measuring the timing differences created by competition for access to the SSD. This is a side-channel attack that exploits the Origin Private File System (OPFS), a browser feature that gives websites their own sandboxed storage area for saving data locally.

The FROST attack can be launched by simply visiting a webpage hosting the attack code, without requiring any malware, browser extensions, or software installation. The technique relies on the OPFS feature, which allows websites to store data locally, and uses JavaScript running in the browser to collect information about the user's activity. The researchers demonstrated that the same mechanism can be used to establish a communication channel through SSD contention. This attack highlights the new security and privacy challenges introduced by the shift of applications to the web, where browsers have evolved into complex platforms capable of running sophisticated applications.

The FROST technique has several practical limitations, including the requirement for long-running measurements that can consume a noticeable amount of storage space. Additionally, the attack depends on the targeted activity occurring on the same SSD being monitored, which can limit its effectiveness. Several mitigations are discussed, including limiting the amount of storage available through OPFS, reducing the precision of timing information, and alerting users to unusual storage usage. The findings were responsibly disclosed to major browser vendors, including Google, Mozilla, and Apple, but the Chromium team does not consider fingerprinting attacks to be security vulnerabilities, and no mitigations have been implemented yet.

---

> *Rainbows apologize for angry skies.
Author: Sylvia Voirol*

Source: [Websites can spy on user activity by analyzing SSD behavior](https://www.helpnetsecurity.com/2026/05/29/website-tracking-ssd-activity-research/)
