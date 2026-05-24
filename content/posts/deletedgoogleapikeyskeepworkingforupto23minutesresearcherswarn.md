---
title: "Deleted Google API keys keep working for up to 23 minutes, researchers warn"
date: 2026-05-22T12:08:12+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Researchers at Aikido Security have discovered that deleted Google API keys can continue to work for up to 23 minutes after deletion. This is a concern because API keys are used to access Google services, and if a key is leaked, an attacker can use it to make unauthorized API calls, rack up charges, and access sensitive data. The researchers found that even after deleting a key, they were able to make successful authentications with a median window of around 16 minutes.

The issue is due to Google Cloud's "eventually consistent" design, which allows for gradual updates across servers rather than instantaneous ones. This design tradeoff enables Google to scale globally and maintain speed, but it can lead to problems with authentication. The researchers also noted that Google's deletion dialog is misleading, stating that the key "can no longer be used to make API requests" when in fact it can still be used for a period of time. Additionally, there is no way for users to confirm when the key has fully stopped working or to speed up the deletion process.

The researchers warn that users should be aware of this issue and treat key deletion as a 30-minute operation. During this window, users should monitor API usage in the GCP console to detect any potential unauthorized activity. The researchers also found that faster revocation is technically achievable, as evidenced by the shorter revocation windows for Google Service Account keys and a newer format of API key. However, Google has stated that this is a known property of the system and not a security issue, and it is unclear whether they will take steps to address the problem.

---

> *Imagination is the living power and prime agent of all human perception.
Author: Samuel Taylor Coleridge*

Source: [Deleted Google API keys keep working for up to 23 minutes, researchers warn](https://www.helpnetsecurity.com/2026/05/22/deleted-google-api-keys-risk/)
