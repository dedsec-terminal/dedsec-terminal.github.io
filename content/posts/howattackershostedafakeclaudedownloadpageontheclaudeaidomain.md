---
title: "How attackers hosted a fake Claude download page on the claude.ai domain"
date: 2026-07-23T13:12:21+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

A threat actor exploited Anthropic's Claude Artifacts feature to host a fake Claude download page on the claude.ai domain, funneling users towards malware. The attackers created a sponsored Bing ad that directed users to the genuine claude.ai domain, but landed on a public artifact that rendered a fake download page. This page was designed to look like a legitimate Claude download page, complete with a functional interface, and was hosted on the Claude.ai domain, making it appear trustworthy.

The fake download page was viewed 7,100 times before it was taken down by Anthropic after being reported by Huntress researchers. When users clicked on the "Download" button, they were redirected to an external domain, which downloaded a bundle containing malware. The malware, known as SectopRAT, is a remote access trojan that exfiltrates user credit card data, personal information, files, and passwords. The attackers used a legitimate signed JetBrains binary vulnerable to DLL sideloading and a tampered libcef.dll to deliver the malware.

Huntress researchers were able to analyze the malware and uncover the command-and-control address, tracing the operator to previous malware delivery campaigns. The researchers found connections to an email address linked to ten domains, including one that was seized by Microsoft as part of Operation Endgame. The attackers' tactics highlight the importance of being cautious when searching for software to download, as threat actors have become skilled at pushing malicious ads via popular search engines and hosting malicious content on legitimate platforms and domains. Users are advised not to trust search engine ads and top-level domains implicitly to avoid falling victim to such attacks.

---

> *The truth which has made us free will in the end make us glad also.
Author: Felix Adler*

Source: [How attackers hosted a fake Claude download page on the claude.ai domain](https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/)
