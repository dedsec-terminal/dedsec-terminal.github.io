---
title: "Patch Tuesday, May 2026 Edition"
date: 2026-05-20
draft: false
categories:
  - threat-intelligence
author: "DedSec-Terminal"
---

Artificial intelligence platforms may be just as susceptible to social engineering as human beings, but they are proving remarkably good at finding security vulnerabilities in human-made computer code. That reality is on full display this month with some of the more widely-used software makers — including Apple, Google, Microsoft, Mozilla and Oracle — fixing near record volumes of security bugs, and/or quickening the tempo of their patch releases.

As it does on the second Tuesday of every month, Microsoft today released software updates to address at least 118 security vulnerabilities in its various Windows operating systems and other products. Remarkably, this is the first Patch Tuesday in nearly two years that Microsoft is not shipping any fixes to deal with emergency zero-day flaws that are already being exploited. Nor have any of the flaws fixed today been previously disclosed (potentially giving attackers a heads up in how to exploit the weakness).

Sixteen of the vulnerabilities earned Microsoft’s most-dire “critical” label, meaning malware or miscreants could abuse these bugs to seize remote control over a vulnerable Windows device with little or no help from the user. Rapid7 has done much of the heavy lifting in identifying some of the more concerning critical weaknesses this month, including:

- CVE-2026-41089: A critical stack-based buffer overflow in Windows Netlogon that offers an attacker SYSTEM privileges on the domain controller. No privileges or user interaction are required, and attack complexity is low. Patches are available for all versions of Windows Server from 2012 onwards.

- CVE-2026-41096: A critical RCE in the Windows DNS client implementation worthy of attention despite Microsoft assessing exploitation as less likely.

- CVE-2026-41103: A critical elevation of privilege vulnerability that allows an unauthorized attacker to impersonate an existing user by presenting forged credentials, thus bypassing Entra ID. Microsoft expects that exploitation is more likely.

*Trust arrives on foot and leaves on horseback. — Dutch proverb*

Source: [Krebs on Security](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/) · [Read Original →](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/)
