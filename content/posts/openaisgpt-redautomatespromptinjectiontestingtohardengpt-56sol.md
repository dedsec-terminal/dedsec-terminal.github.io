---
title: "OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol"
date: 2026-07-16T08:42:31+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

OpenAI has developed an internal automated red-teaming model called GPT-Red, designed to scale prompt injection vulnerability discovery and harden its GPT-5.6 Sol model. GPT-Red works like a human red-teamer, sending prompts and iterating towards malicious goals, such as uploading sensitive data to an external server. The model aims to identify new failure modes, improve robustness, and build countermeasures before the models are deployed.

GPT-Red has been integrated into the training process of OpenAI's production models, resulting in GPT-5.6 Sol being the most robust model to prompt injections to date. The model has achieved a 6x reduction in failures against direct prompt injection benchmarks compared to its previous model, GPT-5.5. GPT-Red has also been used to test various scenarios, including internal directory exfiltration, fraudulent payment instructions, and disabling two-factor authentication. The model is trained using self-play reinforcement learning, where it is rewarded for eliciting valid failures, while defender models are rewarded for resisting attacks.

The development of GPT-Red has led to significant improvements in the robustness of OpenAI's models. In real-world tests, GPT-Red has successfully attacked AI-based systems, including an autonomous vending machine and a Codex command-line agent. However, the model's capabilities are kept separate from other models to prevent malicious actors from exploiting them. OpenAI has also emphasized the importance of robustness and security in its models, particularly in the face of increasing threats from adversarial prompt injections. The company has also retracted its recommendation to use the SWE-Bench Pro benchmark due to issues with the dataset, highlighting the need for reliable and trustworthy benchmarks to evaluate model capabilities.

---

> *Fear not for the future, weep not for the past.
Author: Percy Shelley*

Source: [OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol](https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html)
