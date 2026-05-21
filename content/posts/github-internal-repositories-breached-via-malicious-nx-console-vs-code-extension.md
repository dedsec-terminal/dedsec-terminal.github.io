---
title: "GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension"
date: 2026-05-21T04:27:01+00:00
draft: false
categories:
  - malware
---

**GitHub Internal Repositories Breach**

GitHub has confirmed a breach of its internal repositories due to a malicious version of the Nx Console VS Code extension. The breach occurred when an employee's device was compromised, allowing the threat actor, TeamPCP, to exfiltrate approximately 3,800 repositories. The incident is linked to the recent TanStack supply chain attack, which also affected other companies such as OpenAI, Mistral AI, and Grafana Labs.

**Key Facts:**

1. The malicious extension, nrwl.angular-console, was available on the Visual Studio Marketplace for only 18 minutes before being removed.
2. The extension was able to harvest sensitive data from 1Password vaults, Anthropic Claude Code configurations, npm, GitHub, and Amazon Web Services (AWS).
3. The breach allowed TeamPCP to gain access to GitHub's internal repositories, which may contain customer information, such as support interaction excerpts.
4. GitHub has taken steps to contain the incident, rotated critical secrets, and is monitoring for follow-on activity.

**Impact and Concerns:**

1. The breach highlights the need for deeper changes in securing developer tooling and open-source distribution.
2. The incident demonstrates the interlinked nature of modern software, allowing TeamPCP to unleash a self-sustaining cycle of new compromises.
3. The use of auto-update features in extension marketplaces, such as VS Code, can provide a direct push channel for attackers to compromise machines running the extension.

**Response and Next Steps:**

1. GitHub will notify customers if any impact is discovered through established incident response and notification channels.
2. The Nx team is beginning conversations with other high-profile open-source maintainers to address deeper structural problems around software supply chain security.
3. The incident emphasizes the importance of securing developer tooling and open-source distribution to prevent similar breaches in the future.

---

> *Men of perverse opinion do not know the excellence of what is in their hands, till some one dash it from them.
Author: Sophocles*

Source: [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
