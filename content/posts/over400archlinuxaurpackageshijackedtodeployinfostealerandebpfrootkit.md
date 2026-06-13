---
title: "Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit"
date: 2026-06-12T19:33:25+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Attack Overview**
Over 400 packages in the Arch User Repository (AUR) were hijacked by attackers, who rewrote their build scripts to install a credential stealer on any machine that built them. The malware, a Rust binary, harvests developer secrets, including cookies, tokens, and SSH keys, and can load an eBPF rootkit to hide itself when run with root privileges. The attack targets the trust model of the AUR, exploiting abandoned packages and spoofing git commit metadata to appear legitimate.

**Malware Capabilities**
The malware collects sensitive information from various sources, including Chromium-based browsers, Electron apps, and GitHub tokens. It also installs a systemd service for persistence and can load an eBPF rootkit to hide its processes and socket inodes from standard tools. The rootkit is optional and only loads when the binary has root privileges. The malware also stages a second file tied to a possible cryptominer. The attack is significant due to its scale and the use of an eBPF rootkit, making it difficult to clean up after the payload has run.

**Mitigation and Detection**
To mitigate the attack, users who installed or updated an AUR package on or after June 11 should check their packages against the community-maintained lists of affected packages. If a flagged package ran, users should treat the host as credential-compromised and rotate all affected credentials. Users should also hunt for persistence by checking for unknown systemd services and unexpected files. To prevent similar attacks, users should read the PKGBUILD and .install hooks before building a package, especially for recently adopted or dormant packages. Detection scripts and indicators of compromise are available to help identify and remove the malware.

---

> *Smile, breathe, and go slowly.
Author: Thich Nhat Hanh*

Source: [Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit](https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html)
