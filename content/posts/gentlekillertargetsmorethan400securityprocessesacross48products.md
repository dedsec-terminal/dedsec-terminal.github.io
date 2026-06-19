---
title: "GentleKiller targets more than 400 security processes across 48 products"
date: 2026-06-18T09:00:58+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

The Gentlemen ransomware gang has been found to target more than 400 security processes across 48 products using their in-house framework, GentleKiller. This framework is a set of tools developed and maintained by the gang's operators to shut down endpoint detection and response (EDR) products, which are then provided to affiliates who rent the gang's encryptors. An internal data leak in May 2026 confirmed the arrangement and exposed the gang's leader discussing the supply of these EDR-killer packages.

GentleKiller has eight variants, each impersonating a different legitimate product and abusing a different vulnerable or malicious kernel driver. The variants share code, a process-killing loop, and obfuscation, indicating a reused development template. The gang adapts newly published proofs-of-concept quickly, incorporating them into their tooling within days of release. Additionally, the suite includes three tools obtained from outside sources, which have been standardized to match the gang's own toolset. A shared evasion layer ties the portfolio together, making it difficult for defenders to attribute the tools to the gang.

The Gentlemen gang's model lowers the entry barrier for affiliates, providing them with a ready-to-use way to disable defenses. Understanding how GentleKiller operates gives defenders a basis for spotting current builds and future variants. The gang's wide reach, targeting countries beyond the United States, including Southeast Asia, South America, and Western Europe, makes it a significant threat. Defenders must be aware of the gang's tactics and techniques to effectively protect against their attacks. By recognizing the shared vendor disguises and evasion layer, defenders can improve their chances of detecting and mitigating GentleKiller attacks.

---

> *We all have problems. The way we solve them is what makes us different.*

Source: [GentleKiller targets more than 400 security processes across 48 products](https://www.helpnetsecurity.com/2026/06/18/eset-gentlemen-edr-killers/)
