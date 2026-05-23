---
title: "ZDI-26-319: Progress Software Kemp LoadMaster addcountry Command Injection Remote Code Execution Vulnerability"
date: 2026-05-21T05:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A recently discovered vulnerability, identified as ZDI-26-319, affects Progress Software Kemp LoadMaster installations, allowing remote attackers to execute arbitrary code. To exploit this vulnerability, authentication is required, indicating that attackers must have valid credentials to gain access to the system. This limitation somewhat reduces the risk, as it is not a straightforward, unauthenticated attack.

The vulnerability is specifically related to the handling of the customLocation parameter, where user-supplied input is not properly validated before being used to execute a system call. This lack of validation creates an opportunity for attackers to inject malicious commands, ultimately leading to remote code execution. The ability to execute code in the context of the appliance poses significant risks, as it can lead to unauthorized access, data breaches, and other malicious activities.

The fact that authentication is required to exploit this vulnerability suggests that the primary concern is insider threats or attackers who have already gained access to the system through other means. Nevertheless, it is essential for organizations using Progress Software Kemp LoadMaster to address this vulnerability promptly to prevent potential attacks. By applying the necessary patches or updates, organizations can mitigate the risk of remote code execution and protect their systems from malicious activities.

Organizations should prioritize patch management and ensure that their systems are up-to-date with the latest security fixes. Additionally, implementing robust security measures, such as input validation and secure coding practices, can help prevent similar vulnerabilities from arising in the future. By taking proactive steps to address this vulnerability and improve overall security posture, organizations can reduce the risk of cyber attacks and protect their sensitive data and systems.

---

> *Meditation brings wisdom; lack of mediation leaves ignorance. Know well what leads you forward and what hold you back, and choose the path that leads to wisdom.
Author: Buddha*

Source: [ZDI-26-319: Progress Software Kemp LoadMaster addcountry Command Injection Remote Code Execution Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-319/)
