---
title: "Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install"
date: 2026-07-11T17:59:26+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the incident:

The jscrambler npm package was compromised, with its 8.14.0 release containing a malicious preinstall hook that drops and executes a native binary on the host machine. The payload is a Rust infostealer that targets developers, sweeping for secrets such as cloud credentials, cryptocurrency wallets, and password manager vaults. The stealer also targets config files for AI coding tools, including API keys and Model Context Protocol server credentials.

The malicious package was published on July 11, 2026, and was flagged by Socket just six minutes later. However, any build systems that pulled the package during that window may have already run the payload, potentially exposing sensitive information. The package's maintainer account was likely compromised, allowing the malicious version to be pushed to npm without going through the normal release flow. The payload has been found to have capabilities such as loading an eBPF program into the kernel on Linux and adding persistence mechanisms on Windows and macOS.

To mitigate the incident, users are advised to move away from version 8.14.0 and update to version 8.15.0 or pin to version 8.13.0. Users should also check their lockfiles and package-manager logs for any signs of the compromised package and rotate any secrets that may have been exposed. Indicators of compromise include the presence of a randomly named hidden file in the system temp directory, a hidden Windows scheduled task, or a macOS LaunchAgent. Network endpoints associated with the incident include two IP addresses and Tor infrastructure, which should be blocked to prevent further communication with the attacker's command-and-control servers.

---

> *You are important enough to ask and you are blessed enough to receive back.
Author: Wayne Dyer*

Source: [Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html)
