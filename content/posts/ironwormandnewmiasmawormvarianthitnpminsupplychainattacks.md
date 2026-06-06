---
title: "IronWorm and New Miasma Worm Variant Hit npm in Supply Chain Attacks"
date: 2026-06-05T18:05:30+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

The npm ecosystem has been hit by multiple software supply chain attacks, with threat actors using malicious and poisoned versions of over 50 legitimate packages to distribute a Rust-based information stealer and a self-spreading worm. The information stealer, codenamed IronWorm, scrapes secrets from a developer's machine, hides behind an eBPF kernel rootkit, and answers to its operator over Tor. It targets various environment variables, files, and configurations associated with popular services such as AWS, Docker, and Kubernetes.

The IronWorm malware is spread through trojanized packages published to the npm registry, allowing it to self-replicate. The malicious activity has been traced back to a compromised npm account, and the malware has been found to steal credentials and use them to push commits across repositories. The malware also incorporates an eBPF payload that functions as a kernel-level rootkit to hide processes and thwart analysis. Additionally, the malware can swap existing GitHub Actions workflows to harvest secrets and upload them as build artifacts.

A new variant of the Miasma worm has also been discovered, which has compromised 57 npm packages across more than 286 malicious versions. The Miasma worm uses a technique called "Phantom Gyp" to trigger code execution during npm install, bypassing most install-script security checks. The malware targets AI coding assistant configurations and injects persistent backdoor files into project repositories. Developers who have installed an affected version are advised to rotate credentials, turn off install scripts, and ensure packages are pinned with integrity hashes. The attribution for the latest set of attacks remains unclear, but the malware is assessed to be a derivative of the Shai-Hulud worm.

---

> *Time changes everything except something within us which is always surprised by change.
Author: Thomas Hardy*

Source: [IronWorm and New Miasma Worm Variant Hit npm in Supply Chain Attacks](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html)
