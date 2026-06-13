---
title: "LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution"
date: 2026-06-12T09:50:36+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered three security flaws in LangGraph, an open-source framework for building artificial intelligence (AI) applications. The most critical vulnerability is a chain of flaws that could result in remote code execution, allowing attackers to gain full control of a server. This vulnerability chain is exploitable in self-hosted deployments using the SQLite or Redis checkpointer with user-controlled filter input.

The three identified vulnerabilities are: CVE-2025-67644, a SQL injection vulnerability in LangGraph's SQLite checkpoint implementation; CVE-2026-28277, an unsafe msgpack deserialization vulnerability; and CVE-2026-27022, a RediSearch Query Injection vulnerability. The vulnerability chain can be exploited by an attacker who can prepare a malicious msgpack payload, send a malicious filter parameter to exploit the SQL injection vulnerability, and then deserialize the malicious checkpoint's BLOB to execute arbitrary code.

To mitigate these vulnerabilities, users are advised to apply the latest fixes and implement security measures such as authentication for self-hosted LangGraph servers, network segmentation, and the principle of least privilege (PoLP) to limit the agent's access footprint. LangGraph's managed platform, LangSmith Deployment, is not affected by these vulnerabilities. The discovery of these flaws highlights the importance of securing AI agent frameworks, which can carry elevated access and trust, and the need to protect against classic vulnerability classes like SQL injection that can become more potent in these environments.

---

> *Let me tell you the secret that has led me to my goal: my strength lies solely in my tenacity
Author: Louis Pasteur*

Source: [LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)
