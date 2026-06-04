---
title: "Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag"
date: 2026-06-03T14:56:35+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A critical vulnerability was discovered in several Microsoft 365 Android apps, including Word, PowerPoint, Excel, Microsoft 365 Copilot, Microsoft Loop, and OneNote. The issue, known as "FlagLeft," was caused by a leftover debug flag that disabled the check for trusted Microsoft apps, allowing any app on the same device to access the user's account token. This token could be used to read email, open files, browse the calendar, and send messages without requiring a password or login screen.

The vulnerability was found to be present in a shared Microsoft SDK, which is why it affected multiple apps. The tokens that were handed over were FOCI tokens, which are used for single sign-on across Microsoft apps and can be refreshed and reused over long periods. Enclave, the company that discovered the flaw, built a proof of concept that demonstrated how an unverified third-party app could pull tokens and read email. Microsoft has classified this as a local spoofing flaw, which means a malicious app already on the device is all it takes to exploit the vulnerability.

Microsoft has patched the vulnerability and issued four CVEs (Common Vulnerabilities and Exposures) for the affected apps. To fix the issue, users should update their Microsoft 365 apps from Google Play, and security teams managing Android fleets should push the updates through Mobile Device Management (MDM) and confirm devices are running the latest builds. Additionally, for accounts on devices that may have been compromised, it is recommended to revoke refresh tokens and force a fresh sign-in to ensure security.

---

> *Aerodynamically the bumblebee shouldn't be able to fly, but the bumblebee doesn't know that so it goes on flying anyway.
Author: Mary Kay Ash*

Source: [Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag](https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html)
