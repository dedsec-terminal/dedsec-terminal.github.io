---
title: "Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer"
date: 2026-06-29T05:36:06+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers have discovered two hijacked npm packages and 16 compromised Go packages that deploy a Python-based information stealer on Windows, Linux, and macOS hosts. The attack uses a hidden VS Code task named "eslint-check" to execute arbitrary code when a project folder is opened in VS Code. The task retrieves encrypted JavaScript from blockchain transaction data, connects to attacker-controlled infrastructure, and eventually deploys a Python infostealer. The npm packages, "html-to-gutenberg" and "fetch-page-assets", were uploaded to the npm registry on May 25, 2026, but are no longer available for download.

The attack is attributed to a campaign known as "Fake Font", which has been linked to North Korea. The campaign uses a multi-stage loader to deploy the InvisibleFerret Python backdoor, designed to steal cryptocurrency wallets, browser credentials, and establish persistent access. The malware disguises itself as a font file and uses blockchain infrastructure as a dead drop resolver to fetch a next-stage JavaScript payload. The infection chain sets up a Socket.io backdoor, allowing the operator to remotely control the infected host, and launches a Python loader component to retrieve the Python infostealer from the C2 server.

The Python infostealer is a wide-ranging credential, browser, wallet, and developer artifact stealer that can siphon data from various sources, including browsers, password managers, authenticators, and cryptocurrency wallets. It also harvests developer-oriented information, such as Git credentials and VS Code storage. The collected data is packaged into compressed ZIP archives and uploaded to the C2 server and a Telegram bot. Users who have installed the compromised packages are advised to remove them immediately, search for hidden VS Code tasks, and rotate credentials, tokens, and wallet credentials to prevent further compromise.

---

> *Sadness may be part of life but there is no need to let it dominate your entire life.
Author: Byron Pulsifer*

Source: [Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer](https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html)
