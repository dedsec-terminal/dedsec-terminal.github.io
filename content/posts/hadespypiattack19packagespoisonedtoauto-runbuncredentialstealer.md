---
title: "Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer"
date: 2026-06-09T09:13:32+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

**Hades PyPI Attack Overview**
A recent attack, known as Hades, has compromised 19 packages in the Python Package Index (PyPI) registry, affecting 37 malicious wheel artifacts. The attack is part of the Miasma supply chain campaign, which has been refined and splintered to target specific ecosystems. The compromised packages include bramin, cmd2func, coolbox, and others, which have been poisoned with a malicious payload that downloads and runs the Bun JavaScript runtime, harvesting developer credentials and secrets.

**Malicious Payload and Attack Vector**
The malicious payload is executed automatically during Python startup, using a *-setup.pth file that is processed by Python's "site" module. The payload downloads and runs the Bun JavaScript runtime, which launches a heavily obfuscated JavaScript stealer that can harvest a wide range of data, including secrets associated with GitHub, npm, PyPI, and other platforms. The attack also employs a novel artificial intelligence (AI) defense evasion technique, using plain-text prompt injection to deceive Large Language Model (LLM)-based package analysis tools.

**Impact and Mitigation**
The Hades attack has significant implications for software supply chain security, highlighting the need for vigilance and robust security measures. The attack can replicate and spread laterally across developer networks, targeting GitHub repositories and extracting organization secrets. To mitigate the attack, developers should be cautious when installing packages from PyPI and ensure that their systems and dependencies are up-to-date. Additionally, security researchers recommend using tools like ruff, a Python code formatter, to detect and prevent malicious code injections. The Hades campaign underscores the importance of securing the software supply chain and protecting against sophisticated attacks that can compromise even trusted package channels.

---

> *Meaning is not what you start with but what you end up with.
Author: Peter Elbow*

Source: [Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)
