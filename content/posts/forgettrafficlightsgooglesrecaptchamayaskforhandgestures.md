---
title: "Forget traffic lights, Google’s reCAPTCHA may ask for hand gestures"
date: 2026-06-19T10:46:43+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Google has introduced a new method for verifying that a user is human through its reCAPTCHA service, which is part of Google Cloud Fraud Defense. This new method involves hand gesture verification, where users are prompted to perform specific hand gestures that are analyzed through video processing. The goal is to help organizations identify automated activity and suspicious behavior, particularly on login pages, registration forms, and checkout systems.

The hand gesture verification process involves analyzing one or more videos of a user's hand as they perform the prompted gestures. The videos are processed to extract hand landmark data, including 21 hand-knuckle coordinates. Google emphasizes that the videos are not associated with a user's identity, audio is not recorded, and the videos are deleted after the verification process. Additionally, users have control over camera permissions, which can be revoked at any time.

For users who cannot complete hand gesture verification due to accessibility needs, reCAPTCHA's visual and audio challenges are still available. Google is also developing additional accessibility-focused verification methods to ensure that all users can verify their humanity. The hand gesture verification feature requires camera access and is designed to provide an additional layer of security verification, with related data not being shared with third parties.

---

> *A man may fulfil the object of his existence by asking a question he cannot answer, and attempting a task he cannot achieve.
Author: Oliver Holmes*

Source: [Forget traffic lights, Google’s reCAPTCHA may ask for hand gestures](https://www.helpnetsecurity.com/2026/06/19/google-recaptcha-hand-gesture-verification/)
