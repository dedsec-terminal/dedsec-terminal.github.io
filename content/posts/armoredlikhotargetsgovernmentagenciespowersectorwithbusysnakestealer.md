---
title: "Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer"
date: 2026-07-03T13:36:33+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A previously unknown threat actor, Armored Likho, has been linked to cyber attacks targeting government agencies and the power sector in Russia, Brazil, and Kazakhstan. The group's toolkit includes obfuscated, modular remote access trojans (RATs) and infostealers designed to bypass dynamic analysis. They use a variety of tools, such as Go2Tunnel for remote access and network tunneling, to maintain persistent access to compromised hosts, steal credentials and sensitive data, and deliver tailored modules to victims.

The attacks often begin with spear-phishing emails containing lures related to official government notices or social programs, which distribute a RAR archive with EXE binaries that serve as droppers for additional payloads. The dropper malware creates VBScript files to erase execution traces and launch the stealer, which is a Python-based information stealer called BusySnake. BusySnake implements evasion techniques to complicate static analysis and sidestep detection, and its primary goal is to establish communication with a command-and-control (C2) server and await incoming instructions.

Armored Likho is believed to have possible overlaps with a threat cluster known as Eagle Werewolf, which has been active since May 2023 and has targeted government and defense organizations. The group's toolkit has been refined to include a new task-management framework and integrated reverse-tunneling functionality. The use of artificial intelligence (AI) tools is also suspected, given the presence of redundant comments and code blocks in the first-stage payloads. The campaign highlights the growing technical maturity of Armored Likho and a shift toward more complex schemes aimed at bypassing security solutions.

---

> *You cannot travel the path until you have become the path itself.
Author: Buddha*

Source: [Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer](https://thehackernews.com/2026/07/armored-likho-targets-government.html)
