---
title: "New Browser-in-the-Browser phishing uses fake login popups to steal Microsoft 365 credentials"
date: 2026-06-10T12:53:58+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new phishing campaign, known as Browser-in-the-Browser (BitB), has been discovered targeting Microsoft 365 users. The attack uses fake login popups that closely resemble legitimate browser authentication windows, making it difficult for victims to distinguish between real and fake login pages. The phishing page is embedded within a webpage and presents a spoofed Microsoft OAuth URL and login form when a user clicks a Microsoft sign-in button.

The fake login popup is particularly convincing, as it behaves like a legitimate browser window, allowing users to drag it around the screen and including controls such as back, refresh, minimize, and close buttons. The phishing page also adapts to the victim's environment, identifying the operating system and browser in use and adjusting its appearance to match. This makes it even more challenging for users to spot the fake login page. Additionally, the campaign uses techniques to evade detection and investigation, such as overriding browser console functions and redirecting suspected bots to a legitimate Microsoft Office help page.

The BitB phishing campaign is part of a larger trend of phishing attacks targeting Microsoft 365 users. Recently, the FBI warned about Kali365, a phishing-as-a-service platform that enables attackers to steal Microsoft 365 access tokens and bypass multi-factor authentication (MFA) through device code phishing. To protect themselves, Microsoft 365 users should be cautious when encountering login prompts and verify the authenticity of the page before entering their credentials. Palo Alto Networks Unit 42 has published a list of domains associated with the campaign to help users and organizations stay vigilant and prevent falling victim to this phishing attack.

---

> *We cannot direct the wind but we can adjust the sails.*

Source: [New Browser-in-the-Browser phishing uses fake login popups to steal Microsoft 365 credentials](https://www.helpnetsecurity.com/2026/06/10/browser-in-the-browser-phishing-microsoft-365-users/)
