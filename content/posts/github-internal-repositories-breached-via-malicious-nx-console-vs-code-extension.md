---
title: "GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension"
date: 2026-05-21T04:27:01+00:00
draft: false
categories:
  - malware
---

**GitHub Internal Repositories Breach**

GitHub has confirmed a breach of its internal repositories due to a compromised employee device. The breach occurred when an employee installed a malicious version of the Nx Console VS Code extension, which was poisoned by a cybercriminal group known as TeamPCP. The extension, nrwl.angular-console, was compromised after one of its developers' systems was hacked in the wake of the recent TanStack supply chain attack.

**Key Facts:**

1. The breach allowed the threat actor to exfiltrate approximately 3,800 repositories.
2. GitHub has taken steps to contain the incident and rotated critical secrets.
3. The company has no evidence of impact to customer information stored outside of GitHub's internal repositories.
4. The malicious extension was live on Visual Studio Marketplace for only 18 minutes, but was enough to distribute a credential stealer capable of harvesting sensitive data.

**Attack Method:**

1. The attackers compromised the Nx Console extension by hacking into one of its developers' systems.
2. The poisoned extension was uploaded to the Visual Studio Marketplace, where it was available for 18 minutes.
3. During this time, the extension was downloaded and installed by some users, who unknowingly executed a hidden package that stole sensitive data.

**Consequences:**

1. The breach highlights the need for deeper, more fundamental changes to how developer tooling and open-source distribution are secured.
2. The incident demonstrates the interlinked nature of modern software, allowing attackers to unleash a self-sustaining cycle of new compromises.
3. The use of auto-update features in extension marketplaces can provide a direct push channel for attackers to compromise user machines.

**Response:**

1. GitHub is continuing to monitor the situation for follow-on activity.
2. The company is working with other high-profile open-source maintainers to address deeper structural problems around software supply chain security.
3. Users are advised to be cautious when installing extensions and to keep their software up to date to minimize the risk of compromise.

---

> *Almost everything comes from nothing.
Author: Henri Amiel*

Source: [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
