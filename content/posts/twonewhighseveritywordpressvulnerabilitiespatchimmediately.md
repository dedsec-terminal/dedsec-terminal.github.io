---
title: "Two new high severity WordPress vulnerabilities, patch immediately!"
date: 2026-07-18T14:57:20+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Two new high-severity WordPress vulnerabilities have been discovered, prompting an urgent call to patch immediately. The vulnerabilities, identified as CVE-2026-60137 and CVE-2026-63030, were reported to the WordPress security team and have been addressed in the 7.0.2 WordPress security release. The first vulnerability is a facilitated SQL injection issue, while the second is a REST API batch-route confusion and SQL injection issue that can lead to Remote Code Execution.

The vulnerabilities affect various versions of WordPress, including 6.9, which is affected by both issues, and 6.8, which is only affected by the first vulnerability. The beta release of WordPress 7.1 is also affected by both vulnerabilities. Versions prior to 6.8 are not affected. To address the issue, WordPress has released updated versions, including 6.9.5 and 6.8.6, which contain fixes for the vulnerabilities.

If updating is not immediately possible, temporary mitigation measures can be taken to protect against the vulnerabilities. This can be done by blocking anonymous access to the batch API, either by installing a plugin that blocks anonymous access to the REST API or by blocking specific URLs at a WAF level. However, these measures may impact legitimate use of the site and should only be considered emergency temporary solutions until an update can be applied. It is recommended to update to the latest version of WordPress as soon as possible to ensure security.

---

> *Your work is to discover your world and then with all your heart give yourself to it.
Author: Buddha*

Source: [Two new high severity WordPress vulnerabilities, patch immediately!](https://www.helpnetsecurity.com/2026/07/18/wordpress-vulnerabilities-wp2shell-cve-2026-60137-cve-2026-60137/)
