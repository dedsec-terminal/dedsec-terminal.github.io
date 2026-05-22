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

1. **Malicious Extension**: The poisoned extension was available on the Visual Studio Marketplace for only 18 minutes, but it was enough to distribute a credential stealer capable of harvesting sensitive data.
2. **Impact**: GitHub has no evidence of impact to customer information stored outside of its internal repositories, but some internal repositories contain customer information, such as support interactions.
3. **Response**: GitHub has taken steps to contain the incident, rotated critical secrets, and is continuing to monitor the situation for follow-on activity.
4. **Threat Actor**: TeamPCP has gained notoriety for large-scale software supply chain attacks, targeting widely-used open-source projects and security-adjacent tools.
5. **Security Concerns**: The incident highlights the need for deeper, more fundamental changes to securing developer tooling and open source distribution, as well as the risks associated with auto-update features in extension marketplaces.

**Quotes:**

* "This incident highlights that there need to be deeper, more fundamental changes to how we and other maintainers need to think about securing developer tooling and open source distribution." - Jeff Cross, co-founder of Narwhal Technologies
* "The trade-off stops making sense once you account for hostile/compromised publishers. Auto-update gives an attacker who controls a release a direct push channel into every machine running that extension." - Raphael Silva, Aikido security researcher

---

> *Today is the tomorrow you worried about yesterday.*

Source: [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
