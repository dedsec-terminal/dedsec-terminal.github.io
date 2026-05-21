---
title: "Highly Critical Drupal Core Flaw Exposes PostgreSQL Sites to RCE Attacks"
date: 2026-05-21T03:44:11+00:00
draft: false
categories:
  - cves
---

A highly critical security vulnerability (CVE-2026-9082) has been discovered in Drupal Core, affecting sites that use PostgreSQL databases. The vulnerability, with a CVSS score of 6.5, allows attackers to send specially crafted requests, leading to arbitrary SQL injection, information disclosure, privilege escalation, and remote code execution (RCE) attacks. 

The flaw can be exploited by anonymous users and is fixed in the following Drupal versions:
- Drupal 11.3.10
- Drupal 11.2.12
- Drupal 11.1.10
- Drupal 10.6.9
- Drupal 10.5.10
- Drupal 10.4.10

Drupal 7 is not affected. Manual patches are also available for end-of-life versions 9 and 8. Users of unsupported versions (Drupal 11.1.x, 11.0.x, 10.4.x, and below, as well as Drupal 8 and 9) are advised to upgrade to a supported version as they do not receive security coverage and may have other unpatched vulnerabilities.

---

> *Money was never a big motivation for me, except as a way to keep score. The real excitement is playing the game.
Author: Donald Trump*

Source: [Highly Critical Drupal Core Flaw Exposes PostgreSQL Sites to RCE Attacks](https://thehackernews.com/2026/05/highly-critical-drupal-core-flaw.html)
