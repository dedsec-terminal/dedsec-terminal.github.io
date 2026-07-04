---
title: "North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets"
date: 2026-07-03T16:07:15+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**North Korea-Linked Malicious npm Packages Discovered**
Threat actors with ties to North Korea have been linked to a set of malicious npm packages that mimic Rollup polyfill tooling to steal developer secrets. The packages, including "rollup-packages-polyfill-core" and "rollup-runtime-polyfill-core", are designed to look like legitimate packages, making them difficult to detect during a quick dependency review.

**Malicious Package Behavior**
The malicious packages install and load additional packages, such as "swift-parse-stream" and "quirky-token", which fetch a JSON object from a remote server and execute a JavaScript malware. The malware checks to avoid execution within cloud development environments and sandboxes, and then installs dependencies and reaches out to an external server to fetch an encrypted payload. The decrypted payload enables remote access to the compromised host, allowing for interactive terminal sessions, command execution, and data theft, including stealing data from web browsers and cryptocurrency wallets.

**Recommendations and Similar Attacks**
Users who have installed the malicious packages are advised to remove them, assume compromise, and rotate credentials. The discovery of these packages coincides with the discovery of multiple software supply chain attacks aimed at poisoning open-source package repositories and stealing valuable data. Similar attacks have been discovered in the past, including a sustained npm campaign that involved publishing 108 malicious npm packages to deliver malware. Developers are advised to enable dependency scanning in CI/CD pipelines to flag newly published or suspicious packages and to be cautious when installing packages from unknown sources.

---

> *Successful people ask better questions, and as a result, they get better answers.
Author: Tony Robbins*

Source: [North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets](https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic.html)
