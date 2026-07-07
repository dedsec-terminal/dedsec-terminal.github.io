---
title: "16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems"
date: 2026-07-06T17:37:01+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A 16-year-old flaw in the Linux KVM hypervisor, dubbed "Januscape" (CVE-2026-53359), has been discovered, allowing guest virtual machines to escape to the host on Intel and AMD x86 systems. The vulnerability is a use-after-free bug in the shadow MMU code, which can be triggered by a guest VM to corrupt the host kernel's shadow-page state. This can lead to a host panic, taking down all other VMs on the same physical machine.

The flaw was found by security researcher Hyunwoo Kim, who reported it to the Linux community. The vulnerability requires two conditions to be exploited: root access inside the guest VM and nested virtualization exposed by the host. The attack does not require cooperation from QEMU or any userspace VMM and is purely an in-kernel KVM bug. Kim has also developed a separate, unreleased exploit that can turn the bug into full host code execution, allowing an attacker to run code as root on the host.

The vulnerability affects any x86 environment that hosts untrusted guests with nested virtualization enabled. To mitigate the issue, users can either patch their kernel with the fixed version or disable nested virtualization. The fix is a one-line addition to the KVM code, and fixed stable versions have been shipped. Users are advised to check their kernel version and patch immediately, especially if they operate an x86 KVM host that accepts multi-tenant guests with nested virtualization. Disabling nested virtualization can also remove the attack path for untrusted guests until a patch can be applied.

---

> *We don't stop playing because we grow old; we grow old because we stop playing.
Author: Bernard Shaw*

Source: [16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html)
