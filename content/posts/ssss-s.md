---
title: "Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer"
date: 2026-05-23T09:51:13+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have identified a software supply chain attack targeting multiple PHP packages belonging to Laravel-Lang, a popular PHP framework. The affected packages include laravel-lang/lang, laravel-lang/http-statuses, laravel-lang/attributes, and laravel-lang/actions. The attack involves the publication of over 700 compromised versions of these packages, which were released in rapid succession, indicating automated mass tagging or republishing. This suggests that the attacker may have gained access to organization-level credentials, repository automation, or release infrastructure.

The core malicious functionality is embedded in a file named "src/helpers.php" that is included in the compromised packages. This file is designed to fingerprint the infected host and contact an external server to retrieve a PHP-based cross-platform payload. The payload is capable of running on Windows, Linux, and macOS, and is equipped to harvest a wide range of sensitive data from compromised systems. This includes authentication tokens, cloud credentials, cryptocurrency wallet information, browser history, and other sensitive data.

The attacker's payload is a comprehensive credential stealer, consisting of fifteen specialist collector modules. It is capable of collecting data from various sources, including cloud services, version control systems, and browser extensions. The collected data is then encrypted with AES-256 and sent to a command and control server. The payload also deletes itself from the disk after execution, limiting forensic evidence. The attack highlights the importance of monitoring software dependencies and ensuring the security of the software supply chain.

The compromised packages are likely to have been used in numerous applications, potentially exposing a large number of users to the credential-stealing malware. Developers who have used the affected packages are advised to review their applications and update to a secure version as soon as possible. Additionally, users should be cautious when using applications that may have been compromised, and monitor their accounts and systems for any suspicious activity. The incident serves as a reminder of the need for vigilance and proactive security measures in the software development and deployment process.

The scope of the attack and the potential impact on affected users are still being assessed. However, it is clear that the attackers have gained access to a significant amount of sensitive data, which could be used for various malicious purposes. As the investigation continues, it is essential for developers, users, and organizations to remain vigilant and take proactive steps to protect themselves from potential threats. This includes monitoring software dependencies, updating to secure versions, and implementing robust security measures to prevent similar attacks in the future.

---

> *Learn all you can from the mistakes of others. You won't have time to make them all yourself.
Author: Alfred Sheinwold*

Source: [Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer](https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html)
