---
title: "New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email"
date: 2026-07-13T13:49:48+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers have discovered a new attack called MemGhost that can plant false memories in AI agents through a single email. The attack targets personal AI assistants that have access to a user's inbox and can write to their own memory files. By sending a specially crafted email, an attacker can trick the agent into saving a false "fact" about the user, which can then influence the agent's responses in later sessions. The attack is stealthy, and the user may never realize that their agent has been tampered with.

The researchers tested the MemGhost attack on several AI agents, including OpenClaw, and found that it was successful in 87.5% of cases. The attack works by using a trained generator to create an email that is designed to trick the agent into writing a false memory to its files. The email is crafted to be innocuous-looking, and the agent's response to the email does not reveal that it has been tampered with. The researchers also found that the attack can evade defenses such as input filters and model hardening, and that it can persist even after the email has been deleted.

The implications of the MemGhost attack are significant, as it highlights the vulnerability of AI agents to external manipulation. The researchers argue that the only way to prevent such attacks is to implement robust security measures, such as tagging the source of information, asking the user for approval before writing to memory, and logging every write. Until such measures are implemented, users of AI agents that read untrusted email and can write to their own memory are at risk of having their agents compromised. The researchers plan to disclose their findings to the makers of the affected agents and models, and to release a benchmark to help test the security of AI agents against such attacks.

---

> *The spirit, the will to win, and the will to excel, are the things that endure. These qualities are so much more important than the events that occur.
Author: Vincent Lombardi*

Source: [New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email](https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html)
