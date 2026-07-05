---
title: "Claude Helped a Hacker Find a Way to Issue Tickets to Almost Every US Music Festival"
date: 2026-07-01T10:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Security researcher Ian Carroll used the AI tool Claude Opus 4.7 to discover a vulnerability in the website of Front Gate Tickets, a company that handles ticketing for many major US music festivals. With Claude's help, Carroll was able to gain full access to the system, allowing him to issue free VIP backstage passes to any event, including sold-out shows. He could also access millions of customer and staff records, including names, emails, and mailing addresses.

Carroll reported his findings to Front Gate, which has since patched the vulnerability. The company stated that the issue was resolved within 24 hours and that there is no evidence of exploitation or compromise of customer information. However, Carroll notes that Front Gate does not claim to have evidence that the vulnerability was not previously exploited. The incident highlights the potential for AI tools to discover hackable bugs in websites and the importance of robust security measures to prevent such vulnerabilities.

The vulnerability was found to be a SQL injection flaw that could be exploited using a nested SQL query, which evaded the website's firewall detection. Carroll was surprised by the ease of the takeover method, which did not require two-factor authentication. The incident raises concerns about the security of websites, particularly those that handle sensitive information such as ticketing companies. Carroll's discovery also highlights the potential for AI tools to be used for both malicious and beneficial purposes, and the need for companies to prioritize security and audit their systems regularly to prevent such vulnerabilities.

---

> *Kind words do not cost much. Yet they accomplish much.
Author: Blaise Pascal*

Source: [Claude Helped a Hacker Find a Way to Issue Tickets to Almost Every US Music Festival](https://www.wired.com/story/claude-helped-a-hacker-find-a-way-to-issue-tickets-to-almost-every-us-music-festival/)
