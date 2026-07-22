---
title: "Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs"
date: 2026-07-21T18:46:32+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Apple has fixed a security flaw in its Hide My Email service that allowed users' real email addresses to be exposed. The feature, which generates unique, random email addresses to forward messages to a user's personal inbox, is designed to protect user privacy and prevent spam. However, a bug made it possible to unmask a user's real email address, undermining the feature's privacy guarantees.

The issue was first reported to Apple in June 2025, but the company was unable to patch it until July 3, 2026. The bug was triggered when a message sent to a Hide My Email address was rejected as spam, causing the user's real email address to appear in email logs. The exact number of affected users is unknown, but it is possible that real email addresses were leaked in email logs, even if the messages were legitimate and did not reach the user's inbox.

The fix comes as Apple faces a class action lawsuit accusing the company of misleading customers about the privacy of its Hide My Email feature. The lawsuit claims that Apple failed to deliver on its promise of privacy, despite charging customers for the feature. Apple's failure to address the issue for over a year and its decision not to warn customers or correct its privacy representations have been criticized. The company has finally resolved the issue, but it is possible that some users' real email addresses may have been captured in mail transfer logs before the fix was implemented.

---

> *Be not afraid of greatness: some are born great, some achieve greatness, and some have greatness thrust upon them.
Author: William Shakespeare*

Source: [Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs](https://thehackernews.com/2026/07/apple-fixes-hide-my-email-bug-that.html)
