---
title: "Packagist Supply Chain Attack Infects 8 Packages Using GitHub-Hosted Linux Malware"
date: 2026-05-23T16:07:51+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A recent supply chain attack has compromised eight packages on Packagist, a repository for PHP packages. The attack involved inserting malicious code into the package.json file of the affected packages, rather than the composer.json file, which is typically scanned for security vulnerabilities. This "cross-ecosystem placement" allowed the attackers to target projects that use both PHP and JavaScript code, potentially evading detection by security teams.

The malicious code, which was inserted into the postinstall script of the affected packages, attempts to download a Linux binary from a GitHub Releases URL and run it in the background. The binary is saved to the "/tmp/.sshd" folder and granted execute permissions using "chmod". Although the malicious versions of the packages have been removed from Packagist, an analysis of the packages has revealed that the upstream repositories have been modified to include the malicious code.

The affected packages include moritz-sauer-13/silverstripe-cms-theme, crosiersource/crosierlib-base, and devdojo/wave, among others. Socket's investigation has found references to the same payload across 777 files in GitHub, suggesting that this may be part of a broader campaign. The exact nature of the payload is unclear, as the GitHub account associated with the repository hosting it is no longer available. However, the malicious installer is sufficient to warrant blocking, as it provides remote code execution during installation or build workflows and attempts to hide its activity.

The use of a Linux binary with a name similar to a legitimate GNOME Virtual File System (GVfs) daemon is notable, as it may be an attempt to disguise the malware as a legitimate system component. The attack highlights the importance of scanning all dependencies, including package.json lifecycle hooks, for security vulnerabilities. It also underscores the need for developers and security teams to be aware of the potential for cross-ecosystem attacks, where malicious code is inserted into packages that use multiple programming languages or ecosystems.

The removal of the malicious packages from Packagist and the investigation into the attack are ongoing. However, the incident serves as a reminder of the importance of vigilance and thorough security testing in the development and deployment of software packages. By being aware of the potential for supply chain attacks and taking steps to mitigate them, developers and security teams can help protect their users and prevent similar incidents in the future.

---

> *Difficulties increase the nearer we get to the goal.
Author: Johann Wolfgang von Goethe*

Source: [Packagist Supply Chain Attack Infects 8 Packages Using GitHub-Hosted Linux Malware](https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html)
