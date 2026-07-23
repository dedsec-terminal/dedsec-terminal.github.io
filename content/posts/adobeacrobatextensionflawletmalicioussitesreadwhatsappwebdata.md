---
title: "Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data"
date: 2026-07-22T15:01:21+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Cybersecurity researchers at Guardio Labs have discovered a vulnerability in the Adobe Acrobat Chrome extension, which has over 314 million users. The flaw, codenamed HermeticReader (CVE-2026-48294), is a universal cross-site scripting (UXSS) vulnerability that allows malicious sites to read WhatsApp Web data. This vulnerability affects all versions of the extension prior to and including 26.5.2.2 and can be exploited by convincing a user to visit a maliciously crafted URL or interact with a compromised web page.

The vulnerability can bypass the browser's same-origin policy, allowing an attacker to access data linked to the victim's session across origins. This includes authenticated content from third-party web applications loaded in the victim's browser. To exploit the flaw, an attacker-controlled page can wake up a dormant engine inside the extension, which can then reach directly into WhatsApp Web and steal sensitive data, including chat lists, contact names, messages, and profile names. The attack does not require malware installation, phishing, or session cookie extraction, making it a significant threat.

The exploitation sequence involves an attacker-controlled page calling an iframe element loaded from the extension resources, which then sends commands to alter settings and activate the Hermes engine. The engine manipulates WhatsApp Web's DOM to steal data by injecting a POST form into WhatsApp's DOM. The stolen data can include the rendered chat list, contact names, message previews, and the visible text of the open conversation. The vulnerability has been patched, but it highlights the importance of checking the "plumbing" of widely used extensions, as composition-level flaws can lead to significant security breaches.

---

> *The most important thing is transforming our minds, for a new way of thinking, a new outlook: we should strive to develop a new inner world.
Author: Dalai Lama*

Source: [Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data](https://thehackernews.com/2026/07/adobe-acrobat-extension-flaw-let.html)
