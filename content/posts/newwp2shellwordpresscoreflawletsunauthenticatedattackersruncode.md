---
title: "New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code"
date: 2026-07-17T21:20:10+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A critical vulnerability, known as wp2shell, has been discovered in the WordPress core, allowing unauthenticated attackers to run code on a WordPress site with no preconditions. The flaw, found by Adam Kues at Assetnote, affects WordPress versions 6.9.0 through 6.9.4 and 7.0.0 through 7.0.1, and can be exploited by an anonymous user. WordPress has released updates 6.9.5 and 7.0.2 to fix the issue, which is described as a REST API batch-route confusion and SQL injection issue leading to Remote Code Execution.

The vulnerability is significant, as it can be exploited by a simple HTTP request, and over 500 million websites run WordPress. However, not all of these sites are vulnerable, as the flawed code only exists in versions 6.9 and later. WordPress has enabled forced updates through its auto-update system to patch the issue, but it is unclear whether this will reach sites that have turned off auto-updates. Site owners can check their version and update manually if necessary. A checker is also available at wp2shell.com to test for the vulnerability.

Until an update can be applied, several mitigation options are available, including blocking access to the batch endpoint at a web application firewall (WAF), disabling the WP REST API, or using a short drop-in plugin to reject anonymous requests. No exploitation attempts have been reported as of yet, but the lack of a CVE ID and CVSS score means that many scanners and inventories will not flag this issue. As a result, defenders are relying on the speed of the patch rollout to protect sites before attackers can exploit the vulnerability.

---

> *To understand the heart and mind of a person, look not at what he has already achieved, but at what he aspires to do.
Author: Kahlil Gibran*

Source: [New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)
