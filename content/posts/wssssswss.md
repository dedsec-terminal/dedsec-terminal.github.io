---
title: "ZDI-26-300: Flowise AccountService resetPassword Authentication Bypass Vulnerability"
date: 2026-04-27T05:00:00+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A recently discovered vulnerability, identified as ZDI-26-300, affects Flowise installations and allows remote attackers to bypass authentication. This vulnerability can be exploited without the need for authentication, making it a significant concern for system security. The flaw is specifically located within the resetPassword method of the AccountService class, which is responsible for handling password reset requests.

The issue arises from an improper implementation of the password reset mechanism, which enables an attacker to bypass the authentication process. This means that an attacker can potentially gain unauthorized access to the system without providing valid credentials. The vulnerability can be exploited remotely, which increases the risk of unauthorized access and potential malicious activities.

The vulnerability is considered a significant threat to system security, as it allows attackers to bypass authentication and potentially gain access to sensitive data or perform malicious actions. It is essential for organizations using Flowise to take immediate action to address this vulnerability and prevent potential attacks. This can be achieved by applying patches or updates provided by the vendor or implementing additional security measures to mitigate the risk of exploitation.

The fact that this vulnerability can be exploited without authentication makes it a high-priority issue that requires prompt attention. Organizations should review their security protocols and ensure that they have the necessary measures in place to prevent exploitation. By taking proactive steps to address this vulnerability, organizations can help protect their systems and data from potential attacks and minimize the risk of security breaches.

---

> *From little acorns mighty oaks do grow.
Author: American proverb*

Source: [ZDI-26-300: Flowise AccountService resetPassword Authentication Bypass Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-300/)
