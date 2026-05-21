---
title: "9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros"
date: 2026-05-21T07:35:53+00:00
draft: false
categories:
  - cves
---

**9-Year-Old Linux Kernel Vulnerability Discovered**

A cybersecurity research team has identified a 9-year-old flaw in the Linux kernel, tracked as CVE-2026-46333, which allows an unprivileged local user to execute arbitrary commands as root on major Linux distributions such as Debian, Fedora, and Ubuntu. The vulnerability, also known as "ssh-keysign-pwn," is caused by improper privilege management in the kernel's `__ptrace_may_access()` function, introduced in November 2016.

**Exploitation and Impact**

The vulnerability can be exploited to disclose sensitive files, including `/etc/shadow` and host private keys, and execute arbitrary commands as root through four different exploits. Successful exploitation could allow a local attacker to gain root privileges, potentially leading to a complete system compromise.

**Recommendations and Mitigations**

To mitigate the vulnerability, users are advised to apply the latest kernel update released by their Linux distribution. If updates cannot be applied immediately, a temporary workaround is to raise the `kernel.yama.ptrace_scope` value to 2. Additionally, users who have allowed untrusted local users during the exposure window should rotate their host keys and review any administrative material that may have been compromised.

**Related Vulnerability: PinTheft**

A separate local privilege escalation flaw, called PinTheft, has also been discovered, which allows local attackers to gain root privileges on Arch Linux systems. The exploit requires specific conditions to be met, including the presence of the Reliable Datagram Sockets (RDS) module and io_ring.

**Key Takeaways**

* A 9-year-old Linux kernel vulnerability (CVE-2026-46333) has been discovered, allowing unprivileged local users to execute arbitrary commands as root.
* The vulnerability affects major Linux distributions, including Debian, Fedora, and Ubuntu.
* Users should apply the latest kernel update or use temporary workarounds to mitigate the vulnerability.
* A separate local privilege escalation flaw, PinTheft, has been discovered, affecting Arch Linux systems.

---

> *It's so simple to be wise. Just think of something stupid to say and then don't say it.
Author: Sam Levenson*

Source: [9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros](https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html)
