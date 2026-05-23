---
title: "LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root"
date: 2026-05-23T07:35:13+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A critical security vulnerability, tracked as CVE-2026-48172, has been discovered in the LiteSpeed User-End cPanel Plugin, with a CVSS score of 10.0. This flaw allows attackers to exploit incorrect privilege assignment, enabling them to run arbitrary scripts with elevated permissions as root. The vulnerability affects all versions of the plugin between 2.3 and 2.4.4, but not the LiteSpeed WHM plugin. Security researcher David Strydom is credited with discovering and reporting the issue, which has been addressed in version 2.4.5 of the plugin.

The vulnerability is being actively exploited, but LiteSpeed has not shared additional details. To determine if a server is affected, users can run a "grep" command to search for indicators of compromise in the cPanel logs. If the command produces output, users should examine the IP addresses and block any that appear to be malicious. LiteSpeed has also released an updated version of the cPanel plugin, version 2.4.7, bundled with WHM plugin version 5.3.1.0, which patches the vulnerability and addresses additional potential attack vectors.

Users are advised to upgrade to the latest version of the LiteSpeed WHM Plugin, version 5.3.1.0, which includes cPanel plugin version 2.4.7 or higher, to patch the vulnerability. If immediate patching is not possible, removing the user-end plugin by running a specific command is recommended as a temporary workaround. The discovery of this vulnerability comes after a critical cPanel vulnerability, CVE-2026-41940, was identified as being actively exploited by unknown threat actors to deploy malware and ransomware.

The active exploitation of this vulnerability highlights the importance of keeping software up to date and patching known vulnerabilities in a timely manner. By upgrading to the latest version of the LiteSpeed WHM Plugin and cPanel plugin, users can protect their systems from potential attacks and prevent malicious actors from exploiting this vulnerability. It is essential for users to take immediate action to patch this vulnerability and ensure the security of their systems.

In summary, the LiteSpeed cPanel Plugin vulnerability CVE-2026-48172 is a critical issue that allows attackers to run arbitrary scripts as root, and it is being actively exploited. Users should take immediate action to patch the vulnerability by upgrading to the latest version of the LiteSpeed WHM Plugin and cPanel plugin, or remove the user-end plugin as a

---

> *True silence is the rest of the mind; it is to the spirit what sleep is to the body, nourishment and refreshment.
Author: William Penn*

Source: [LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root](https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html)
