---
title: "OAuth marketplace apps keep access after publishers vanish"
date: 2026-06-04T12:00:22+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

An audit by OhAuth, an OAuth research project, found that many marketplace apps on Google Workspace and GitHub retain access to company data even after the publisher is no longer present. The audit covered 2,890 public OAuth app listings and found that nearly a third of them (32%) carry at least one structural exposure signal, such as scopes wider than the app's stated function or dead publisher websites. These signals pose a risk to companies, as a compromise of the publisher could turn a legitimate app into a supply-chain access path.

The audit found that 677 apps request permissions that exceed their stated function, with a combined lower-bound install footprint of 1.82 billion. For example, a multiple-choice form helper with over 8 million installs holds off-purpose Drive, Forms, and Sheets scopes. The audit also found that 206 apps have dead publisher domains, and 89 apps have domains available for purchase, which could allow an attacker to take over the app. Additionally, 36 apps have publisher domains flagged on commercial threat-intel blocklists. These findings highlight the need for continuous monitoring and review of OAuth grants, as a one-time check at approval time is not sufficient.

To mitigate these risks, Offroad recommends that administrators treat OAuth grants as part of identity risk management. This includes inventorying every grant, monitoring high-privilege actions continuously, separating AI apps from traditional ones, and rotating top-risk grants on a fixed schedule. Administrators should also conduct a tenant-level security evaluation of scope, publisher, purpose, usage, and business owner for each app. By taking these steps, companies can reduce the risk of unauthorized access to their data and prevent potential security breaches.

---

> *He who fears being conquered is sure of defeat.
Author: Napoleon Bonaparte*

Source: [OAuth marketplace apps keep access after publishers vanish](https://www.helpnetsecurity.com/2026/06/04/oauth-marketplace-apps-audit/)
