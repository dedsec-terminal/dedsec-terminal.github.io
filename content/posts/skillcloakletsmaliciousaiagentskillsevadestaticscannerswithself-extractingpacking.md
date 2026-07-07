---
title: "SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing"
date: 2026-07-06T06:33:56+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Researchers at the Hong Kong University of Science and Technology have discovered that malicious AI coding agent "skills" can evade detection by static scanners using simple techniques. These skills are small packages of files that can be loaded by AI agents to gain new capabilities, but they can also be used to steal credentials, copy source code, or install backdoors. The researchers' tool, SKILLCLOAK, can rewrite a malicious skill to look clean while still behaving maliciously, using techniques such as rewriting giveaway bytes or moving the payload into a directory that scanners skip.

The researchers tested SKILLCLOAK against eight scanners and found that it could evade detection more than 90% of the time. They also proposed a new approach to detecting malicious skills, called SKILLDETONATE, which runs the skill in a sandbox and watches its behavior at the operating-system level. This approach caught 97% of attacks in a controlled test and 87% of real-world malicious skills. The researchers argue that static scanning is not enough to detect malicious skills and that a more effective approach is to watch the skill's behavior at runtime.

The researchers' findings have significant implications for teams using coding agents, as they highlight the limitations of static scanning and the need for more robust defenses. The paper offers concrete stopgaps, such as hashing a skill when it is scanned and re-checking before each run, and flagging skills that ship opaque blobs in ignored folders or pad files past a size cap. However, the researchers emphasize that the durable defense is watching behavior at runtime and taking steps to limit the damage that a malicious skill can cause, such as installing only from vetted sources, giving agents the least access they need, and not running them on machines that hold sensitive information.

---

> *Better than a thousand hollow words, is one word that brings peace.
Author: Buddha*

Source: [SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html)
