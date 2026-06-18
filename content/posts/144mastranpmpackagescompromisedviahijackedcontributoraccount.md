---
title: "144 Mastra npm Packages Compromised via Hijacked Contributor Account"
date: 2026-06-17T07:38:24+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A software supply chain attack, codenamed "easy-day-js," has compromised 144 npm packages associated with the Mastra namespace, a popular open-source JavaScript and TypeScript framework for building artificial intelligence (AI) applications. The attack occurred when a hijacked contributor account, "ehindero," published malicious packages across the Mastra scope within a short window on June 17, 2026. The infected packages do not contain malicious code themselves, but instead introduce a third-party library named "easy-day-js" that downloads and runs a cryptocurrency-stealing remote access trojan.

The "easy-day-js" library is a clone of the "dayjs" date library and was published by an npm user called "sergey2016" on June 16, 2026. The library was initially clean but was later modified to include malicious changes. The malicious code launches an obfuscated payload during a postinstall hook, which acts as a dropper or loader for a second-stage payload retrieved from attacker-controlled infrastructure. The payload is then executed as a detached background process, allowing it to harvest sensitive information, including browser history and cryptocurrency wallet data.

The attack has a large potential blast radius, with the affected packages including @mastra/core, which receives over 918K weekly npm downloads. Any workstation, CI runner, or build environment that installed the affected versions should be treated as potentially compromised. It is advised to roll back to a safe version, rotate any credentials, and audit the hosts for any artifacts linked to the campaign. The attack highlights the importance of verifying the authenticity of packages and dependencies, as well as the need for robust security measures to prevent similar attacks in the future.

---

> *Be kind whenever possible. It is always possible.
Author: Dalai Lama*

Source: [144 Mastra npm Packages Compromised via Hijacked Contributor Account](https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html)
