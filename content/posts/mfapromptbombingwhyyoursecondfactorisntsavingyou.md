---
title: "MFA Prompt Bombing: Why Your Second Factor Isn't Saving You"
date: 2026-05-26T10:30:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article on MFA prompt bombing:

Multi-factor authentication (MFA) was designed to provide an additional layer of security, but attackers have found a way to bypass it. MFA prompt bombing involves attackers using valid account credentials, often obtained from breached password dumps, to trigger repeated login attempts and prompt the user to approve the request. The goal is to trick the user into approving the login, allowing the attacker to gain access to the account. This type of attack is particularly effective against organizations that use push-based MFA, where users are asked to approve or deny a login with little context.

The Cisco breach in 2022 is a notable example of the effectiveness of MFA prompt bombing. An attacker compromised a Cisco employee's personal Google account, which stored the employee's Cisco VPN password. The attacker then triggered MFA prompts to the employee's phone, and after initial failures, used vishing calls to pose as IT support and convince the employee to accept a push notification. Once accepted, the attacker gained VPN access and was able to escalate privileges, exfiltrate data, and maintain persistence. This attack highlights the vulnerability of push-based MFA and the need for more robust security measures.

To prevent MFA prompt bombing, organizations can take several steps. These include using fatigue and phishing-resistant MFA factors, such as FIDO2 security keys or number-matching codes, which are harder to abuse. Additionally, blocking compromised passwords at the source by scanning Active Directory against a live database of breached passwords can remove the fuel for the attack. Finally, adding risk signals to the login process, such as geography, device posture, and login times, can block or step up authentication before a prompt is sent to the user's phone. By taking these measures, organizations can strengthen their MFA and reduce the risk of prompt bombing attacks.

---

> *If we learn to open our hearts, anyone, including the people who drive us crazy, can be our teacher.
Author: Pema Chodron*

Source: [MFA Prompt Bombing: Why Your Second Factor Isn't Saving You](https://thehackernews.com/2026/05/mfa-prompt-bombing-why-your-second.html)
