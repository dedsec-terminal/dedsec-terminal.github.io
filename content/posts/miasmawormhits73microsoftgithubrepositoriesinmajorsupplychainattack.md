---
title: "Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack"
date: 2026-06-06T06:58:04+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Microsoft's GitHub repositories have been hit by the Miasma self-replicating supply chain attack campaign, impacting 73 repositories across four organizations, including Azure, Azure-Samples, Microsoft, and MicrosoftDocs. The attack has led to GitHub disabling access to the affected repositories, with a message indicating a violation of GitHub's terms of service. The repositories affected include various Azure and Microsoft projects, such as azure-search-openai-demo-purviewdatasecurity, Connectors-NET-LSP, and durabletask.

The Miasma campaign is notable for its re-compromise of the "durabletask" PyPI package, which was previously infected by TeamPCP to deliver an information stealer on Linux systems. Security researchers believe that the same credentials used in the previous attack may still be held by the attackers, allowing them to reopen the same vulnerability. Miasma is assessed to be a variant of the Mini Shai-Hulud worm, which has continued to mutate and refine its tactics, infecting more packages and using various descriptions for the newly-created public repositories containing stolen secrets.

The attack has exposed weaknesses in the trust model of open-source ecosystems, making it one of the most significant and sustained campaigns observed to date. The Miasma worm operates entirely within legitimate channels, exploiting the trust model of platforms like GitHub and npm by compromising the key and maintainer, then acting as a legitimate publisher. This allows the worm to propagate exponentially across the ecosystem, compromising downstream users and repeating the same cycle. Conventional defenses have largely failed to stop the attack, as it does not exploit a vulnerability in the platforms, but rather the assumption that a package is safe if it is signed with a valid key and published by an authenticated maintainer.

---

> *When performance exceeds ambition, the overlap is called success.
Author: Cullen Hightower*

Source: [Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)
