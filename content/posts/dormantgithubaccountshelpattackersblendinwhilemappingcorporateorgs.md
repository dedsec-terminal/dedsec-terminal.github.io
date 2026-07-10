---
title: "Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs"
date: 2026-07-09T18:38:49+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Datadog Security Labs has identified a series of campaigns targeting corporate GitHub organizations, repositories, and user accounts through the GitHub API. The attackers are using a combination of automated scraping tools, dormant "ghost" accounts, and compromised OAuth tokens and personal access tokens (PATs) to gather information. These ghost accounts, which were created two to five years ago, were intentionally left inactive before being used to issue API traffic, allowing the attackers to blend in with legitimate activity.

The attackers are using these accounts to enumerate public data, including listing public repositories, walking user followers and following lists, and enumerating gists, starred repos, and org memberships. They are also running GraphQL queries against public objects, which can be used to map out an organization's GitHub-related activity. This information can be used for reconnaissance, allowing the attackers to identify potential targets and vulnerabilities. While most of the activity involves targeting public data, some instances have gone beyond public information enumeration to successfully clone private repositories.

The use of dormant accounts and compromised tokens allows the attackers to avoid raising red flags, as the activity appears to be legitimate. Datadog notes that individually, most of these requests are unremarkable, but the aggregate activity is concerning. The attackers' ability to clone private repositories in some cases highlights the potential risks of this campaign. The use of custom tooling and the iteration of attacks over weeks suggests a sophisticated and targeted approach, emphasizing the need for organizations to be aware of these campaigns and take steps to protect their GitHub accounts and data.

---

> *Action may not always bring happiness, but there is no happiness without action.
Author: Benjamin Disraeli*

Source: [Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs](https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html)
