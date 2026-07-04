---
title: "Non-interactive SSH attacks dominate after login"
date: 2026-07-03T05:30:42+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers at the Czech Technical University in Prague conducted a study using eleven SSH honeypots to analyze the behavior of attackers after they gain access to a server. The honeypots, which ran for 15 days, logged 177,622 authenticated sessions, with 99.23% of the sessions being non-interactive, meaning the attacker logged in, ran a single command, and then disconnected. This type of attack is typically used for reconnaissance, with the most common commands gathering basic information about the machine, such as the operating system and kernel.

The study found that the majority of the traffic was reconnaissance, with the top 10 non-interactive commands accounting for 41.59% of the traffic. Some scanners also tested whether the honeypot was a real system or a trap, by sending commands that checked for basic system functionality. The researchers compared their findings to an independent dataset from CZ.NIC, which showed similar results, with 92.67% of sessions carrying exactly one command. This suggests that the pattern of non-interactive attacks is widespread and not specific to the researchers' honeypots.

The study's findings have implications for the design and evaluation of honeypots. Many honeypots measure success by engagement, counting how long an attacker stays and how many commands they run. However, this approach may not be effective for detecting non-interactive attacks, which are typically short-lived and involve only a single command. The researchers suggest that honeypots should be designed to recognize and group non-interactive attacks into campaigns, rather than focusing on individual sessions. This approach could help to better understand the behavior of attackers and improve the effectiveness of honeypots in detecting and preventing attacks.

---

> *There are basically two types of people. People who accomplish things, and people who claim to have accomplished things. The first group is less crowded.
Author: Mark Twain*

Source: [Non-interactive SSH attacks dominate after login](https://www.helpnetsecurity.com/2026/07/03/research-non-interactive-ssh-attacks/)
