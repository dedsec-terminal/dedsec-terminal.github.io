---
title: "ZDI-26-296: Delta Electronics ASDA-Soft PAR File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability"
date: 2026-04-23T05:00:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A recently discovered vulnerability, identified as ZDI-26-296, affects Delta Electronics ASDA-Soft installations, allowing remote attackers to execute arbitrary code. This vulnerability requires user interaction, meaning the target must either visit a malicious webpage or open a malicious file to be exploited. The vulnerability is triggered when the user performs one of these actions, enabling the attacker to gain control over the system.

The specific flaw exists in the parsing of PAR files, which is a critical component of the ASDA-Soft software. The issue arises from the lack of proper validation of user-supplied data, specifically the length of the data, prior to copying it to a stack-based buffer. This oversight allows an attacker to manipulate the data and overflow the buffer, potentially leading to remote code execution. As a result, an attacker can leverage this vulnerability to execute malicious code in the context of the current process.

The implications of this vulnerability are significant, as it can be exploited by remote attackers to gain control over affected systems. The fact that user interaction is required to exploit the vulnerability does not diminish its severity, as attackers can use social engineering tactics to trick users into visiting malicious webpages or opening malicious files. To mitigate this vulnerability, it is essential for users to exercise caution when interacting with unfamiliar webpages or files and for administrators to apply patches or updates as soon as they become available.

The vulnerability can be exploited by attackers to gain unauthorized access to sensitive data, disrupt system operations, or install malware. As a result, it is crucial for organizations using Delta Electronics ASDA-Soft to take immediate action to address this vulnerability. By applying the necessary patches or updates, organizations can prevent remote attackers from exploiting this vulnerability and reduce the risk of a successful attack.

---

> *We cannot change our memories, but we can change their meaning and the power they have over us.
Author: David Seamans*

Source: [ZDI-26-296: Delta Electronics ASDA-Soft PAR File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-296/)
