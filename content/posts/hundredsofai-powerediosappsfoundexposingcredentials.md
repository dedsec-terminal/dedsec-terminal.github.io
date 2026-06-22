---
title: "Hundreds of AI-powered iOS apps found exposing credentials"
date: 2026-06-22T04:00:05+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Researchers from Wake Forest University analyzed 444 iOS applications with AI features and found that 282 of them exposed exploitable credentials or backend access mechanisms. This issue affects 26% of the analyzed apps across various categories, including productivity, entertainment, lifestyle, education, utilities, and health and fitness. The vulnerable apps had a significant number of downloads, with the most popular one having over 2.3 million user ratings.

The types of exposed credentials included authentication tokens, unauthenticated backend access, and plaintext API keys. Productivity apps accounted for the largest number of vulnerable applications, followed by entertainment and lifestyle apps. The health and fitness category had the highest leakage rate among the examined categories. The researchers found that over half of the leaked apps used custom developer-operated backends, while others used cloud platforms or communicated directly with AI providers.

The researchers disclosed the issues to the developers of the vulnerable applications and retested them 90 days later. While 28% of the vulnerable apps successfully remediated the issues, 23% remained exploitable due to lack of action or flawed authentication implementations. The study highlights the widespread and systemic issue of LLM API key leakage in the iOS ecosystem, emphasizing the need for better security measures to protect user data and prevent credential exposure. The researchers' findings suggest that adopting a proxy architecture does not prevent credential exposure, and that provider-side mitigations alone are insufficient to address the issue.

---

> *Friends are those rare people who ask how we are and then wait to hear the answer.
Author: Ed Cunningham*

Source: [Hundreds of AI-powered iOS apps found exposing credentials](https://www.helpnetsecurity.com/2026/06/22/llm-api-credential-leakage-ios-apps/)
