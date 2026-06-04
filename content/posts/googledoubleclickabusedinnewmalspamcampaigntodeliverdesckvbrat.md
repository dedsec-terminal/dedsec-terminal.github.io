---
title: "Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT"
date: 2026-06-03T16:29:16+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Cybersecurity researchers have identified a new malspam campaign that utilizes Google's DoubleClick domain to evade detection and deliver a remote access trojan (RAT) called DesckVB RAT. The campaign begins with a phishing email containing an HTML file that redirects the user to a Google DoubleClick Campaign Manager click-tracking URL, and then to a landing page with a "Download PDF" button. This button triggers a ZIP archive download, initiating the infection chain.

The infection chain involves a JavaScript loader that retrieves and executes a .NET RAT, while evading security controls. The loader verifies it's not being analyzed, neutralizes security controls, sets up persistence, and downloads the RAT payload using process hollowing. Once launched, the trojan communicates with a command-and-control server, carries out system reconnaissance, and configures Microsoft Defender exclusions. The malware also extracts data, runs commands, and deploys additional payloads, granting attackers full control over infected machines.

To prevent such attacks, researchers recommend a defense-in-depth approach, including configuring Group Policy Objects to force script files to open in Notepad by default. Additionally, organizations should deploy DMARC, DKIM, and SPF records to reduce the likelihood of spoofed or malicious emails reaching end users. An email gateway solution capable of sandboxing attachments and links before delivery can also add a meaningful layer of protection. By taking these measures, organizations can prevent threats like DesckVB RAT from being dropped and reduce the risk of infection.

---

> *Do not go where the path may lead, go instead where there is no path and leave a trail.
Author: Ralph Emerson*

Source: [Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT](https://thehackernews.com/2026/06/google-doubleclick-abused-in-new.html)
