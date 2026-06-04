---
title: "Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for Five Months"
date: 2026-06-04T09:33:57+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A senior executive at a major global stock exchange was the target of a sophisticated cyber attack, with hackers gaining access to their Outlook mailbox for at least five months. The attackers, whose identities remain unknown, used the access to copy the executive's emails in small batches, routing them through Dropbox and OneDrive to blend in with normal cloud activity. This campaign, reported by Symantec and Carbon Black's Threat Hunter Team, appears to be a case of espionage rather than a financially motivated attack.

The attackers' goal was likely to gather intelligence on the executive's dealings and the organization's plans, including non-public listing details, enforcement matters, and market-moving information. They achieved this by using a custom-built mailbox stealer, which converted the Outlook mailbox to a PST file and uploaded it to Dropbox and OneDrive. The attackers used legitimate cloud services and scheduled tasks to make their activity appear ordinary, avoiding detection by security software. The first malicious activity was detected on October 10, 2025, but the attackers had already gained full control of the machine by then.

The attack highlights the importance of monitoring and response in preventing such breaches, as there is no patch or fix that can close this type of vulnerability. The attackers' use of public tooling and consumer cloud services made it difficult to attribute the activity to a known group. To defend against similar attacks, organizations should watch for unusual mailbox export activity, odd Outlook access, and uploads to personal cloud accounts, as well as unexpected tunneling and credential-dumping on systems tied to privileged users. By feeding in the hashes and monitoring for suspicious behavior, organizations can reduce the risk of similar attacks.

---

> *It's important to know that words don't move mountains. Work, exacting work moves mountains.
Author: Danilo Dolci*

Source: [Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for Five Months](https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html)
