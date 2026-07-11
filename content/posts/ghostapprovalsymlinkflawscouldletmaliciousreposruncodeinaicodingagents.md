---
title: "GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents"
date: 2026-07-09T04:27:18+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Researchers at Wiz have discovered a flaw in six popular AI coding assistants, including Amazon Q Developer, Anthropic's Claude Code, and Google Antigravity, which could allow a malicious repository to take control of a developer's computer. The flaw, dubbed "GhostApproval," exploits an old Unix feature called a symbolic link (symlink) that the assistants fail to check. This allows a malicious repository to trick the assistant into writing to a sensitive file, such as the SSH login file or shell startup file, by creating a symlink that points to the target file.

The attack works by creating a malicious repository with a symlink that points to a sensitive file. When the assistant is asked to edit the symlink, it writes to the target file instead, allowing the attacker to gain access to the developer's computer. The approval box shown to the developer lies about the destination of the write, making it appear as though the assistant is editing a harmless file. This "informed-consent bypass" allows the attacker to gain access to the developer's computer without their knowledge or consent. Three of the six affected tools have shipped fixes, while two have not, and Anthropic disputes that it is a bug.

To mitigate the risk of this attack, developers can take several precautions, including running the agent with limited file access, using a sandbox or container, and carefully reviewing a repository's README and hidden config files before allowing an agent to "set it up." Additionally, developers can check the files targeted by the attack, such as shell startup files and SSH keys, for any changes after working in an unfamiliar repository. Wiz advises tool makers to resolve the symlink and show the real destination before asking for approval, flag any write that lands outside the project folder, and never touch the disk until the user has actually approved.

---

> *It is more important to know where you are going than to get there quickly. Do not mistake activity for achievement.
Author: Mabel Newcomber*

Source: [GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents](https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html)
