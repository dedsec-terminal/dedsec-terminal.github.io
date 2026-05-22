---
title: "Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer"
date: 2026-05-19T07:49:23+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Cybersecurity researchers have flagged a compromised version of the Nx Console extension that was published to the Microsoft Visual Studio Code (VS Code) Marketplace.
The extension in question is rwl.angular-console (version 18.95.0), a popular user interface and plugin for code editors like VS Code, Cursor, and JetBrains. The VS Code extension has more than 2.2 million installations. The Open VSX version has not been affected by the incident.
"Within seconds of a developer opening any workspace, the compromised extension silently fetched and executed a 498 KB obfuscated payload from a dangling orphan commit hidden inside the official nrwl/nx GitHub repository," StepSecurity researcher Ashish Kurmi said.
The payload is a "multi-stage credential stealer and supply chain poisoning tool" that harvests developer secrets and exfiltrates them via HTTPS, the GitHub API, and DNS tunneling. It also installs a Python backdoor on macOS systems that abuses the GitHub Search API as a dead drop resolver for receiving further commands.
In an advisory issued Monday, the maintainers of the extension said the root cause has been traced to one of its developers, whose machine was compromised in a rec

---

> *The smallest act of kindness is worth more than the grandest intention.
Author: Oscar Wilde*

Source: [Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html)
