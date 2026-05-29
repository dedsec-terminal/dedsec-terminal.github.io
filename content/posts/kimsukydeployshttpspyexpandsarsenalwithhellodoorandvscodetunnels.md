---
title: "Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels"
date: 2026-05-29T05:57:41+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The North Korean state-sponsored threat actor Kimsuky has been attributed to a series of cyber attacks targeting South Korean military and corporate entities in March and April 2026. The attacks employed social engineering tactics, including spoofing security software installation pages and crafting a fake Webex meeting page, to deliver a variant of the HTTPSpy malware. The malware was disguised as installers from South Korean security software, and its primary responsibility was to launch a second-stage DLL payload and establish persistence on the host.

Kimsuky's tactics have evolved to include the use of sophisticated mechanisms to maximize delivery success, such as real-time infection verification via JSONPing and crafting fake pages using stolen meeting schedules. The threat actor has also been found to use Microsoft Visual Studio Code (VS Code) tunneling and Cloudflare Quick Tunnels to establish covert remote access to victim devices. Additionally, Kimsuky has been leveraging large language models (LLMs) and the Rust programming language in its latest campaigns, highlighting its continued adaptation and evolution.

The attacks have delivered a range of malware families, including PebbleDash and AppleSeed, which have been used to target various sectors in South Korea, including defense, government, and private entities. Notable malware variants include HelloDoor, HttpMalice, and HttpTroy, which support capabilities such as command execution, screenshot capture, and data exfiltration. Kimsuky's evolving tactics and techniques demonstrate its ability to adapt and refine its approaches to achieve its goals, making it a significant threat to organizations in South Korea and beyond.

---

> *Pick battles big enough to matter, small enough to win.
Author: Jonathan Kozol*

Source: [Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels](https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html)
