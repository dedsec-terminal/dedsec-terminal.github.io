---
title: "Frontier AI models collapse under multi-turn AI attacks, Cisco finds"
date: 2026-05-28T05:30:10+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Vulnerability of AI Models to Multi-Turn Attacks**
Cisco's AI threat intelligence team has found that large language models are vulnerable to multi-turn attacks, where attackers reframe, build context, and escalate their requests over multiple turns. The research tested 15 flagship models from leading AI companies, including OpenAI, Anthropic, and Google, and found that multi-turn attack success rates were significantly higher than single-turn rates, with some models failing up to 88% of the time.

**Gap Between Published Scores and Observed Resilience**
The study revealed a wide gap between published single-turn benchmark scores and observed resilience to multi-turn attacks. Every model in the cohort failed a significant number of multi-turn attacks, with some models showing a ninefold increase in failure rates under iterative pressure. The research also found that configuration-driven safety variations, such as enabling or disabling reasoning modes, can significantly impact a model's vulnerability to multi-turn attacks.

**Recommendations for Improved AI Security**
To address these vulnerabilities, the Cisco team recommends that organizations buying or deploying AI models publish attack success rates by strategy family, gate deployments on regressions in top procedures and content types, and flag models with significant cross-regime gaps for manual review. Regulatory frameworks, such as the NIST AI Risk Management Framework and the EU AI Act, also emphasize the need for adversarial robustness testing, but currently lack specificity on interaction regimes and strategy decomposition. By taking these steps, organizations can better assess and mitigate the risks associated with AI model vulnerabilities.

---

> *How many cares one loses when one decides not to be something but to be someone.
Author: Coco Chanel*

Source: [Frontier AI models collapse under multi-turn AI attacks, Cisco finds](https://www.helpnetsecurity.com/2026/05/28/cisco-multi-turn-ai-attacks/)
