---
title: "CISA Warns Fortinet Customers as FortiBleed Hits 86,644 FortiGate Devices"
date: 2026-06-19T14:00:21+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The US Cybersecurity and Infrastructure Security Agency (CISA) has warned Fortinet customers to secure their FortiGate appliances against an ongoing malicious campaign known as FortiBleed. The campaign, believed to be carried out by Russian-speaking threat actors, has compromised 86,644 devices as of June 19, 2026. The majority of compromised credentials are generic admin accounts and built-in Fortinet system accounts, indicating a widespread failure to rename default accounts or rotate factory credentials.

The threat actors have used a bespoke tool to scan the internet for Fortinet remote login endpoints and then employed a brute-force attack to break into them using known login and password combinations. Once access is obtained, they passively monitor network traffic to collect additional credentials, which are then used to compromise more appliances. The credentials are verified and added to a database of confirmed, working logins. The attack has targeted various sectors, including telecom, government, and education, with the most exposures located in India, the US, Mexico, Colombia, and Thailand.

To defend against the activity, CISA has outlined several recommendations, including terminating all active SSL VPN and administrative sessions, resetting all Fortinet VPN and administrative passwords, and enforcing strong password policies. Additionally, organizations are advised to use the Password-Based Key Derivation Function 2 (PBKDF2) algorithm to store administrator credentials, review logs for suspicious actions, and enable phishing-resistant multi-factor authentication (MFA) on all external gateways and administrative interfaces. Fortinet has also urged organizations to follow best practices, including regularly rotating security credentials and enabling MFA, to prevent similar incidents in the future.

---

> *Never mistake activity for achievement.
Author: John Wooden*

Source: [CISA Warns Fortinet Customers as FortiBleed Hits 86,644 FortiGate Devices](https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html)
