---
title: "Malicious npm Package Stole Files From Claude AI User Directory via GitHub"
date: 2026-05-27T15:44:29+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers at OX Security have discovered a malicious package on the npm registry called "mouse5212-super-formatter". This package has the capability to steal files from the "/mnt/user-data" directory, which is used by Anthropic's Claude artificial intelligence (AI) tool. The package, codenamed Malware-Slop, disguises itself as a utility for validating and initializing a GitHub repository.

The malware operates by authenticating to GitHub during the postinstall stage, using either a GitHub access token found in the victim's environment or a hard-coded token as a fallback. It then checks if a target repository exists, creates it if not, and recursively uploads all files to a threat actor-controlled GitHub account. The stolen files are stored in randomly named folders, and a fake "network connections" log is created to obscure the malware's true behavior. The package has been downloaded 676 times, although the number of actual installs is unclear.

The malicious package is notable for its sloppy implementation, with the threat actor leaking details of the GitHub account, including its private token. This suggests that the actor may be using AI to generate malware without following basic operational security best practices. OX Security warns that the ease of creating malicious code will lead to more threat actors uploading similar malware, and that npm needs to improve its automatic blocking of malware to prevent such incidents. The GitHub account linked to the campaign is no longer available, but the package remains available for download from npm.

---

> *It is not the possession of truth, but the success which attends the seeking after it, that enriches the seeker and brings happiness to him.
Author: Max Planck*

Source: [Malicious npm Package Stole Files From Claude AI User Directory via GitHub](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html)
