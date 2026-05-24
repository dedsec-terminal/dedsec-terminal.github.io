---
title: "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence"
date: 2026-05-15T13:35:04+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have identified four security flaws in OpenClaw, collectively known as the Claw Chain, which can be exploited to achieve data theft, privilege escalation, and persistence. The vulnerabilities, tracked as CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, and CVE-2026-44118, have CVSS scores ranging from 7.7 to 9.6, indicating a high level of severity. These flaws can be chained together to allow an attacker to establish a foothold, expose sensitive data, and plant backdoors, ultimately gaining persistent control over the compromised host.

The vulnerabilities include time-of-check/time-of-use (TOCTOU) race condition flaws in the OpenShell managed sandbox backend, which can be exploited to bypass sandbox restrictions and redirect writes or read files outside the intended mount root. Additionally, an incomplete list of disallowed inputs vulnerability can be used to bypass allowlist validation, while an improper access control vulnerability can allow non-owner loopback clients to impersonate an owner and elevate their privileges. Successful exploitation of these flaws can enable an attacker to tamper with configuration, plant backdoors, and establish persistent control over the compromised host.

The exploitation chain involves four steps, starting with gaining code execution inside the OpenShell sandbox through a malicious plugin, prompt injection, or compromised external input. The attacker can then leverage the vulnerabilities to expose credentials, secrets, and sensitive files, obtain owner-level control of the agent runtime, and finally plant backdoors or make configuration changes to set up persistence. The root cause of one of the vulnerabilities stems from the fact that OpenClaw trusts a client-controlled ownership flag without validating it against the authenticated session.

The vulnerabilities have been addressed in OpenClaw version 2026.4.22, following responsible disclosure. Users are advised to update to the latest version to stay protected against potential threats. The cybersecurity company, Cyera, warns that by exploiting these vulnerabilities, an adversary can move through data access, privilege escalation, and persistence, using the agent as their hands inside the environment, making detection significantly harder. The discovery and reporting of these issues are credited to security researcher Vladimir Tokarev.

---

> *The one who always loses, is the only person who gets the reward.
Author: Claire Charmont*

Source: [Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)
