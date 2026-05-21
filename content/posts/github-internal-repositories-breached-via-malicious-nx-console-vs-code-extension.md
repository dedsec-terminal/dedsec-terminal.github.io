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

1. **Malicious Extension**: The poisoned extension was live on Visual Studio Marketplace for only 18 minutes, but it was enough to distribute a credential stealer capable of harvesting sensitive data.
2. **Impact**: GitHub has no evidence of impact to customer information stored outside of its internal repositories, but some internal repositories contain customer information, such as support interactions.
3. **Response**: GitHub has taken steps to contain the incident, rotated critical secrets, and is continuing to monitor the situation.
4. **Threat Actor**: TeamPCP, a cybercriminal group, has gained notoriety for large-scale software supply chain attacks, targeting widely-used open-source projects and security-adjacent tools.
5. **Supply Chain Security**: The incident highlights the need for deeper, more fundamental changes to how developer tooling and open-source distribution are secured.

**Concerns and Implications:**

1. **Auto-Update Vulnerability**: The default auto-update feature in extension marketplaces, such as VS Code, can provide a direct push channel for attackers to compromise machines running the extension.
2. **Interlinked Nature of Software**: The breach demonstrates how the interlinked nature of modern software can allow attackers to unleash a self-sustaining cycle of new compromises.
3. **Need for Structural Changes**: The incident emphasizes the need for high-profile open-source maintainers to work together to address deeper structural problems around software supply chain security.

---

> *A man should look for what is, and not for what he thinks should be.
Author: Albert Einstein*

Source: [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
