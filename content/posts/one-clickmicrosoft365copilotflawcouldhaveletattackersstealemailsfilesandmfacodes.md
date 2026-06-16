---
title: "One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes"
date: 2026-06-15T15:09:05+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Researchers at Varonis Threat Labs discovered a critical vulnerability in Microsoft 365 Copilot Enterprise Search, which could have allowed attackers to steal sensitive information, including emails, files, and multi-factor authentication (MFA) codes. The flaw, dubbed "SearchLeak," was caused by a combination of three bugs that could be exploited with a single click on a trusted Microsoft link. The link, which pointed to a real microsoft.com domain, would not have been flagged by traditional anti-phishing and URL filtering tools.

The SearchLeak vulnerability worked by exploiting a command injection flaw in the Copilot Enterprise Search URL, which allowed attackers to inject malicious code and extract sensitive information. The attack involved a "Parameter-to-Prompt injection" technique, where an attacker would craft a URL that instructed Copilot to search for specific information and embed it in an image URL. The victim would then click on the link, and Copilot would do the rest, ultimately allowing the attacker to exfiltrate the stolen data through a Bing image endpoint.

Microsoft has mitigated the flaw on its backend, and customers do not need to take any action. However, researchers warn that similar vulnerabilities may exist, and organizations should be vigilant in monitoring their systems for suspicious activity. To protect themselves, organizations can look for Copilot Search URLs carrying encoded payloads or HTML in the q parameter and monitor for unusual outbound requests to Bing's image endpoints. Additionally, they can tighten data-access governance to limit the amount of data that Copilot can index, reducing the potential impact of any future leaks.

---

> *You can be what you want to be. You have the power within and we will help you always.
Author: Byron Pulsifer*

Source: [One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html)
