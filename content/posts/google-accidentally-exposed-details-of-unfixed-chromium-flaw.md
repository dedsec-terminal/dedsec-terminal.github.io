---
title: "Google accidentally exposed details of unfixed Chromium flaw"
date: 2026-05-21T18:13:50+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Google has accidentally leaked details about an unfixed issue in Chromium that keeps JavaScript running in the background even when the browser is closed, allowing remote code execution on the device.
The flaw was reported by security researcher Lyra Rebane and acknowledged as valid in December 2022, as per the thread on Chromium Issue Tracker.
An attacker could exploit the problem to create a malicious webpage with a Service Worker, such as a download task, that never terminates. Rebane says that this could allow an attacker to execute JavaScript code on the visitors' devices.
"It's realistic to get tens of thousands of pageviews for creating a 'botnet', and people won't be aware that JavaScript can be remotely executed on their device," Rebane says in the original bug report.
Potential exploitation scenarios include using compromised browsers to launch distributed denial-of-service (DDoS) attacks, proxying malicious traffic, and arbitrarily redirecting traffic to target sites.
The is

---

> *You have to think anyway, so why not think big?
Author: Donald Trump*

Source: [Google accidentally exposed details of unfixed Chromium flaw](https://www.bleepingcomputer.com/news/security/google-accidentally-exposed-details-of-unfixed-chromium-flaw/)
