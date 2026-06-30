---
title: "Malicious Perplexity Chrome Extension Intercepted Searches and Address Bar Input"
date: 2026-06-29T18:40:09+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A malicious Chrome extension, "Search for perplexity ai", was discovered by Microsoft, which posed as the AI search engine Perplexity and intercepted users' searches and address bar input. The extension routed every query and character typed into the address bar through an attacker-controlled server before redirecting users to real results. This allowed the attacker to collect data, including browser headers, IP address, and user agent, without the user's knowledge.

The extension was able to collect this data by setting itself as the browser's default search engine and using a look-alike domain to pass as the real Perplexity service. It also pointed the browser's live search suggestions to the attacker's domain, allowing the collection of every character typed into the address bar, even before the user pressed Enter. Microsoft found no proof of password theft, but the extension had far more access than a search box should need, and its actions were deemed deliberate, not a side effect of the redirect.

The extension has been removed from the Chrome store after Microsoft's responsible disclosure, and users who installed it are advised to remove it and check their default search engine settings. Microsoft suggests that teams take precautions such as allowing only approved extensions, watching for changed search settings, and treating AI-branded tools with extra suspicion. The incident highlights the need for caution when installing extensions, especially those with AI branding, and the importance of monitoring browser settings and traffic to unfamiliar domains.

---

> *A good teacher is like a candle � it consumes itself to light the way for others.*

Source: [Malicious Perplexity Chrome Extension Intercepted Searches and Address Bar Input](https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html)
