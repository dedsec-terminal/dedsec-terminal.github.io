---
title: "Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT"
date: 2026-06-23T08:54:32+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

**Malicious npm Packages Discovered**: Cybersecurity researchers have identified a set of malicious npm packages that pose as PostCSS tools to deliver a Windows-based remote access trojan (RAT). The packages, published by an npm user named "abdrizak", include "aes-decode-runner-pro", "postcss-minify-selector", and "postcss-minify-selector-parser", which have been downloaded a total of 1,016 times. These packages appear to be related to legitimate PostCSS tools, but actually contain a JavaScript dropper that leads to the deployment of the Windows malware.

**Attack Chain and Malware Capabilities**: The malicious packages come embedded with a JavaScript dropper that writes a PowerShell script to disk and executes it, which then downloads a next-stage payload from an external server. The payload is a ZIP archive containing a Visual Basic Script, a Python runtime, and Python extension modules. The malware is equipped to gather host information, steal credentials from Google Chrome, collect data from Chrome extensions, run shell commands, and download/upload files to and from a command-and-control (C2) server. The malware's capabilities are realized through a set of Python native extension modules, including modules for handling C2 packet exchange, RAT orchestration, and Chrome credential theft.

**Broader Campaigns and Recommendations**: The discovery of these malicious packages coincides with other campaigns targeting the npm and TypeScript ecosystem, including packages that deliver Linux RATs, steal developer credentials, and execute dropper binaries on Windows hosts. Users who have installed any of the affected packages are advised to remove them immediately, remove any artifacts created by them, and rotate credentials from impacted developer machines. The findings highlight the importance of treating lookalike build dependencies as potential delivery mechanisms for malware, and the need for defenders to be vigilant in monitoring the npm ecosystem for suspicious activity.

---

> *Autumn is a second spring when every leaf is a flower.
Author: Albert Camus*

Source: [Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT](https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html)
