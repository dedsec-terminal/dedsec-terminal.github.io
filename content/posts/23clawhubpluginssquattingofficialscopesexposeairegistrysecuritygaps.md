---
title: "23 ClawHub plugins squatting official scopes expose AI registry security gaps"
date: 2026-06-22T08:00:11+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

A security vulnerability was discovered in the ClawHub registry, which is used by AI agents such as Claude and OpenClaw. The issue arose from the use of npm-style scopes, such as @openclaw/ and @clawhub/, which are meant to indicate the publisher of a package. However, these official scopes were not reserved for their owners, allowing unrelated accounts to publish packages under these scopes.

As a result, 23 code-executing plugins were found to be published under the official @openclaw and @clawhub scopes, despite being owned by unrelated accounts. This poses a significant supply chain risk, even if the code itself is not malicious. The use of an official-looking scope can create a false sense of trust, making it more likely for users to install and execute the plugins. This highlights the importance of securing AI registries and ensuring that official scopes are properly reserved.

Following the disclosure of this vulnerability, the ClawHub registry made changes to address the issue. The incident also highlights a broader pattern of security gaps emerging alongside new AI tools, assets, and registries. As the use of AI continues to grow, it is essential to prioritize security and ensure that these new technologies are developed and deployed with robust security measures in place. This includes securing registries, validating packages, and educating users about the potential risks associated with AI-powered tools.

---

> *The amount of happiness that you have depends on the amount of freedom you have in your heart.
Author: Thich Nhat Hanh*

Source: [23 ClawHub plugins squatting official scopes expose AI registry security gaps](https://www.helpnetsecurity.com/2026/06/22/clawhub-code-executing-plugins-video/)
