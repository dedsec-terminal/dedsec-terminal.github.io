---
title: "New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials"
date: 2026-06-30T08:37:19+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers at LayerX have discovered a new attack technique called BioShocking, which tricks AI browsers into leaking user credentials. The attack works by convincing the AI browser that it is playing a game, and then manipulating it into copying and sending sensitive information to an attacker. The technique was successful against six AI browsers and assistants, including OpenAI's ChatGPT Atlas, Perplexity's Comet, and Anthropic's Claude browser extension.

The BioShocking attack exploits a vulnerability in how AI browsers read and process text. By creating a malicious web page that appears to be a game, an attacker can inject commands that are disguised as ordinary content or game rules. The AI browser, unable to distinguish between legitimate and malicious commands, will follow the game logic and execute the attacker's instructions. In a test, the attack was able to trick an AI browser into pulling SSH login credentials from a victim's work GitHub repository and passing them to the attacker.

To prevent such attacks, LayerX recommends that AI browsers be designed to ask for user permission before reading from logged-in accounts and to notice when a page is attempting to manipulate its behavior. Users are advised to treat agent mode with care and limit the access of AI browsers to sensitive information. Security teams should also be aware of the potential risks of AI browsers and grant them only the narrowest access necessary to perform specific tasks. By taking these precautions, users and organizations can reduce the risk of falling victim to BioShocking and other similar attacks.

---

> *Everyone can taste success when the going is easy, but few know how to taste victory when times get tough.
Author: Byron Pulsifer*

Source: [New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials](https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html)
