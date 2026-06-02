---
title: "Zero trust physical security needs trust decisions at the edge"
date: 2026-06-02T05:30:53+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article on zero trust physical security:

Zero trust physical security requires making trust decisions at the edge, without recreating old perimeter assumptions. This means that devices such as cameras and door controllers should be treated as IT assets, with centralized trust governance and distributed enforcement. According to Chuck Davis, VP of Global Information Security at Hikvision, this can be achieved through a model of distributed trust with centralized policy, where policy creation and identity governance remain centralized, but enforcement happens locally at the edge.

A key challenge in implementing zero trust physical security is the need for fast decision-making, such as unlocking a door within 200 milliseconds. This requires a design constraint that does not rely on cloud-based policy engines, but rather on local enforcement with cryptographically signed policies and short-lived credentials. Davis emphasizes that local enforcement does not mean local trust, and that edge devices should operate against centrally governed policies with well-defined access boundaries. He also notes that organizations often get into trouble operationally by extending policy cache lifetimes to avoid network issues, which can lead to a drifting perimeter.

The Mirai botnet in 2016 highlighted the importance of treating physical security devices as IT assets, with consistent standards for deployment and security. Davis argues that the most significant blind spot is the gap between physical security and IT silos, where risk often falls. To address this, he recommends isolating physical security devices on their own network segment, keeping firmware current, and following manufacturer hardening guidance. For devices that cannot run EDR agents or be patched during business hours, a zero trust posture assessment can focus on defining a "trust envelope" of acceptable behavior, using network telemetry and secure boot and signed firmware verification to validate device behavior.

---

> *Well begun is half done.
Author: Aristotle*

Source: [Zero trust physical security needs trust decisions at the edge](https://www.helpnetsecurity.com/2026/06/02/chuck-davis-hikvision-zero-trust-physical-security/)
