---
title: "AI agents tricked into recommending malicious GitHub repositories"
date: 2026-07-21T14:27:38+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Researchers at Island have uncovered a large-scale operation, dubbed "FakeGit," where approximately 7,600 malicious GitHub repositories were created to trick AI agents into recommending them. These repositories, tied to around 6,600 accounts, pose as legitimate AI Skills or Model Context Protocol (MCP) servers, but actually deliver malware called SmartLoader. This malware installs an information stealer called StealC, which targets credentials, active sessions, and other sensitive data.

The malicious repositories use various tactics to appear legitimate, including copied projects, lookalike developer profiles, and convincing READMEs. They have been successful in deceiving AI agents, such as Claude Code, Gemini, and ChatGPT, which have recommended these repositories to users. The AI agents are tricked into treating the attacker's README as legitimate documentation and passing along installation instructions to the user. This technique, called "AgentBaiting," targets the AI agent rather than the user, allowing the malware to spread more easily.

To protect themselves from this threat, enterprises are advised to build a catalog of reviewed Skills and MCP servers, test new capabilities in a sandboxed environment, and verify both the publisher and the project. Additionally, monitoring the paths agents use to download and install tools can help detect potential malware. If SmartLoader execution is suspected, isolating the endpoint and revoking active browser sessions, OAuth grants, API tokens, and cloud and developer credentials is recommended. Island has provided a list of affected repositories and file hashes to help organizations identify and mitigate the threat.

---

> *You give before you get.
Author: Napoleon Hill*

Source: [AI agents tricked into recommending malicious GitHub repositories](https://www.helpnetsecurity.com/2026/07/21/github-repos-malware-campaign-fakegit-ai-agents/)
