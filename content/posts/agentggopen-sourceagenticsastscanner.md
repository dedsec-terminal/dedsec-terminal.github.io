---
title: "AgentGG: Open-source agentic SAST scanner"
date: 2026-06-05T06:00:29+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Introduction to AgentGG**
AgentGG is an open-source, agentic Static Application Security Testing (SAST) scanner that uses AI agents to analyze source code and identify potential security issues. Unlike traditional SAST tools, AgentGG's agents read the code, follow imports, and walk the call graph to confirm findings before reporting them. The project is released under the Apache 2.0 license and is available for free on GitHub.

**How AgentGG Works**
Each agent in AgentGG is a self-contained markdown file with YAML frontmatter that declares a precondition, target file patterns, and instructions. The tool comes with over 100 official agents and can be installed via npm. The scan process involves a fast recon pass, followed by parallel agent runs, and an optional validation pass that analyzes the code behind each finding. The tool also includes a scoring pass that attaches a CVSS severity score to each finding. AgentGG can be integrated with various providers, including Anthropic, OpenAI, and Google Vertex AI, and includes a state directory for resuming interrupted scans.

**Features and Benefits**
AgentGG offers several features that set it apart from other SAST tools, including a manual review process for its official agent catalog, a custom directory for user-installed agents, and an optional validation phase that can label findings as confirmed, false-positive, or uncertain. The tool has been benchmarked against other SAST tools, such as deepsec, and has shown promising results, including a 10-20% reduction in false positives. Overall, AgentGG provides a powerful and flexible SAST solution that can help organizations identify and address security vulnerabilities in their codebases.

---

> *Go to your bosom: Knock there, and ask your heart what it doth know.
Author: William Shakespeare*

Source: [AgentGG: Open-source agentic SAST scanner](https://www.helpnetsecurity.com/2026/06/05/agentgg-open-source-agentic-sast-scanner/)
