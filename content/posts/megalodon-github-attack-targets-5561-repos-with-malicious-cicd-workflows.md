---
title: "Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows"
date: 2026-05-22T11:55:24+00:00
draft: false
categories:
  - cves
---

**Megalodon GitHub Attack: Malicious CI/CD Workflows Target 5,561 Repositories**

A new automated campaign, dubbed Megalodon, has been discovered targeting GitHub repositories. The attack involves injecting malicious GitHub Actions workflows containing base64-encoded bash payloads that exfiltrate sensitive data, including:

* CI environment variables
* Cloud credentials (AWS, Google Cloud, Azure)
* SSH private keys
* Docker and Kubernetes configurations
* Vault tokens
* Terraform credentials
* API keys and database connection strings

The attack was carried out using throwaway GitHub accounts and forged author identities, with 5,718 malicious commits pushed to 5,561 distinct repositories within a six-hour window. The malware executes inside CI/CD pipelines, enabling the theft of credentials and secrets at scale.

**Attack Variants and Tactics**

Two payload variants have been observed: SysDiag and Optimize-Build. The attacker used four author names and seven commit messages to mimic routine CI maintenance. The attack also involved rotating through throwaway GitHub accounts and using compromised PATs or deploy keys.

**Impact and Consequences**

The Megalodon attack is part of a larger trend of supply chain attacks, with TeamPCP compromising hundreds of open-source tools and extorting victims for profit. The attack has prompted npm to invalidate granular access tokens and urge users to switch to Trusted Publishing.

**Related Attacks**

A separate attack involves a throwaway account publishing nine malicious npm packages impersonating Polymarket trading CLI tools. These packages steal victims' Ethereum/Polygon private keys via a postinstall hook and are still available for download from npm.

**Recommendations**

To mitigate these types of attacks, it is essential to:

* Use two-factor authentication (2FA) and Trusted Publishing
* Monitor CI/CD pipelines for suspicious activity
* Validate and verify the authenticity of dependencies and packages
* Keep software and dependencies up to date with the latest security patches

The Megalodon attack highlights the importance of cybersecurity in the software development supply chain and the need for developers to be vigilant in protecting their repositories and dependencies from malicious activity.

---

> *Formula for success: under promise and over deliver.
Author: Tom Peters*

Source: [Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)
