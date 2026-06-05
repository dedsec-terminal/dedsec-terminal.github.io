---
title: "Attackers obtained encrypted password vaults from some Dashlane user accounts"
date: 2026-06-05T11:34:19+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Dashlane, a password management company, has disclosed that a threat actor successfully launched a brute-force attack on some of its user accounts. The attack allowed the threat actor to access and copy encrypted password vaults from fewer than 20 personal plan customers. Dashlane stated that its internal systems were not compromised and that its automated security systems responded by locking targeted accounts to protect affected users.

The attack targeted API endpoints used for device registration, with the threat actor launching a high volume of automated requests to gain access to user accounts. Although the copied vaults remain encrypted, they can still be subjected to offline password-cracking attempts, making the strength of a user's master password a key factor in limiting the risk of exposure. Dashlane has deployed additional protections to detect and filter malicious traffic and is adding verification steps to the device registration process.

The incident has raised concerns about the security of password managers, particularly in light of a recent study that identified design weaknesses in several major password managers, including Dashlane. The risks associated with stolen password vaults can persist long after an incident, as demonstrated by the 2022 LastPass breach, where encrypted vault backups were still being cracked using weak master passwords as late as 2025. Dashlane's handling of the incident has also drawn criticism, with some users complaining about the lack of information provided during the outage.

---

> *The free man is he who does not fear to go to the end of his thought.
Author: Leon Blum*

Source: [Attackers obtained encrypted password vaults from some Dashlane user accounts](https://www.helpnetsecurity.com/2026/06/05/dashlane-brute-force-attack-vaults-customer-accounts/)
