---
title: "Armored Likho digging a snake pit: inside the covert BusySnake Stealer campaign"
date: 2026-07-03T10:00:33+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Researchers have uncovered a new phishing campaign tied to a previously unknown APT group dubbed Armored Likho, which targets government agencies and the electric power sector in Russia, Brazil, and Kazakhstan. The group's toolkit features obfuscated, modular RATs and infostealers designed to bypass dynamic analysis, as well as simpler tools like Go2Tunnel for remote access and network tunneling. This diverse malware stack enables the threat actor to maintain stealthy control of compromised hosts, exfiltrate credentials and other sensitive information, and dynamically deploy downloadable modules tailored to the victim's profile and tasks.

The campaign leverages a previously undocumented tool called BusySnake Stealer, a Python-based infostealer designed to target Windows systems. The malware is delivered through phishing emails with malicious attachments or links, which execute a loader that fetches and installs the stealer. The loader also installs dependencies, including a Python 3.12 interpreter and the pip package manager, and establishes persistence through a scheduled task. The BusySnake Stealer features multiple evasion techniques, including code obfuscation and encryption, to thwart detection and complicate static analysis.

The BusySnake Stealer's architecture relies on handlers responsible for specific functions, such as stealing data from the system clipboard, enumerating files, and capturing screenshots. The malware also communicates with a C2 server to receive commands and forward stolen data. The researchers were able to strip the protector and disassemble the executable functions, revealing the stealer's configuration and core functionality. The campaign highlights the growing technical maturity of Armored Likho and the use of tool polymorphism and complex schemes to bypass security solutions. The researchers note that the group is likely leveraging AI-generated code to create their malicious payloads, making attribution efforts more complicated.

---

> *It is only when the mind and character slumber that the dress can be seen.
Author: Ralph Waldo Emerson*

Source: [Armored Likho digging a snake pit: inside the covert BusySnake Stealer campaign](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/)
