---
title: "Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign"
date: 2026-05-24T14:12:32+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A large-scale campaign is currently exploiting a critical SQL injection vulnerability in Ghost CMS, identified as CVE-2026-26980. This vulnerability allows unauthenticated attackers to read arbitrary data from the website database, including admin API keys, which can be used to modify article pages and gain management access to users, articles, and themes. The campaign, discovered by XLab threat intelligence researchers, has impacted over 700 domains, including prominent websites such as Harvard University, Oxford University, and DuckDuckGo.

The attack chain begins with the exploitation of CVE-2026-26980 to steal admin API keys, followed by the injection of malicious JavaScript into articles. This JavaScript code fetches second-stage code from the attacker's infrastructure, which fingerprints visitors to determine whether they qualify as targets. Visitors who pass the verification are served a fake Cloudflare prompt, which contains the ClickFix lure, instructing them to paste a provided command on their Windows command prompt, resulting in the drop of a payload on their systems.

The payloads used in these attacks include DLL loaders, JavaScript droppers, and an Electron-based malware sample. To mitigate the risk, Ghost CMS website administrators are advised to upgrade to version 6.19.1 or later and rotate all previously used keys, as they may have been exposed. A thorough review of the websites is necessary to locate and remove injected scripts, and maintaining a 30-day record of admin API call logs can enable a reliable retrospective investigation.

The fact that many sites failed to install the security update, released on February 19, has allowed the campaign to continue exploiting the vulnerability. Researchers have observed at least two distinct activity clusters targeting vulnerable Ghost sites, with attackers sometimes re-infecting the same domains with different scripts after cleanup. The campaign highlights the importance of keeping software up to date and implementing robust security measures to prevent such attacks. By taking prompt action, website administrators can protect their sites and prevent further exploitation of the CVE-2026-26980 vulnerability.

---

> *When your desires are strong enough you will appear to possess superhuman powers to achieve.
Author: Napoleon Hill*

Source: [Ghost CMS SQL injection flaw exploited in large-scale ClickFix campaign](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/)
