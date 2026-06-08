---
title: "Hackers used Meta’s AI support system to hijack over 20,000 Instagram accounts"
date: 2026-06-08T13:50:42+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Meta, the company behind Instagram, has revealed that hackers exploited a flaw in its AI-assisted account recovery system to hijack over 20,000 Instagram accounts. The vulnerability, which was discovered on May 31, allowed unauthorized parties to perform password resets on accounts by providing an email address not associated with the account. As a result, attackers were able to receive password reset links and gain access to accounts that did not have two-factor authentication (2FA) enabled.

The attack was relatively simple, with hackers using VPN services to appear as if they were in the same geographic area as the target account. They would then interact with Meta's AI support assistant, asking it to link the account to an email address under their control. The attackers targeted high-profile accounts, including those of the Obama White House and the U.S. Space Force's Chief Master Sergeant, as well as short, high-value usernames that can be resold on underground markets. Meta has stated that it has no evidence of what information was accessed from the compromised accounts, but potentially exposed data includes contact information, dates of birth, photos, and more.

Meta has taken steps to address the issue, including disabling the affected AI-assisted support tool, invalidating password reset links, and requiring additional authentication for potentially affected accounts. The company is also conducting a comprehensive review of similar account recovery flows across its platforms to identify and remediate any potential issues. Prior to re-launching the tool, Meta will fix the authentication check to ensure proper verification of email addresses against existing account information. The incident highlights the potential risks of relying on AI-powered support systems and the importance of robust security measures to protect user accounts.

---

> *You can do what's reasonable or you can decide what's possible.*

Source: [Hackers used Meta’s AI support system to hijack over 20,000 Instagram accounts](https://www.helpnetsecurity.com/2026/06/08/instagram-ai-support-vulnerability-account-takeovers/)
