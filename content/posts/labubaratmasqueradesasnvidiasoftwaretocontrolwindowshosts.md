---
title: "LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts"
date: 2026-07-14T16:52:37+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered a previously undocumented remote access trojan (RAT) called LabubaRAT, which disguises itself as NVIDIA software to blend in with its target environment. This Rust-based malware creates a reusable foothold for attackers, allowing them to profile the host, identify security tools, receive commands, move files, capture screenshots, and proxy traffic. LabubaRAT's ability to masquerade as legitimate software makes it a significant threat to Windows hosts.

The malware's attack chain begins with an executable named "nvidia-sysruntime.exe," which accepts a runtime configuration through command-line arguments. This allows the campaign operator to define parameters such as server details and polling intervals, making it easy to reuse the same compiled binary with different infrastructure or campaign groupings. LabubaRAT then stores its configuration in a local SQLite database and undertakes discovery operations to inventory the host's web browsers and security products. It also gathers information about the hostname, RAM size, CPU model, and Windows User Account Control (UAC) state.

LabubaRAT supports a wide range of functions, including command execution, PowerShell execution, JavaScript execution, screenshot capture, file upload and download, and SOCKS5 proxy support. Its multiple communication methods, including HTTPS, WebView2, and DNS tunneling, enable attackers to maintain access to compromised hosts even if one pathway is detected and closed off. The malware's framework-like structure and ability to be configured and operated across multiple deployments make it a significant threat. Researchers believe that LabubaRAT may be offered under a malware-as-a-service (MaaS) model, making it easily accessible to various attackers.

---

> *Our distrust is very expensive.
Author: Ralph Emerson*

Source: [LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts](https://thehackernews.com/2026/07/labubarat-masquerades-as-nvidia.html)
