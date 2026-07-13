---
title: "Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access"
date: 2026-07-10T10:30:20+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A threat actor, tracked as O-UNC-066, has been targeting organizations across multiple sectors with voice-based phishing attacks. The attackers pose as Microsoft representatives and prompt users to enroll a new Entra passkey, which is a phishing-resistant security upgrade. The goal is to gain unauthorized access to Microsoft 365 accounts and carry out data extortion attacks. The targeted industries include food and beverage, technology, healthcare, automotive, construction, and aviation.

The attackers use a panel-controlled phishing kit that mimics the Microsoft passkey enrollment process, making it difficult for users to distinguish between the legitimate and fake processes. The kit is capable of adapting to each victim's multi-factor authentication (MFA) requirements, allowing the attackers to guide the user through the passkey enrollment process in real-time. The attackers then use the harvested credentials to enroll their own passkey in the victim's Microsoft account, granting them unauthorized access.

The phishing kit used in these attacks is sophisticated, with multiple pages that mimic the legitimate Microsoft passkey enrollment process. The attackers use social engineering tactics to deceive users into approving the attacker's access to their Microsoft 365 account. The attack chain involves a series of actions, including harvesting credentials, presenting fake MFA challenges, and enrolling a passkey in the victim's account. The threat actor behind these attacks is suspected to be linked to a decentralized cybercrime collective known as The Com, which includes groups such as Scattered Spider, ShinyHunters, and LAPSUS$.

---

> *What worries you masters you.
Author: Haddon Robinson*

Source: [Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access](https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html)
