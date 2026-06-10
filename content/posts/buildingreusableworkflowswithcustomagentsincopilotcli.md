---
title: "Building reusable workflows with custom agents in Copilot CLI"
date: 2026-06-10T11:34:59+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Developers often spend a significant amount of time in the terminal, performing repetitive tasks such as running commands, debugging issues, and translating logs. To address this, GitHub Copilot CLI introduces custom agents, which can turn repeated tasks into reusable workflows. Custom agents are defined using Markdown files, allowing developers to describe how the agent should operate, what tools it can use, and what outputs it should produce.

Custom agents rely on agent profiles, which are files written in Markdown with YAML frontmatter that specify the agent's role, area of expertise, and tools it can access. These profiles live in the repository, allowing teams to review, version, and share them. To set up an agent in the CLI, developers can run Copilot CLI, use the /agent slash command, and select the agent, which will then execute the same steps every time. This enables teams to automate various workflow patterns, such as security audits, infrastructure as code compliance, and release documentation.

GitHub offers both off-the-shelf and custom agent options. Off-the-shelf agents are built with partners and cover areas such as observability, infrastructure as code, and security. Custom agents, on the other hand, allow teams to define their own workflows and tool-specific knowledge, and version them like code. To get started, developers can install GitHub Copilot CLI and begin with a task that their team repeats regularly, turning it into an agent that runs the same checks and produces the same reviewable output. A growing set of partner-built agents is also available for teams to test and define their own custom agents.

---

> *It is impossible for a man to learn what he thinks he already knows.
Author: Epictetus*

Source: [Building reusable workflows with custom agents in Copilot CLI](https://www.helpnetsecurity.com/2026/06/10/uilding-reusable-workflows-copilot-cli-custom-agents/)
