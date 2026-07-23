---
title: "Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents"
date: 2026-07-22T04:57:52+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

A security flaw has been discovered in Microsoft's Azure DevOps MCP server, which allows an attacker to hijack a reviewer's AI coding agent using a hidden comment in a pull request. The comment, written in HTML, is invisible to human reviewers but can be read by the AI agent, allowing it to access projects and data that the attacker would not normally have access to. This can lead to the leakage of sensitive information, including source code and secrets.

The flaw works because the Azure DevOps server does not apply a prompt-injection guardrail to pull request descriptions, allowing an attacker to inject malicious instructions that the AI agent will follow. The agent, which is designed to assist reviewers with tasks such as code review, is given the reviewer's credentials and can therefore access projects and data that the reviewer has access to. The attacker can use this to gain access to sensitive information, even if they do not have the necessary permissions.

The security firm Manifold, which discovered the flaw, has demonstrated how it can be exploited using a proof-of-concept attack. Microsoft has acknowledged the issue, stating that it is a known class of AI risk, but has not yet released a fix or assigned a CVE. To mitigate the risk, Microsoft recommends that customers limit project access and review proposed changes before asking an AI tool to act on them. However, the fact that the payload is invisible in the interface a human reviews makes it difficult to detect. Manifold recommends that customers take additional steps, such as giving the agent least-privilege tokens and scoping it to the project under review, to prevent exploitation of the flaw.

---

> *If you can dream it, you can do it.
Author: Walt Disney*

Source: [Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents](https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html)
