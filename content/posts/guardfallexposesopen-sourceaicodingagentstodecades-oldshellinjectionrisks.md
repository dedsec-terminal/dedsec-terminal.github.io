---
title: "GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks"
date: 2026-06-30T14:26:15+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers at Adversa AI have discovered a vulnerability, dubbed GuardFall, that affects ten out of eleven popular open-source AI coding agents. The flaw allows an attacker to bypass safety checks and execute malicious shell commands, potentially leading to data theft or destruction. This is possible because the agents check commands as plain text, while the bash shell rewrites the text before running it, allowing malicious commands to slip through.

The vulnerability is not a bug, but rather a "dangerous convention and a class of problems" that arises from the way the agents interact with the shell. To exploit this vulnerability, an attacker would need to produce a malicious command that is not caught by the agent's blocklist, and the agent would need to be running with elevated privileges. The researchers demonstrated the attack against several popular tools, including Plandex, and found that only one tool, "Continue", was able to defend against it.

To mitigate the risk, users can take several steps, including running agents with limited privileges, turning off auto-execute flags, and not allowing agents to run on untrusted code. The researchers also recommend re-implementing the defense mechanism used by "Continue", which breaks down commands into the same pieces as the shell and checks them against a hard list of destructive commands. This vulnerability is part of a larger trend of similar findings, highlighting the need for improved security measures in AI coding agents to prevent attacks that can compromise user data and systems.

---

> *Obstacles are those things you see when you take your eyes off the goal.
Author: Hannah More*

Source: [GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks](https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html)
