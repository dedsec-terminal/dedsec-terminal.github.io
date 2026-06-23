---
title: "New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer"
date: 2026-06-22T13:20:12+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Cybersecurity researchers at Elastic Security Labs have discovered a new malware campaign that uses a previously unknown loader called OXLOADER to deliver the CastleStealer payload. The campaign, codenamed REF8372, is believed to be operated by a Russian-speaking threat actor with financial motivations. The attackers use malicious Google Ads to distribute the malware, targeting users who search for specific keywords such as "lts version of node.js".

The attack begins when a user clicks on a fake ad, which redirects them to a bogus website hosting a batch script. The script is served from a decentralized cloud storage platform called Storj, and it displays a fake installation wizard UI while downloading and executing the OXLOADER payload. The OXLOADER loader uses various techniques such as control-flow flattening, opaque predicates, and mixed Boolean-Arithmetic to evade detection. It also employs DLL side-loading to launch a rogue DLL, which decrypts and executes the CastleStealer payload.

The CastleStealer payload is a .NET information stealer that was previously distributed through a different campaign. The OXLOADER loader is considered to be in an early operational phase, but its engineering suggests that it is a significant threat. The loader's use of code obfuscation, anti-VM measures, and unique staging techniques has resulted in low detection rates across static engines and detonation runs. As a result, OXLOADER has a window of opportunity to operate before it is detected and mitigated. The campaign highlights the ongoing threat of malware distribution through legitimate services and the importance of vigilance in detecting and preventing such attacks.

---

> *If you want your life to be more rewarding, you have to change the way you think.
Author: Oprah Winfrey*

Source: [New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer](https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html)
