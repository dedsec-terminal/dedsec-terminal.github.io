---
title: "Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows"
date: 2026-05-22T11:55:24+00:00
draft: false
categories:
  - cves
---

**Megalodon GitHub Attack: 5,561 Repositories Compromised with Malicious CI/CD Workflows**

A new automated campaign, dubbed Megalodon, has targeted 5,561 GitHub repositories, injecting malicious GitHub Actions workflows that exfiltrate sensitive data, including CI secrets, cloud credentials, SSH keys, and source code secrets. The attack, which occurred within a six-hour window, pushed 5,718 malicious commits to the compromised repositories.

**How the Attack Works:**

1. The attacker uses throwaway GitHub accounts and forged author identities to inject malicious workflows into repositories.
2. The workflows contain base64-encoded bash payloads that steal sensitive data and send it to a command and control (C2) server.
3. The attacker targets CI/CD runners, using two payload variants: SysDiag and Optimize-Build.

**Stolen Data:**

* CI environment variables
* AWS credentials
* Google Cloud access tokens
* SSH private keys
* Docker and Kubernetes configurations
* Vault tokens
* Terraform credentials
* API keys
* Database connection strings
* JWTs
* PEM private keys
* Cloud tokens

**Impact:**

* The attack has compromised a large number of repositories, including @tiledesk/tiledesk-server.
* The malware executes inside CI/CD pipelines, allowing the theft of credentials and secrets at scale.
* The attack is part of a larger campaign by TeamPCP, which has compromised hundreds of open-source tools and is financially and geopolitically motivated.

**Related Attacks:**

* TeamPCP has also compromised npm packages, including a recent attack that used a throwaway account to publish nine malicious packages impersonating Polymarket trading CLI tools.
* The packages steal victims' Ethereum/Polygon private keys via a postinstall hook.

**Mitigation:**

* npm has invalidated granular access tokens with write access that bypass two-factor authentication (2FA).
* Users are urged to switch to Trusted Publishing to reduce reliance on such tokens.
* Repository owners should be cautious when merging commits and should monitor their CI/CD pipelines for suspicious activity.

---

> *We learn what we have said from those who listen to our speaking.
Author: Kenneth Patton*

Source: [Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)
