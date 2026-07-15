---
title: "148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet"
date: 2026-07-14T07:08:36+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A recent campaign involving 148 npm packages disguised as student web proxies turned visitors' browsers into a distributed denial-of-service (DDoS) botnet. The packages, which had names like "charlie-kirk" and "ilovefemboys", appeared to be a legitimate proxy service, allowing students to bypass school web filters. However, they also contained malicious code that loaded a remote code loader and a WebSocket flood generator, which could be used to launch DDoS attacks.

The malicious code was designed to run in the browser, rather than at install time, making it difficult to detect using traditional dependency scanners and install-time sandboxes. The code used a remote script loader to fetch code from a GitHub repository, which could be updated at any time, allowing the attackers to change the behavior of the botnet. The WebSocket flood generator was used to launch a control-plane attack against Wisp proxy servers, which could exhaust file descriptors, flood log storage, and drop the proxy.

The campaign was discovered by JFrog, which deobfuscated the code and reconstructed the timeline of the attack. The attackers were found to be using a GitHub organization and a Discord handle, and were likely young individuals. The infrastructure used by the attackers was clustered tightly and not built to hide, with 90 of the 93 deployment hostnames resolving to a single IP address. The malicious packages have since been pulled from npm, but the attackers still have the ability to re-arm the DDoS capability by updating the code in the mutable branch.

---

> *I can't believe that God put us on this earth to be ordinary.
Author: Lou Holtz*

Source: [148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet](https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html)
