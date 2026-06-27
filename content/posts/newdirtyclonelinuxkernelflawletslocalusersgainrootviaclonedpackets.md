---
title: "New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets"
date: 2026-06-26T11:51:35+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A new Linux kernel vulnerability, known as DirtyClone, has been discovered, allowing local users to gain root access by corrupting file-backed memory through a cloned network packet. Tracked as CVE-2026-43503, this flaw has a CVSS score of 8.8 and can be exploited by loading a privileged binary into memory, wiring it into a network packet, and forcing the kernel to clone it. The cloned packet can then be used to overwrite the binary's login checks, granting the attacker root access.

The vulnerability is part of the DirtyFrag family and is the fourth recent privilege escalation flaw with the same failure mode. Previous vulnerabilities, including Copy Fail, DirtyFrag, and Fragnesia, have been exploited using similar techniques. The underlying problem is a contract issue, where every code path that moves skb fragments must preserve the shared-frag bit, but this contract is not always honored. The DirtyClone exploit centers on the __pskb_copy_fclone() function, but the broader fix covers additional frag-transfer helpers where the same flag could be lost.

To mitigate the vulnerability, users are advised to install their distribution's kernel update, which includes the fix that landed upstream in v7.1-rc5. If patching is not possible, two workarounds can reduce the attack surface: restricting unprivileged user namespaces and blacklisting certain kernel modules. However, these workarounds are temporary controls and not fixes. The DirtyFrag class of vulnerabilities is likely not yet fully addressed, and auditing should cover every path that touches skb_shinfo()->flags during fragment transfer to identify potential new CVEs.

---

> *By going beyond your own problems and taking care of others, you gain inner strength, self-confidence, courage, and a greater sense of calm.
Author: Dalai Lama*

Source: [New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets](https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html)
