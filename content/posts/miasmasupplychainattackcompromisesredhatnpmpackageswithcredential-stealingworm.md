---
title: "Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm"
date: 2026-06-01T17:40:28+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A new supply chain attack campaign, codenamed Miasma, has compromised several Red Hat npm packages, including `@redhat-cloud-services/vulnerabilities-client` and `@redhat-cloud-services/topological-inventory-client`. The attack is similar to the Mini Shai-Hulud campaign, using tactics such as install-time execution, credential harvesting, and encrypted exfiltration. The malware contains an obfuscated preinstall hook designed to collect sensitive information, including GitHub Actions secrets, npm tokens, and cloud credentials.

The malware transmits the stolen data to a server and uses GitHub as a fallback mechanism, committing the encrypted result through the GitHub API. It also attempts to avoid execution on Russian-language systems and establishes persistence by injecting hooks into developer tools. The attack is believed to have started on May 29, 2026, and has been found to generate a uniquely encrypted payload for each infection, making detection and version tracking challenging. The compromise of a Red Hat employee's GitHub account is thought to be the initial point of infection.

To mitigate the attack, it is recommended to isolate affected hosts, remove malicious versions, rotate exposed credentials, and review for suspicious activity. Uninstalling the npm package or deleting node_modules is not considered sufficient cleanup due to the malware's background execution and persistence mechanisms. CI/CD systems should suspend affected workflow runs, invalidate build artifacts, and review release, container image, npm package, or deployment artifacts created after the malicious package was installed. Strong access controls should be enforced to prevent further compromise.

---

> *By believing passionately in something that does not yet exist, we create it.
Author: Nikos Kazantzakis*

Source: [Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing Worm](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html)
