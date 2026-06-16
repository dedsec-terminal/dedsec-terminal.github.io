---
title: "Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails"
date: 2026-06-15T19:44:06+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A China-linked espionage group, known as UNC6508, has been found to have infiltrated North American medical, academic, and military research networks for over a year. The group used a backdoor on REDCap research servers to steal login credentials, and then exploited Google Workspace rules to copy sensitive emails to an inbox they controlled. This was done by creating a content compliance rule that watched for specific keywords and email addresses, and then silently forwarded matching messages to the attacker-controlled Gmail address.

The attackers gained initial access to the networks through compromised REDCap servers, which are used to build and manage study databases. They then deployed custom malware, known as INFINITERED, which hijacked the upgrade process, harvested usernames and passwords, and acted as a backdoor. The group used the stolen credentials to move laterally within the network and gain domain administrator access, which allowed them to set up the email exfiltration mechanism. The earliest known compromise dates back to September 2023, and activity continued until November 2025.

To prevent similar attacks, organizations are advised to patch and secure their REDCap servers, review their Google Workspace content compliance and mail-forwarding rules, and implement phishing-resistant multi-factor authentication (MFA) on administrator accounts. It is also recommended to hunt for indicators of the INFINITERED malware and to monitor admin audit logs for any suspicious changes to mail rules. The use of built-in cloud features, such as content compliance rules, as an exfiltration path is a new tactic that defenders need to be aware of, and regular audits and monitoring are necessary to detect and prevent such attacks.

---

> *Our lives are a sum total of the choices we have made.
Author: Wayne Dyer*

Source: [Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails](https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html)
