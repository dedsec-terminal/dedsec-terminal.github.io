---
title: "CISA Admin Leaked AWS GovCloud Keys on Github"
date: 2026-05-18T20:48:21+00:00
draft: false
categories:
  - data-breaches
---

A cybersecurity article reports that a contractor for the Cybersecurity and Infrastructure Security Agency (CISA) accidentally leaked highly sensitive credentials, including AWS GovCloud keys, on a public GitHub repository. The repository, named "Private-CISA," contained internal CISA systems, cloud keys, tokens, plaintext passwords, logs, and other sensitive assets. The leak is considered one of the most egregious government data leaks in recent history.

The leak was discovered by a security researcher, Guillaume Valadon, who notified CISA and the contractor, Nightwing. The repository was taken offline, but the exposed AWS keys remained valid for another 48 hours.

The leak is attributed to poor security hygiene, including the use of easily-guessed passwords and the disabling of GitHub's default setting that blocks users from publishing sensitive information. The contractor's GitHub account showed a pattern of use consistent with an individual operator using the repository as a working scratchpad or synchronization mechanism.

CISA has acknowledged the incident and is investigating, but claims that there is no indication that any sensitive data was compromised. However, security experts warn that the exposed credentials could be used by malicious attackers to gain access to CISA systems and maintain a persistent foothold.

The incident raises concerns about the security practices of government contractors and the potential risks of data exposure. It also highlights the challenges faced by CISA, which is currently operating with reduced budget and staffing levels.

---

> *For every failure, there's an alternative course of action. You just have to find it. When you come to a roadblock, take a detour.
Author: Mary Kay Ash*

Source: [CISA Admin Leaked AWS GovCloud Keys on Github](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)
