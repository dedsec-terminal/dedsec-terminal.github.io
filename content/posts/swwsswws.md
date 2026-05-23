---
title: "ZDI-26-310: Microsoft Windows splwow64 Race Condition Local Privilege Escalation Vulnerability"
date: 2026-05-12T05:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A recently discovered vulnerability in Microsoft Windows, identified as ZDI-26-310, allows local attackers to escalate privileges on affected systems. To exploit this vulnerability, an attacker must first gain the ability to execute low-privileged code on the target system. This initial access is a necessary precursor to leveraging the vulnerability and gaining elevated privileges.

The vulnerability is specifically located within the splwow64.exe process, which is a component of the Windows Print Spooler service. The issue arises from the unsafe use of shared memory, which can be manipulated by an attacker to achieve privilege escalation. By exploiting this flaw, an attacker can transition from a low-integrity context to a medium-integrity context, allowing them to execute arbitrary code with elevated privileges.

The implications of this vulnerability are significant, as it allows an attacker to gain increased access to system resources and potentially carry out malicious activities. The fact that the vulnerability can be exploited by an attacker with low-privileged code execution capabilities makes it a notable concern. As with any local privilege escalation vulnerability, the potential for damage is closely tied to the attacker's initial level of access and their ability to leverage the vulnerability to achieve their goals.

The vulnerability highlights the importance of secure coding practices, particularly when working with shared memory and other sensitive system resources. Microsoft's response to the vulnerability will likely involve issuing a patch to address the issue and prevent exploitation. In the meantime, system administrators and users should be aware of the potential risks associated with this vulnerability and take steps to minimize their exposure, such as limiting access to sensitive systems and keeping software up to date.

---

> *Today is the tomorrow we worried about yesterday.*

Source: [ZDI-26-310: Microsoft Windows splwow64 Race Condition Local Privilege Escalation Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-310/)
