---
title: "ZDI-26-307: FlowiseAI Flowise Airtable_Agent Code Injection Remote Code Execution Vulnerability"
date: 2026-05-01T05:00:00+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A recently discovered vulnerability, tracked as ZDI-26-307, affects FlowiseAI Flowise installations, allowing remote attackers to execute arbitrary code without requiring authentication. This vulnerability poses a significant threat, as it enables attackers to gain control over the system and perform malicious actions.

The vulnerability is specifically located within the run method of the Airtable_Agents class. The issue arises from the lack of proper validation of user-supplied input, which is then used to execute Python code. This lack of validation creates an opportunity for attackers to inject malicious code, leading to remote code execution. As a result, an attacker can exploit this vulnerability to execute code in the context of the service account, potentially leading to further exploitation of the system.

The fact that authentication is not required to exploit this vulnerability makes it particularly concerning, as it allows attackers to launch attacks without needing to obtain login credentials. This highlights the importance of implementing proper input validation and secure coding practices to prevent such vulnerabilities. By addressing this issue, FlowiseAI can help prevent potential attacks and protect its users from the risks associated with remote code execution.

The vulnerability can be exploited by sending a specially crafted request to the affected system, which can then lead to the execution of arbitrary code. It is essential for users and administrators to be aware of this vulnerability and take necessary steps to mitigate its impact. This may involve applying patches or updates provided by FlowiseAI, as well as implementing additional security measures to prevent exploitation. By taking proactive steps, users can help protect themselves from the potential consequences of this vulnerability.

---

> *It has never been my object to record my dreams, just to realize them.
Author: Man Ray*

Source: [ZDI-26-307: FlowiseAI Flowise Airtable_Agent Code Injection Remote Code Execution Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-307/)
