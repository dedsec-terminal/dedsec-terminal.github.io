---
title: "Debian 13.6 security update patches over a hundred advisories in trixie"
date: 2026-07-12T22:25:16+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Debian has released its 13.6 security update, codenamed "trixie", which patches over a hundred advisories. The update primarily focuses on security corrections, including a fix for an expired UEFI Secure Boot certificate authority that could prevent machines from booting with Secure Boot enabled. The update also includes fixes for serious problems and advises users to apply updates supplied by their system OEM to avoid boot issues.

The update includes several key changes, such as an update to fwupd, which can update the Secure Boot certificate authority, and a new upstream release of the shim package. Additionally, the "geoip-database" package has been reverted to a 2019 build due to licensing conflicts, which may cause software to return stale network allocation data. Web tooling has also seen significant patching, with fixes for issues such as bearer token leaks, connection reuse, and use-after-free bugs in packages like curl, rsync, and python-urllib3.

The update also includes corrections for various widely deployed software, including the apache2 web server, qemu emulator, and cryptographic libraries like openssl and gnutls28. Other notable fixes include those for Chromium, Firefox ESR, Thunderbird, Samba, PostgreSQL, and BIND. Users can upgrade their existing installation by pointing their package management system to one of Debian's many mirrors. Overall, the update provides a significant security boost to Debian 13, addressing numerous vulnerabilities and ensuring the stability and security of the operating system.

---

> *Success means having the courage, the determination, and the will to become the person you believe you were meant to be.
Author: George Sheehan*

Source: [Debian 13.6 security update patches over a hundred advisories in trixie](https://www.helpnetsecurity.com/2026/07/13/debian-13-6-security-update-released/)
