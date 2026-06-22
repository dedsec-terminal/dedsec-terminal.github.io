---
title: "The systemd 261 release brings a software TPM, new OS installer"
date: 2026-06-21T22:30:29+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

The systemd 261 release brings several new features and improvements to Linux distributions that use systemd as their init system. One of the key additions is a cloud metadata subsystem, which provides a local interface for accessing instance metadata services. This is achieved through a daemon called systemd-imdsd, which offers a Varlink API that allows programs to access metadata services. The recognized clouds include major providers such as Amazon EC2, Microsoft Azure, and Google Compute Engine.

Another significant feature in systemd 261 is the ability to carry process state through kexec reboots. This means that system units can now preserve their file descriptor stores and receive their stashed file descriptors back after a reboot. This feature is enabled by setting FileDescriptorStorePreserve=yes and is supported by user session managers and systemd-nspawn containers. Additionally, systemd 261 introduces a software TPM (Trusted Platform Module) service, which allows systems without physical TPM hardware to use IBM's swtpm as a software TPM.

The release also includes other notable additions, such as a new textual OS installer called systemd-sysinstall, which is built on Varlink calls to systemd-repart, bootctl, and systemd-creds. Furthermore, systemd-oomd now supports OOM rulesets, and the manager exposes a ReloadCount property over D-Bus and Varlink. The release also removes support for udev's database version 0, which ends support for live upgrades from releases older than v247. Overall, systemd 261 provides a range of new features and improvements that enhance the functionality and security of Linux distributions that use systemd.

---

> *We aim above the mark to hit the mark.
Author: Ralph Emerson*

Source: [The systemd 261 release brings a software TPM, new OS installer](https://www.helpnetsecurity.com/2026/06/22/systemd-261-released/)
