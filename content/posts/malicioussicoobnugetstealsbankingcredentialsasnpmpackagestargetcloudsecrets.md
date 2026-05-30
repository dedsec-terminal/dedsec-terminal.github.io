---
title: "Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets"
date: 2026-05-29T09:11:25+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Malicious NuGet Package Targets Sicoob Banking Credentials**: Cybersecurity researchers have discovered a malicious NuGet package, "Sicoob.Sdk", that steals client IDs and PFX certificates from Sicoob, a Brazilian cooperative financial system. The package, which has been downloaded nearly 500 times, contains functionality to exfiltrate sensitive information, including PFX certificates used to authenticate businesses with the Sicoob banking network. This can potentially expose sensitive transaction details and payment status.

**npm Packages Target Cloud Secrets**: In a separate incident, 14 malicious npm packages have been discovered that typosquat well-known libraries to harvest AWS credentials, HashiCorp Vault tokens, and CI/CD pipeline secrets. The packages, published by a single threat actor, use a purpose-built credential harvester launched through a preinstall hook to steal sensitive information. This is part of a larger trend of supply chain attacks targeting the npm ecosystem, with multiple campaigns discovered in recent days, including packages that abuse npm for ad-monetized web proxies and those that employ dependency confusion to distribute malicious payloads.

**Broader Implications and Recommendations**: The discovery of these malicious packages highlights the growing threat of supply chain attacks, which can have severe consequences for organizations and individuals. To mitigate these risks, organizations are advised to immediately remove the "Sicoob.Sdk" package, treat PFX material as compromised, and audit Sicoob authentication and API logs for signs of unusual activity. Developers are also warned to be cautious when installing packages, especially those with similar names to legitimate libraries, and to verify the authenticity of packages before use. The incidents demonstrate the importance of vigilant security practices and the need for continuous monitoring of software ecosystems to prevent and detect malicious activity.

---

> *Until you make peace with who you are, you will never be content with what you have.
Author: Doris Mortman*

Source: [Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud Secrets](https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html)
