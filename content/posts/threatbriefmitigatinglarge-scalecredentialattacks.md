---
title: "Threat Brief: Mitigating Large-Scale Credential Attacks"
date: 2026-06-20T02:05:33+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Threat Brief Overview**
Unit 42 has identified a large-scale password spraying and credential theft campaign, known as "FortiBleed," targeting Fortinet devices, as well as MSSQL and Sophos devices. Although Palo Alto Networks devices are not directly targeted, the company is providing this report as a precaution to ensure customers have the latest intelligence and product recommendations to protect against these attacks. The threat actors are using a curated password list to attempt password spraying against services exposed to the internet.

**Threat Actor Tactics and Recommendations**
The threat actors are leveraging a multi-stage process to gain persistent, high-privilege access, including password spraying, configuration extraction, and offline cracking. Unit 42 recommends auditing remote access logs for suspicious activity, reviewing and implementing hardening guidance, and requiring multi-factor authentication for all remote services. Additionally, customers can customize password profiles and complexity, adopt a Zero Trust Architecture, change default credentials, disable unused accounts, and ensure the latest software versions and patches are installed.

**Palo Alto Networks Protections and Services**
Palo Alto Networks customers can leverage various product protections and consulting services to identify and defend against this threat. The company's products, such as PAN-OS, use encryption and salted hashes to protect credentials. Customers can also integrate multi-factor authentication platforms, customize password profiles, and follow administrative access best practices. The Unit 42 Incident Response team is available to assist with compromises or proactive assessments, and the company offers Deep and Dark Web monitoring services to identify sensitive information and leaked credentials.

---

> *When you meet someone better than yourself, turn your thoughts to becoming his equal. When you meet someone not as good as you are, look within and examine your own self.
Author: Confucius*

Source: [Threat Brief: Mitigating Large-Scale Credential Attacks](https://unit42.paloaltonetworks.com/large-scale-credential-attacks/)
