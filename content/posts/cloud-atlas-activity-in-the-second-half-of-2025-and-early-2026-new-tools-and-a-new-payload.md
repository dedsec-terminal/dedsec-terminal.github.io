---
title: "Cloud Atlas activity in the second half of 2025 and early 2026: new tools and a new payload"
date: 2026-05-22T09:12:13+00:00
draft: false
categories:
  - cves
---

The article discusses the recent activities of the Cloud Atlas APT group, a cyber threat actor that has been active since 2014. The group has been observed using new tools and techniques to target government agencies and diplomatic entities in Russia and Belarus. The main findings of the article are:

1. **Initial Infection**: Cloud Atlas uses phishing emails with malicious attachments, such as ZIP archives containing LNK files, to gain initial access to victim systems.
2. **Malicious Payload**: The LNK files execute PowerShell scripts that download and install additional malware, including the VBCloud and PowerShower backdoors.
3. **VBCloud Backdoor**: This backdoor is designed to steal files with specific extensions (e.g., DOC, PDF, XLS) and exfiltrate them to the attackers' command and control (C2) server.
4. **PowerShower Backdoor**: This backdoor is used for network reconnaissance and lateral movement within the victim's infrastructure. It can collect information about running processes, administrator groups, and domain controllers, and conduct "Kerberoasting" attacks to steal password hashes.
5. **Reverse SSH Tunneling**: Cloud Atlas uses reverse SSH tunnels to maintain access to compromised systems and bypass firewall rules.
6. **Patched OpenSSH**: The group uses modified OpenSSH binaries to evade detection and ensure stealth.
7. **RevSocks**: Cloud Atlas also uses RevSocks, a tool written in Golang, to establish tunnels and proxy connections.
8. **Tor Tunneling**: The group uses the Tor network to maintain control over compromised hosts and access them via RDP.
9. **New Tools**: Cloud Atlas has developed new tools, such as PowerCloud, which collects user data with administrator privileges and writes it to Google Sheets in Base64 format.
10. **Victims**: The group's targets are primarily government agencies and diplomatic entities in Russia and Belarus.

The article concludes that Cloud Atlas continues to evolve and expand its arsenal, using new tools and techniques to target its victims. The group's activities are attributed to the Cloud Atlas APT group with a high degree of confidence, based on the use of similar techniques and tools in the past.

---

> *It isn't where you come from, it's where you're going that counts.
Author: Ella Fitzgerald*

Source: [Cloud Atlas activity in the second half of 2025 and early 2026: new tools and a new payload](https://securelist.com/cloud-atlas-2026/119895/)
