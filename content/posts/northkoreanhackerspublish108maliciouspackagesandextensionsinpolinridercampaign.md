---
title: "North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign"
date: 2026-07-04T11:17:24+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

North Korean hackers have been observed publishing 108 malicious packages and browser extensions as part of the PolinRider campaign. The campaign, linked to the Contagious Interview campaign, involves compromising maintainer accounts and modifying legitimate repositories to deliver malware. The malicious packages and extensions span multiple platforms, including npm, Packagist, Go, and Google Chrome, with 19 npm libraries, 10 Composer packages, 61 Go modules, and one Google Chrome extension affected.

The Contagious Interview campaign uses job recruitment as a tactic to target software developers and individuals in the cryptocurrency sector, using fake job interviews and assessments to trick them into executing malicious code. The campaign has been active since at least 2023 and has compromised 1,951 public GitHub repositories associated with 1,047 unique owners. The attackers use various techniques, including expired domain takeover and account recovery paths, to take over maintainer accounts and deliver malware. Once executed, the malware searches for specific files and appends malicious JavaScript code to them.

The malware also makes use of a Windows batch script to modify the last commit and rewrite Git history, making it appear as if the changes were made by the original author. The latest wave of the campaign involves a JavaScript malware loader that reaches out to blockchain infrastructure to fetch an encrypted second-stage payload. Users who have installed the malicious packages should treat their environment as compromised and take steps to rotate exposed secrets, remove affected versions, and audit their developer workstations and repositories for suspicious commits and hidden execution paths.

---

> *A subtle thought that is in error may yet give rise to fruitful inquiry that can establish truths of great value.
Author: Isaac Asimov*

Source: [North Korean Hackers Publish 108 Malicious Packages and Extensions in PolinRider Campaign](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html)
