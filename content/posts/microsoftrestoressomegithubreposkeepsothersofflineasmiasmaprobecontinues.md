---
title: "Microsoft Restores Some GitHub Repos, Keeps Others Offline as Miasma Probe Continues"
date: 2026-06-09T16:34:52+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Microsoft has temporarily removed some GitHub repositories in response to a recent security incident that compromised 73 of its open-source projects. The incident, part of a software supply chain campaign codenamed Miasma, involved injecting an information stealer into the code. Microsoft's priority is to protect customers and the broader ecosystem, and some repositories have been restored after review, while others remain offline.

The Miasma campaign has been found to have capabilities to trigger automatic code execution when an unsuspecting developer opens the repository in an AI-powered coding tool or integrated development environment (IDE). Further analysis has uncovered a newer wave of infected packages, including bioinformatics-related libraries and AI-themed packages. These packages, such as dreamgen, embiggen, and langchain-core-mcp, have been found to contain malware capable of propagating to downstream users and beyond.

The threat actors behind the Miasma campaign are adapting and experimenting with different methods, including new payload delivery mechanisms and trojanized native extensions. The malware targets developer workstations and CI/CD environments, harvesting high-value secrets and exfiltrating them to a public GitHub repository. Researchers have warned that the campaign is "fast-moving" and not limited to a single package incident, emphasizing the need for continued vigilance and investigation to protect customers and the broader ecosystem.

---

> *Go put your creed into the deed. Nor speak with double tongue.
Author: Ralph Emerson*

Source: [Microsoft Restores Some GitHub Repos, Keeps Others Offline as Miasma Probe Continues](https://thehackernews.com/2026/06/microsoft-restores-some-github-repos.html)
