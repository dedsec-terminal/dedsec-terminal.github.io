---
title: "Klue breach lead to Salesforce data theft, Huntress affected"
date: 2026-06-19T12:57:39+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

A breach at Klue, a market intelligence platform, has led to the theft of Salesforce data, affecting multiple companies including cybersecurity vendor Huntress. The breach occurred when attackers gained access to Klue's backend infrastructure using a dormant API credential, which was then used to push a malicious code update designed to harvest OAuth tokens. These tokens were used to query customer CRM systems, including Salesforce, and exfiltrate data.

The attackers, attributed to the extortion group "Icarus," made off with business contacts, price quotes, and other sales-related data, but not sensitive information such as passwords or payment card details. Huntress has shared indicators of compromise and recommended that other Klue customers review logs and consider revoking active sessions tied to the compromised integrations. Several other security vendors, including Recorded Future, Tanium, and Jamf, have also been affected and have released official statements.

Salesforce has disabled the connection between the Klue Battlecards app and its platform, and Klue has revoked affected credentials and tokens, removed unauthorized code, and started an investigation. Law enforcement has been notified, and affected customers have been contacted and provided with information to aid in their own incident response. The breach highlights the risk of targeting trusted third-party integrations, which has been a pattern of attacks in 2025, with other Salesforce-connected SaaS integrations such as Drift and Gainsight also being hit by OAuth-abuse campaigns.

---

> *Happiness is found in doing, not merely possessing.
Author: Napoleon Hill*

Source: [Klue breach lead to Salesforce data theft, Huntress affected](https://www.helpnetsecurity.com/2026/06/19/klue-salesforce-data-breach-huntress/)
