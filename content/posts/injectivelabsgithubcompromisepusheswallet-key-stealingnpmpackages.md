---
title: "Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Packages"
date: 2026-07-10T16:29:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in 3 concise paragraphs:

The Injective Labs SDK project's GitHub repository was compromised by unknown threat actors, who published a malicious package on the npm registry. The compromised package, @injectivelabs/sdk-ts@1.20.21, contained fake telemetry functionality that stole cryptocurrency wallet private keys and mnemonic seed phrases. The malicious package was released on July 8, 2026, and has since been deprecated, but its release artifacts are still available for download from GitHub.

The threat actors introduced the malicious functionality into the project's official GitHub repository through commits submitted by a trusted developer's account. The malware was designed to fly under the radar by avoiding lifecycle scripts and not launching during the installation phase. It modified legitimate functions used in workflows to generate private keys, invoking a "trackKeyDerivation()" function that exfiltrated sensitive information to a remote server. The malware was also published across 17 additional @injectivelabs scoped packages, putting transitive users at risk.

Users who have installed the malicious version are advised to update to the newly published, clean version of the package (1.20.23) and treat any private key or mnemonic phrase passed through the package as compromised. They should also rotate their keys and check for transitive dependencies. The malicious release was facilitated through the repository's own trusted-publisher pipeline, and the malicious commits were authored and pushed under the identity of an existing, trusted maintainer. Users are urged to take immediate action to protect their cryptocurrency wallets and sensitive information.

---

> *I am a man of fixed and unbending principles, the first of which is to be flexible at all times.
Author: Everett Dirksen*

Source: [Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Packages](https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html)
