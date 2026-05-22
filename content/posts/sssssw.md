---
title: "Four Malicious npm Packages Deliver Infostealers and Phantom Bot DDoS Malware"
date: 2026-05-18T08:57:26+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered four new npm packages containing information-stealing malware, one of which is a clone of the Shai-Hulud worm open-sourced by TeamPCP.
The list of identified packages is below -
- chalk-tempalte (825 Downloads)
- @deadcode09284814/axios-util (284 Downloads)
- axois-utils (963 Downloads)
- color-style-utils (934 Downloads)
"One of the packages (chalk-tempalte) contains a direct clone of the Shai-Hulud source code that TeamPCP leaked last week, probably inspired as part of the supply chain attack competition that was published in BreachForums not long after," OX Security's Moshe Siman Tov Bustan said.
Interestingly, the malicious payloads embedded into the four npm packages are different, despite them being published by the same npm user, "deadcode09284814." As of writing, the four libraries are still available for download from npm.
An analysis of the packages has revealed that "axois-utils" is designed to deliver a Golang-based distributed denial-of-service (DDoS) botnet called Phantom Bot, with capabilities to flood a target website using HTTP, TCP, and UDP protocols. It also establishes persistence on both Windows and Linux machines by ad

---

> *To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.
Author: Buddha*

Source: [Four Malicious npm Packages Deliver Infostealers and Phantom Bot DDoS Malware](https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html)
