---
title: "New 'Bad Epoll' Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android"
date: 2026-07-03T19:40:01+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A newly discovered Linux kernel flaw, known as "Bad Epoll" (CVE-2026-46242), allows an unprivileged user to gain root access to a machine. The bug is a "use-after-free" vulnerability that occurs when two parts of the kernel try to clean up the same internal object at the same time, causing a brief collision that can be exploited by an attacker. This flaw affects Linux desktops, servers, and Android devices, and a fix is available.

The Bad Epoll bug is particularly concerning because it can be triggered from within Chrome's renderer sandbox, which is designed to block kernel bugs, and it can also affect Android devices, which are often immune to Linux privilege escalation bugs. The bug was discovered by researcher Jaeyoung Chung, who built a working exploit that can gain root access about 99% of the time on tested systems. The exploit works by widening the timing window of the collision and retrying without crashing.

The discovery of Bad Epoll highlights the challenges of finding and exploiting race condition bugs, even for advanced AI models like Anthropic's Mythos, which recently found a different bug in the same area of code but missed Bad Epoll. The bug is a reminder that AI-powered bug detection is not foolproof and that human researchers are still essential for identifying and exploiting vulnerabilities. A fix for Bad Epoll is available, and users are advised to apply the upstream commit or install their distribution's backport to protect against the vulnerability.

---

> *If the shoe doesn't fit, must we change the foot?
Author: Gloria Steinem*

Source: [New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android](https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html)
