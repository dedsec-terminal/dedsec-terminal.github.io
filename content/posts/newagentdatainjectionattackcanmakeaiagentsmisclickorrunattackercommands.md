---
title: "New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands"
date: 2026-07-16T11:32:28+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers from Seoul National University, the University of Illinois Urbana-Champaign, and Largosoft have discovered a new class of attack called Agent Data Injection (ADI). This attack corrupts the facts that AI agents trust, allowing attackers to manipulate the agent's actions without hijacking its task. ADI works by injecting fake data into the agent's trusted sources, such as a sender's name or a button's ID, which can cause the agent to perform unintended actions, such as clicking "Buy Now" instead of "Read More" or running a malicious command on a developer's machine.

The researchers found that ADI is effective against various AI agents, including web agents and coding assistants. They built three working attacks on real tools, demonstrating the vulnerability of these agents to ADI. The attacks use a technique called probabilistic delimiter injection, which involves sprinkling punctuation-like characters into a field to trick the model into reading them as real structure. The researchers tested the attacks on several models, including OpenAI's GPT-5.2 and GPT-5-mini, Anthropic's Claude Opus 4.5 and Sonnet 4.5, and Google's Gemini 3 Pro and Flash, and found that ADI worked on structured data 31% to 43% of the time and on webpage data anywhere from a third of attempts to all of them.

The researchers suggest that to prevent ADI attacks, agents need to draw a clear line between trusted and untrusted data. One possible defense is to add a short random tag to field names, which can roughly halve the success rate of ADI attacks. Another defense is to track the origin of every piece of data, which can completely prevent ADI attacks but may also limit the agent's functionality. The researchers have reported their findings to the affected vendors and are releasing their benchmark and attack code to help vendors and defenders test against ADI.

---

> *Nothing is softer or more flexible than water, yet nothing can resist it.
Author: Lao Tzu*

Source: [New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands](https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html)
