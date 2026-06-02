---
title: "KDE Linux security audit cuts kernel modules and unused packages"
date: 2026-06-02T08:45:10+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

The KDE Linux operating system has undergone a security audit, resulting in the removal of several kernel modules and software packages. The audit was prompted by the discovery of multiple security issues in the upstream Linux kernel. As a result, the project has returned to using the vanilla Linux kernel, abandoning the Zen kernel which offered little additional functionality. The alf_alg kernel modules, deemed insecure and unused, were also deleted.

The audit led to the removal of several out-of-tree kernel modules, including OpenRazer and APFS, which would have caused issues with secure boot review. Instead, the project is working towards upstream solutions for the affected functionality. Additionally, a number of unused packages were removed, including acpi_call, busybox, and vpl-gpu-rt. The unmaintained and insecure fuse2 package was also dropped, which may break some older AppImage applications. Users are advised to report any issues to the application authors or packagers.

The security audit has also led to improvements in credential storage and build checks. KDE Linux has replaced KWalletManager with KeepSecret, a credential management application packaged with Flatpak. The project has also added a service to install new pre-installed Flatpak apps on existing systems. Furthermore, build testing has been improved with the addition of a test to confirm that builds do not ship with broken file capabilities. These changes aim to move KDE Linux towards passing secure boot review by dropping out-of-tree kernel code and improving overall security.

---

> *Who we are never changes. Who we think we are does.
Author: Mary Almanac*

Source: [KDE Linux security audit cuts kernel modules and unused packages](https://www.helpnetsecurity.com/2026/06/02/kde-linux-security-audit-update/)
