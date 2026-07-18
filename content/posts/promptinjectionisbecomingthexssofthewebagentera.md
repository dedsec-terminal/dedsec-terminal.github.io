---
title: "Prompt injection is becoming the XSS of the web agent era"
date: 2026-07-17T06:00:31+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

The rise of autonomous web agents has introduced a new security threat, dubbed Cross-Site Prompting (XSP), which is similar to Cross-Site Scripting (XSS). XSP occurs when an attacker injects malicious text into a webpage, which is then read by a web agent and executed as instructions. This can lead to unauthorized actions, such as sending sensitive user data to an attacker. Researchers at UC Berkeley have developed a system called Prismata, which filters and constrains web content to prevent XSP attacks.

Prismata works by analyzing the structure of a webpage and identifying potential injection points. It uses a reasoning model to determine whether a particular element, such as a button or form field, is relevant to the user's task. If the element is not relevant, Prismata blocks it from being executed by the web agent. The system also uses a no-read-down, no-write-up rule to prevent untrusted content from being executed. In tests, Prismata was able to block 99.3% of XSP attacks, and improved the success rate of web agents completing their tasks under attack from 5% to 24%.

While Prismata shows promise in preventing XSP attacks, it is not foolproof. The system relies on language models to label webpage elements, which can be imperfect. Additionally, well-structured webpages can reduce the risk of XSP attacks, but poorly structured sites can increase the vulnerability. The researchers acknowledge that determined attackers may still be able to find ways to bypass Prismata's defenses. Nevertheless, the development of Prismata highlights the importance of addressing XSP attacks, particularly for organizations that use web agents to handle sensitive user data.

---

> *Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared.
Author: Buddha*

Source: [Prompt injection is becoming the XSS of the web agent era](https://www.helpnetsecurity.com/2026/07/17/xss-web-agent-prompt-injection/)
