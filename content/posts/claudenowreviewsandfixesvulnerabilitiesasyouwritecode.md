---
title: "Claude now reviews and fixes vulnerabilities as you write code"
date: 2026-05-27T13:37:28+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Anthropic has introduced a security-guidance plugin for Claude Code, a tool that reviews code changes for common vulnerabilities and helps identify and fix issues during the development session. The plugin is designed to catch issues such as injection flaws, unsafe deserialization, and insecure DOM APIs before code reaches pull requests, reducing the amount of manual security review later in the development process. This plugin operates automatically during development sessions, without requiring developers to launch separate tools or remember additional commands.

The plugin operates through three review stages integrated into the coding workflow, targeting different categories of security issues. The first stage runs during file edits and performs lightweight pattern checks, looking for risky constructs and commonly abused libraries. The second stage activates after each model turn, analyzing the complete git diff to identify vulnerabilities that pattern matching may miss. The deepest review stage runs when Claude performs commits or pushes, reviewing surrounding files and code paths to validate findings and reduce false positives. Developers can also extend these review layers with custom rules and repository-specific security checks.

The plugin is free for all users and available on all plans, with instant security checks running without model calls and not adding usage costs. It requires Claude Code version 2.1.144 or later and Python 3.8 or newer, with deeper review stages working only inside git repositories. Anthropic has seen a 30-40% decrease in security-related comments on PRs opened using the plugin, indicating its effectiveness as a lightweight first pass in catching issues before a full code review. The company has been using the plugin internally and is now making it available to all users.

---

> *To live a pure unselfish life, one must count nothing as ones own in the midst of abundance.
Author: Buddha*

Source: [Claude now reviews and fixes vulnerabilities as you write code](https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/)
