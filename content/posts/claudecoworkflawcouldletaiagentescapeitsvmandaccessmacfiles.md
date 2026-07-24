---
title: "Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files"
date: 2026-07-23T13:27:59+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

Cybersecurity researchers at Accomplish AI have discovered a sandbox escape vulnerability in Anthropic's Claude Cowork, a virtual machine (VM) that runs on macOS. The vulnerability, codenamed "SharedRoot," allows the AI agent to break out of its Linux VM and access files on the host Mac, potentially exposing sensitive data such as SSH keys, cloud credentials, and other valuable information. Approximately 500,000 macOS users were affected by the vulnerability before it was patched.

The vulnerability is caused by the fact that the entire host file system is mounted into the agent's VM with read-write privileges, allowing the agent to access the underlying host and escape the sandbox. The researchers were able to exploit a recently disclosed flaw in the Linux kernel, known as CVE-2026-46331, to obtain guest-root privileges and access the host file system. The vulnerability can be exploited by loading the Linux kernel's "act_pedit" Traffic Control (tc) packet editing subsystem into an unprivileged user namespace and exploiting the flaw to obtain elevated privileges.

To mitigate the threat, Accomplish AI recommends disabling unprivileged user namespaces, avoiding overly permissive seccomp filters, stopping autoloading of modules, and restricting sharing of the whole host into the VM. Additionally, scoping the shared folders to only those that are actually connected, mounting them read-only, and running the coworkd daemon with strict protections can help prevent the vulnerability from being exploited. The researchers note that this is not a one-time fix, as new vulnerabilities can emerge at any time, and constant vigilance is required to stay ahead of potential threats.

---

> *Don't be afraid to go out on a limb. That's where the fruit is.
Author: H. Jackson Browne*

Source: [Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files](https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html)
