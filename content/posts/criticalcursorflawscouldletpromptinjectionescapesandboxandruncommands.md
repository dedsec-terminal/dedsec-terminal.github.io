---
title: "Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands"
date: 2026-07-01T14:42:54+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

**Critical Vulnerabilities in Cursor AI Code Editor**
Two critical flaws, known as DuneSlide, have been discovered in the Cursor AI code editor, which could allow an attacker to break out of the editor's safety sandbox and run any command on a developer's computer. The vulnerabilities, tracked as CVE-2026-50548 and CVE-2026-50549, are rated 9.8 out of 10 and can be exploited through a single, ordinary-looking prompt. This means that no user interaction, such as a click or approval, is required for the attack to succeed.

**How the Vulnerabilities Work**
The vulnerabilities exploit the way Cursor's AI agent reads and executes instructions from connected services or web searches. An attacker can plant malicious instructions in a prompt, which can then be executed by the agent without the user's knowledge or consent. The vulnerabilities, CVE-2026-50548 and CVE-2026-50549, use similar techniques to escape the sandbox by writing to a file that should not be allowed, and then using that write to disable the sandbox. This allows subsequent commands to run with full privileges, giving the attacker control of the developer's machine and any connected cloud or SaaS workspaces.

**Fix and Implications**
The vulnerabilities have been patched in Cursor 3.0, released on April 2, and all previous versions are affected. Users are advised to update to the latest version as soon as possible. The discovery of DuneSlide is the latest in a series of vulnerabilities found in Cursor, which have all started with a poisoned prompt and ended in code execution. This highlights the need for coding agents to treat every input as hostile and to prioritize security in their design. The vulnerabilities also raise questions about the structural security of coding agents and whether a more comprehensive approach is needed to prevent similar vulnerabilities in the future.

---

> *Sometimes the most important thing in a whole day is the rest we take between two deep breaths.
Author: Etty Hillesum*

Source: [Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands](https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html)
