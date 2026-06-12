---
title: "New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets"
date: 2026-06-11T17:46:32+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Two separate security research teams, Imperva and Varonis, have discovered vulnerabilities in the OpenClaw AI agent that allow attackers to trick it into running malicious code or leaking sensitive data. Imperva found that OpenClaw can be exploited through hidden commands in shared contacts, vCards, or location pins, which can be used to download and run scripts from an attacker-controlled server. This flaw has been patched in OpenClaw version 2026.4.23.

Varonis, on the other hand, demonstrated that OpenClaw can be tricked into leaking sensitive data through social engineering tactics, such as phishing emails that pose as legitimate requests from colleagues. The researchers created a test agent and found that it could be convinced to forward mock AWS keys and customer data to an outside address. This vulnerability is not something that can be fixed with a patch, but rather requires limiting the agent's access and implementing controls to prevent it from acting on suspicious requests.

The underlying issue with OpenClaw is its trust in the input it receives, which allows attackers to exploit it. Both research teams recommend implementing controls such as treating the agent's instruction file as a version-controlled policy, requiring approval for outbound mail to unfamiliar addresses, and limiting the agent's access to sensitive data. Ultimately, the problem is that a useful AI agent is, by design, one that trusts input and wants to help, and a general fix for this issue has not yet been found.

---

> *Keeping a little ahead of conditions is one of the secrets of business, the trailer seldom goes far.
Author: Charles Schwab*

Source: [New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets](https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html)
