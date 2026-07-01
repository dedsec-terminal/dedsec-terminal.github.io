---
title: "Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data"
date: 2026-06-30T17:46:07+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Introduction to the Threat**
Microsoft has warned of a potential security threat where attackers can hijack AI agents using poisoned tool descriptions, allowing them to leak company data without triggering alarms. This vulnerability exists because AI agents, which can perform tasks on behalf of users, rely on tool descriptions to determine their actions. These descriptions can be manipulated by attackers to include hidden instructions, enabling them to access sensitive data.

**How the Attack Works**
The attack exploits the Model Context Protocol (MCP), an open protocol that allows AI agents to call external tools. Each MCP tool comes with a description that the agent reads to decide how to act. Attackers can update these descriptions to include malicious instructions, which the agent will then follow. For example, an attacker could modify a tool's description to collect and send sensitive invoices to an external server. Since the agent's actions appear legitimate, the attack may go undetected. This vulnerability highlights the need for companies to carefully review and monitor the tools and descriptions used by their AI agents.

**Mitigation and Defense**
To defend against these attacks, Microsoft recommends treating connected tools as part of the supply chain and implementing strict controls. This includes reviewing tool descriptions like code changes, limiting agent access to specific tools, and requiring human approval for high-risk actions. Additionally, companies should monitor agent activity, set baselines for normal behavior, and flag suspicious actions. By applying these principles, companies can reduce the risk of AI agent hijacking and protect their sensitive data. Microsoft's own products, such as Prompt Shields and Defender for Cloud, can also be used to implement these security measures.

---

> *As we risk ourselves, we grow. Each new experience is a risk.
Author: Fran Watson*

Source: [Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data](https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html)
