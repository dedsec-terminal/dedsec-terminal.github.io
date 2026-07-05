---
title: "OpenClaw: risks for the users and how to mitigate them"
date: 2026-07-01T06:42:48+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

**Introduction to OpenClaw and Its Risks**
OpenClaw, a fast-growing ecosystem for AI agents, has gained popularity worldwide due to its flexibility and ability to automate complex tasks. However, its widespread adoption has also introduced risks to users and their employers. The system's architecture allows for the use of skills, which can be obtained from external sources, making it vulnerable to attacks. With over 530 vulnerabilities discovered in less than two years, it is essential to examine the security aspects of OpenClaw and mitigate potential risks.

**Vulnerabilities and Malicious Skills**
The majority of the discovered vulnerabilities are high-severity and involve issues with storing sensitive data and operating with excessive privileges. Malicious skills, which can be easily created and distributed, pose a significant threat to OpenClaw users. Research has drawn parallels between supply-chain attacks and the distribution of malicious skills, with over 1100 malicious accounts created since January. To mitigate these risks, it is crucial to employ layered protection, isolate the OpenClaw agent from critical data and infrastructure systems, and monitor network accesses used by the agent.

**Mitigating Risks and Best Practices**
To protect against OpenClaw-related risks, users should implement measures such as preliminary scanning of skills with VirusTotal and NVIDIA's SkillSpector, as well as monitoring malicious OpenClaw skill activity on the system. Kaspersky products can detect malicious skills and monitor client behavior. Additionally, users should develop a comprehensive AI policy, ensure employees only use authorized tools, and utilize solutions like Kaspersky Scan Engine to protect web applications and network attached storage. By taking these steps, users can minimize the risks associated with OpenClaw and ensure a secure environment for AI agent automation.

---

> *Never idealize others. They will never live up to your expectations.
Author: Leo Buscaglia*

Source: [OpenClaw: risks for the users and how to mitigate them](https://securelist.com/openclaw-security/120484/)
