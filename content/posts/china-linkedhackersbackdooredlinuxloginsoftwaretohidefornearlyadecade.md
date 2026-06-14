---
title: "China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade"
date: 2026-06-12T18:17:55+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A China-linked hacking group, known as Velvet Ant, has been hiding in the Linux login system for nearly a decade. The group backdoored the PAM and OpenSSH components, which decide who is allowed to sign in, by planting their access where ordinary cleanup could not reach it. This allowed them to remain undetected, as the activity looked like normal administration and did not trigger any security alerts.

The earliest traces of the hack date back to 2016, and the group used various tactics to gain access to the targeted network, which had no direct internet access. They staged through internet-facing systems and used disguised tools to pass commands and open remote sessions deep inside the isolated network. The attackers replaced the main PAM login module with backdoored copies, allowing them to log in with a secret password or record real usernames and passwords as people logged in.

To mitigate this threat, researchers recommend monitoring the PAM and OpenSSH programs and their key files for any changes, and alerting when they change. It is also essential to hunt for changes by comparing these programs against known-good copies, as nothing will flag them for you. Additionally, removing the backdoor before resetting passwords is crucial, as the new ones can get stolen the same way. The wider lesson is that infrastructure that sits outside normal monitoring still needs integrity checks, including the login layer, to prevent similar attacks in the future.

---

> *I have an everyday religion that works for me. Love yourself first, and everything else falls into line.
Author: Lucille Ball*

Source: [China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html)
