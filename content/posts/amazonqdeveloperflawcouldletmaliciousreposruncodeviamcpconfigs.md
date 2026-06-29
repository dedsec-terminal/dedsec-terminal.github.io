---
title: "Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs"
date: 2026-06-26T13:53:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A high-severity flaw, tracked as CVE-2026-12957, was discovered in Amazon Q Developer, allowing a malicious repository to run commands and steal a developer's cloud credentials. The bug was found in how Amazon's AI coding assistant handled Model Context Protocol (MCP) servers. By dropping a single configuration file in a repository, an attacker could compromise a developer's cloud account, gaining access to sensitive information such as AWS keys, cloud CLI tokens, and API secrets.

The attack worked by exploiting the way Amazon Q read an MCP configuration file from an open workspace and launched the servers it defined. These servers inherited the developer's full environment, allowing an attacker to run arbitrary code with the developer's live cloud session attached. The vulnerability was patched by Amazon, with the fix closing the gap in consent for MCP servers. The patch, included in Language Servers for AWS 1.65.0, flags untrusted MCP servers and allows developers to reject the command before it runs.

To protect against this vulnerability, developers should update their Language Servers for AWS to version 1.69.0 or later. The patched plugin minimums vary by IDE, with VS Code requiring version 2.20 or later, JetBrains requiring version 4.3 or later, Eclipse requiring version 2.7.4 or later, and Visual Studio toolkit requiring version 1.94.0.0 or later. There is no known public exploitation of this vulnerability, and the fix was coordinated with Amazon, highlighting the importance of responsible disclosure and patching in preventing attacks. This vulnerability is part of a larger pattern of coding assistants tripping over MCP trust, emphasizing the need for explicit consent and trust checks when handling project configuration files.

---

> *No alibi will save you from accepting the responsibility.
Author: Napoleon Hill*

Source: [Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs](https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html)
