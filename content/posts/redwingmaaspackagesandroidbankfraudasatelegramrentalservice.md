---
title: "RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service"
date: 2026-07-07T17:10:15+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new Android malware operation called RedWing is being rented out on Telegram, allowing low-skill criminals to take over a victim's phone and steal their banking logins and one-time codes. RedWing is a ready-made bank-fraud service that can be purchased in subscription tiers with referral discounts, guides, and how-to videos. The operation is believed to be a new variant of the Oblivion malware, which was documented earlier this year.

The RedWing malware is sold as a complete product, with a Telegram bot building a custom app on demand for each buyer. The app is designed to mimic legitimate app stores, such as Google Play or the Galaxy Store, and can trick users into installing it from outside the official store. Once installed, the app requests a series of permissions, including Accessibility service, which allows it to read the screen and control the phone. With these permissions, RedWing can steal passwords, read incoming texts, and even control the phone in real-time.

To protect against RedWing, individuals should only install apps from official stores and be cautious of apps that request suspicious permissions. Managed devices can also be configured to block sideloading and flag apps that request Accessibility or default-SMS roles. Researchers have published indicators of compromise to help teams detect and track the malware. It's essential to focus on the behavior of the malware rather than its name, as the same code can resurface under new names. By being aware of these tactics, users and organizations can take steps to prevent and detect RedWing and other similar malware operations.

---

> *Sometimes it is better to lose and do the right thing than to win and do the wrong thing.
Author: Tony Blair*

Source: [RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service](https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html)
