---
title: "n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer"
date: 2026-07-16T13:33:25+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

A security flaw was discovered in the n8n workflow automation platform, specifically in its token exchange feature. The issue allowed an attacker to log in as a user from another issuer, without needing their password. This was possible because n8n matched an incoming JWT (JSON Web Token) to a local user based on the "sub" claim alone, ignoring the "iss" (issuer) claim. This meant that a valid token from one issuer could be used to log in as a user from another issuer, if the "sub" values matched.

The flaw, tracked as CVE-2026-59208, was reported by a GitHub user and was fixed by n8n on June 24. The issue only affects n8n Enterprise instances that have token exchange enabled and trust multiple external token issuers. The token exchange feature is still in preview and is primarily used by OEM partners who embed the n8n product. The vulnerability allows an attacker to obtain a token and use it to log in as a user from another issuer, although the exact mechanism for obtaining the token is not specified.

To mitigate the issue, users can either patch their n8n instance to version 2.27.4 or 2.28.1, or reduce the number of trusted issuers to one, or disable the token exchange feature altogether. The advisory notes that neither of the latter two measures fully remediates the risk, but they can be used as short-term measures until a patch can be applied. The fix is not mentioned in the release notes, so users who rely on changelogs for upgrade decisions may miss this important security update.

---

> *Aim for success, not perfection. Never give up your right to be wrong, because then you will lose the ability to learn new things and move forward with your life.
Author: Dr. David M. Burns*

Source: [n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer](https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html)
