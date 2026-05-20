---
title: "Grafana GitHub Breach Exposes Source Code via TanStack npm Attack"
date: 2026-05-20
draft: false
categories:
  - threat-intelligence
author: "DedSec-Terminal"
---

Grafana Labs, on May 19, 2026, said an investigation into its recent breach found no evidence of customer production systems or operations being compromised.

It said the scope of the incident is limited to the Grafana Labs GitHub environment, which includes public and private source code along with internal GitHub repositories.

"After the initial assessment, we found that in addition to source code, the downloaded content included GitHub repositories that some Grafana Labs teams use to collaborate on and store internal operational information and other details about our business," it said.

"This includes business contact names and email addresses that would be exchanged in a professional relationship context, not information pulled from or processed through the use of production systems or the Grafana Cloud platform."

The open-source visualization software maker also noted that the breach originated from the TanStack npm supply chain attack orchestrated by TeamPCP, which also hit OpenAI and Mistral AI, and that it detected the activity on May 11, 2026.

"We performed analysis and quickly rotated a significant number of GitHub workflow tokens, but a missed token led to the attackers gaining access to our GitHub repositories," it said. "A subsequent review confirmed that a specific GitHub workflow we originally deemed not impacted had, in fact, been compromised."

*The bamboo that bends is stronger than the oak that resists. — Japanese saying*

Source: [The Hacker News](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html) · [Read Original →](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)
