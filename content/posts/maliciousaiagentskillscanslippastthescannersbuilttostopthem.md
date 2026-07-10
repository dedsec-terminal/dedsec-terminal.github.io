---
title: "Malicious AI agent skills can slip past the scanners built to stop them"
date: 2026-07-09T06:00:33+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

The rise of AI coding agents has led to the creation of marketplaces where developers can download and install "agent skills" - bundles of instructions, scripts, and files that give these agents new capabilities. However, this convenience comes with a significant security risk, as malicious skills can be created and distributed, potentially allowing attackers to steal credentials, source code, or install backdoors. In fact, a campaign called ClawHavoc has already planted over 300 malicious skills on a single marketplace, highlighting the need for effective defense mechanisms.

Current defense mechanisms, such as skill scanners, rely on checking the contents of a skill bundle at install time and blocking or allowing it based on certain rules or language models. However, researchers at the Hong Kong University of Science and Technology have found that these scanners can be easily evaded by malicious skills that use techniques such as rewriting suspicious code or hiding payloads in directories that scanners skip. In experiments, the researchers found that their evasion techniques could bypass scanners over 90% of the time, highlighting the limitations of current defense mechanisms.

To address these limitations, the researchers have developed a new tool called SkillDetonate, which runs suspicious skills in a sandbox and monitors their behavior at the operating-system boundary. This approach has shown promising results, catching 97% of attacks in synthetic benchmarks and 87% of real-world malicious skills, even when they use evasion techniques. While SkillDetonate has its own limitations, such as requiring more time to analyze skills and potentially missing payloads that are not executed, it represents a significant step forward in defending against malicious AI agent skills. The researchers' work highlights the need for a behavioral approach to security, where the focus is on monitoring and analyzing the behavior of code, rather than just inspecting its contents.

---

> *Winners have simply formed the habit of doing things losers don't like to do.
Author: Albert Gray*

Source: [Malicious AI agent skills can slip past the scanners built to stop them](https://www.helpnetsecurity.com/2026/07/09/malicious-ai-agent-skills-scan/)
