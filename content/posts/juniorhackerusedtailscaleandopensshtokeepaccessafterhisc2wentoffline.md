---
title: "Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline"
date: 2026-06-17T16:00:56+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A French-speaking attacker, known as "Poisson," broke into a small French automotive business, stealing banking and email credentials. The attacker used a keylogger and installed OpenSSH and Tailscale on a victim's machine, creating a backdoor that allowed them to maintain access even after their command-and-control (C2) server went offline. This move was significant, as it showed that the attacker had created a separate door into the network that did not rely on the C2 server.

The attacker's methods were relatively unsophisticated, with a "junior operator" profile and a reliance on free-tier tools such as DuckDNS and Backblaze B2. Despite this, they were able to compromise four machines and steal sensitive information. The attacker's use of Tailscale, a legitimate remote-access tool, allowed them to create a secure and encrypted connection to the victim's machine, even after the C2 server was taken offline. This highlights the importance of looking beyond the C2 server and searching for other potential entry points.

The incident highlights the need for thorough remediation efforts, as simply taking down a C2 server may not be enough to prevent further attacks. Researchers recommend watching for signs of backdoors, such as the installation of OpenSSH Server on a Windows workstation, and monitoring for suspicious activity, such as reverse tunnels and scheduled tasks with high privileges. By assuming that a C2 server is not the only way into a network, security teams can take a more proactive approach to hunting down and removing potential backdoors, preventing attackers from maintaining access to sensitive information.

---

> *The world is round and the place which may seem like the end may also be the beginning.
Author: Ivy Baker Priest*

Source: [Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline](https://thehackernews.com/2026/06/junior-hacker-used-tailscale-and.html)
