---
title: "Bypassing On-Camera Age-Verification Checks"
date: 2026-05-15T11:06:32+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Some AI-based video age-verification checks can be bypassed using simple methods such as wearing a fake mustache. The primary purpose of these checks is not to verify age, but to de-anonymize critics and enable governments to deny access to online platforms. The failure to keep minors out of adult spaces is not surprising, as this is not the ultimate goal of these checks. Researchers have found that current zero-knowledge proofs have several failings, including the need for interaction, setup, and imperfect soundness.

A recent paper has proposed a new relaxation of zero-knowledge proofs that achieves perfect soundness and no interaction, which could have significant benefits for age verification and other applications. The paper defines a new concept of zero-knowledge that only requires that one cannot rule out the existence of a simulator, rather than requiring that a simulator actually exists. This enables the removal of interaction and setup from classical zero-knowledge proofs, making them more practical and secure.

The discussion around age verification has also touched on the topic of hacking hard drive firmware, with some researchers exploring the possibility of modifying firmware to exploit vulnerabilities. One researcher discovered that some hard drives have backdoor vendor commands and connections to diagnostic ports, which could be used to access and modify the firmware. Others have noted that the microcontrollers in hard drives can be quite powerful and problematic, with some having multiple ARM CPUs and shared memory.

The conversation has also highlighted the importance of security research and the need to stay one step ahead of attackers. As one commenter noted, the question is not whether you can make it difficult for honest users, but whether the system can withstand the creativity of attackers. Another commenter pointed out that the current system can be bypassed by a 12-year-old with a makeup pencil, and that more robust security measures are needed. Researchers are exploring new methods to bypass hardware attestation recapthca, which is being developed by Google, and are looking for ways to cheat the new captcha using Linux desktops or GrapheneOS phones. 

The use of Intel ME and AMD PSP has also been discussed, with one researcher noting that these can be removed by formatting the partition in SPI, which can help to improve security by preventing remote access and bypassing system security. However, this requires the right connectors and cables, as well as some technical know-how. Overall, the discussion highlights the ongoing cat-and-mouse game between security researchers and attackers, and the need for continued innovation and vigilance to stay ahead of emerging threats.

---

> *A little knowledge that acts is worth infinitely more than much knowledge that is idle.
Author: Kahlil Gibran*

Source: [Bypassing On-Camera Age-Verification Checks](https://www.schneier.com/blog/archives/2026/05/bypassing-on-camera-age-verification-checks.html)
