---
title: "WhatsApp, Slack Notifications Could Hijack Google Gemini on Android"
date: 2026-06-03T19:11:15+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers at SafeBreach discovered a vulnerability in Google Gemini, a voice assistant on Android, that allowed a single poisoned notification from apps like WhatsApp, Slack, or SMS to hijack the assistant. This could lead to various malicious actions, such as opening connected windows, sending fake messages, or pushing the phone into a Zoom call. No malicious app was required, as the assistant would treat the hostile notification as useful context.

The vulnerability, dubbed "Fake Context Alignment," exploited Gemini's ability to read and reply to notifications, including those from third-party apps. The researchers found that the agent reading these notifications treated their text as instructions, allowing an attacker to deliver a payload. By combining two illusions - a legitimate-looking authorization and a harmless exchange - an attacker could bypass Google's security checks and perform sensitive actions. This included smart home control, tracking and downloads, crossing into other apps, and even memory poisoning.

Google has since patched the vulnerability, which was reported to their Vulnerability Reward Program in August 2025. The fix is server-side, so no app update is required. However, users can take control by disconnecting the Utilities app in Gemini's Connected Apps settings or turning off the Google app's "Notification read, reply & control" permission on Android. The researchers stress that there is no evidence the technique was ever used in the wild, and Google has confirmed that content-classifier improvements have mitigated the notification injections and the Delayed Tool Invocation bypass.

---

> *The mind unlearns with difficulty what it has long learned.
Author: Seneca*

Source: [WhatsApp, Slack Notifications Could Hijack Google Gemini on Android](https://thehackernews.com/2026/06/whatsapp-slack-notifications-could.html)
