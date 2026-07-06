---
title: "New ClamAV security patch closes seven scanner bugs dating back two decades"
date: 2026-07-05T22:30:13+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

The ClamAV open-source antivirus scanning engine, maintained by Cisco's Talos group, has released two patch versions, 1.5.3 and 1.4.5, to address seven security flaws. These vulnerabilities, some of which date back two decades, affect the scanner's ability to handle hostile input, including executable formats, archives, and disk-image handling. The patched bugs include integer overflows, buffer overflows, and parser flaws that could lead to crashes, data corruption, or unauthorized access.

The vulnerabilities are primarily located in the code that unpacks and parses executable formats, with three bugs affecting PE parsing and three others affecting archive and disk-image handling. One of the PE parsing bugs, CVE-2026-20214, has been present in the codebase since 2004, while another, CVE-2026-20217, has been present since 2005. The archive and disk-image handling bugs include issues with 7z, ALZ, and InstallShield archives, as well as a 32-bit DMG parser flaw.

In addition to the security fixes, the new releases also include hardening changes, such as improved quarantine actions to prevent time-of-check/time-of-use races. Version 1.5.3 also includes additional updates, including upgrades to the Rust tar dependency and the Rust openssl dependency, as well as a fix for hash bucket list corruption in ClamOnAcc. The release files are available on the GitHub release page and through Docker Hub, and users are advised to update to the latest version to ensure the security and integrity of their systems.

---

> *The more you know yourself, the more you forgive yourself.
Author: Confucius*

Source: [New ClamAV security patch closes seven scanner bugs dating back two decades](https://www.helpnetsecurity.com/2026/07/06/clamav-security-patch-versions/)
