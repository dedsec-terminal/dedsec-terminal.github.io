---
title: "GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension"
date: 2026-05-21T04:27:01+00:00
draft: false
categories:
  - malware
---

**GitHub Internal Repositories Breach**

GitHub has confirmed a breach of its internal repositories due to a malicious version of the Nx Console VS Code extension. The extension, nrwl.angular-console, was compromised after one of its developers' systems was hacked in the wake of the recent TanStack supply chain attack. The breach allowed the threat actor, TeamPCP, to exfiltrate approximately 3,800 repositories.

**Key Points:**

1. **Malicious Extension**: The poisoned extension was live on Visual Studio Marketplace for only 18 minutes, but it was enough to distribute a credential stealer capable of harvesting sensitive data from various sources.
2. **Impact**: GitHub has no evidence of impact to customer information stored outside of its internal repositories, but some internal repositories may contain customer information, such as support interactions.
3. **Response**: GitHub has taken steps to contain the incident, rotated critical secrets, and is continuing to monitor the situation for follow-on activity.
4. **Threat Actor**: TeamPCP, a cybercriminal group, has gained notoriety for large-scale software supply chain attacks, targeting widely-used open-source projects and security-adjacent tools.
5. **Security Concerns**: The incident highlights the need for deeper, more fundamental changes to how developer tooling and open source distribution are secured, as well as the risks associated with auto-update features in extension marketplaces.

**Recommendations:**

1. **Developer Awareness**: Developers should be cautious when installing and updating extensions, and consider disabling auto-update features to prevent potential security risks.
2. **Marketplace Security**: Extension marketplaces should impose review gates and waiting periods between updates to prevent malicious publishers from pushing compromised code to users.
3. **Collaboration**: Open-source maintainers and security experts should work together to address the deeper structural problems around software supply chain security.

---

> *If you look into your own heart, and you find nothing wrong there, what is there to worry about? What is there to fear?
Author: Confucius*

Source: [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
