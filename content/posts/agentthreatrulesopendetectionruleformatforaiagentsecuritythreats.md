---
title: "Agent Threat Rules: Open detection rule format for AI agent security threats"
date: 2026-06-03T05:00:06+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Introduction to Agent Threat Rules**
Agent Threat Rules (ATR) is an open detection format designed to identify AI agent security threats. AI agents, which run inside coding assistants and multi-agent frameworks, can be vulnerable to attacks such as prompt injection, tool poisoning, and credential theft. ATR aims to address this category of attack with a standardized format for detecting and preventing these threats.

**ATR Format and Capabilities**
ATR rules are written in YAML and conform to a versioned schema, declaring the attack pattern, input field, and test cases. The project includes a reference engine in TypeScript and a Python wrapper, both available under the MIT license. With over 400 rules across categories such as prompt injection and context exfiltration, ATR has demonstrated benchmark recall rates ranging from 98.0% to 0.0% across various test corpora. The format draws inspiration from Sigma and YARA, established standards for SIEM detection and malware signatures.

**Adoption and Governance**
ATR has been adopted by several organizations, including Microsoft, Cisco, and Gen Digital, which have integrated the rules into their tooling. The project is available for free on GitHub, with adopters self-declaring through pull requests. ATR maps to external frameworks, covering 91.8% of SAFE-MCP techniques and 10 of 10 OWASP Agentic Top 10 categories. While ATR has shown promising results, its maintainer acknowledges the need for pairing with additional security measures, such as credential brokering and human review, to address coverage gaps and ensure effective threat detection.

---

> *Can you imagine what I would do if I could do all I can?
Author: Sun Tzu*

Source: [Agent Threat Rules: Open detection rule format for AI agent security threats](https://www.helpnetsecurity.com/2026/06/03/agent-threat-rules-ai-detection/)
