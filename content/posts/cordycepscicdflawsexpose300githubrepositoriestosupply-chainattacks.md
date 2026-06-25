---
title: "Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks"
date: 2026-06-24T12:48:11+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

**Introduction to Cordyceps Vulnerability**
Cybersecurity researchers at Novee Security have discovered a critical exploitable pattern in CI/CD workflows, codenamed Cordyceps. This vulnerability allows attackers to hijack workflows and compromise open-source supply chains, potentially giving them full control over repositories. The issue can be exploited by any unauthenticated user with a free account, enabling them to forge approvals, push code, or steal credentials.

**Impact and Exploitation**
The Cordyceps vulnerability affects over 300 GitHub repositories, including those of major organizations such as Microsoft, Google, Apache, and Cloudflare. Weak CI/CD configurations grant pull requests more permissions than they should have, allowing untrusted PRs to trigger privileged workflows and enabling command injection, privilege escalation, and supply chain compromise. Novee Security's scan of 30,000 high-impact repositories revealed that many are fully exploitable, allowing attacker-controlled code execution, credential theft, and supply chain compromise.

**Response and Mitigation**
Following responsible disclosure, affected organizations have confirmed the impact and applied patches or hardening measures to mitigate the vulnerability. The findings highlight the need for more secure CI/CD configurations and auditing of trust boundaries to prevent similar vulnerabilities. The Cordyceps vulnerability has significant implications for the open-source software supply chain, and its exploitation could have severe downstream impacts. As Novee Security's Elad Meged noted, the vulnerability allows attackers to "puppeteer" repositories, silently manipulating workflows and gaining control over the software supply chain.

---

> *It is the quality of our work which will please God, not the quantity.
Author: Mahatma Gandhi*

Source: [Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks](https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html)
