---
title: "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability"
date: 2026-06-25T14:12:52+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A popular Google Chrome ad block extension, "Adblock for YouTube", with over 10 million installs, has been found to have a dormant script injection capability. This means it can potentially execute arbitrary JavaScript code on any website, allowing it to read pages, steal data, and act as the user inside personal accounts. The extension, which has been on the Chrome Web Store since 2014, has undergone changes in ownership and codebase, and has ties to other ad-blocking extensions that have been removed from the store for malware.

The researchers who discovered the vulnerability found that the extension has the ability to run arbitrary JavaScript code, which could be activated by a single server-side configuration change without an extension update or store review. The extension's description states that it allows users to block ads on YouTube and external sites that load YouTube, but it also features capabilities to run arbitrary JavaScript code. The researchers noted that there is no evidence that malicious payload has been distributed to users, but the presence of the capability raises significant privacy and security risks.

The discovery of this vulnerability is particularly concerning because ad blocker extensions typically request extensive permissions to inspect requests, alter pages, and adjust their behavior. The "Adblock for YouTube" extension runs on every website a user visits, and its check to activate only on YouTube can be trivially bypassed by putting "youtube.com" anywhere in the URL. The researchers have contacted the developer of the extension for comment, and the disclosure comes as other browser extensions have been found to be impersonating consumer brands to monetize through affiliate marketing.

---

> *Our strength grows out of our weaknesses.
Author: Ralph Waldo Emerson*

Source: [Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)
