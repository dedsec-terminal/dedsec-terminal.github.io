---
title: "ZDI-26-299: Docker Desktop Enhanced Container Isolation Exposed Dangerous Function Local Privilege Escalation Vulnerability"
date: 2026-04-23T05:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code within a container in order to exploit this vulnerability.
The specific flaw exists within the processing of Docker CLI arguments. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges to resources normally protected by Enhanced Container Isolation.
Fixed in Docker Desktop 4.59.0

---

> *However many holy words you read, however many you speak, what good will they do you if you do not act on upon them?
Author: Buddha*

Source: [ZDI-26-299: Docker Desktop Enhanced Container Isolation Exposed Dangerous Function Local Privilege Escalation Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-299/)
