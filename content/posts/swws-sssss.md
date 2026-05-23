---
title: "ZDI-26-294: (0Day) Microsoft Windows library-ms NTLM Response Information Disclosure Vulnerability"
date: 2026-04-21T05:00:00+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

A recently discovered vulnerability in Microsoft Windows, known as ZDI-26-294, allows network-adjacent attackers to disclose sensitive information on affected installations. This vulnerability requires user interaction to exploit, as the target must view a folder containing malicious content. The specific flaw exists within the parsing of library-ms files, which can be crafted to trigger an outgoing WebDAV request.

An attacker can leverage this vulnerability to disclose an NTLM response in the context of the current user, potentially leading to sensitive information disclosure. The vulnerability was first reported to the vendor on December 18, 2025, and the vendor acknowledged receipt of the report shortly after. However, on March 4, 2026, the vendor communicated that the vulnerability did not meet the bar for security servicing, indicating that a patch may not be forthcoming.

Given the nature of the vulnerability, the primary mitigation strategy is to restrict interaction with the product. This can help prevent attackers from exploiting the vulnerability and disclosing sensitive information. It is essential for users to exercise caution when viewing folders or files from untrusted sources, as this can help minimize the risk of exploitation.

The Zero Day Initiative (ZDI) has notified the vendor of their intention to publish the case as a 0-day advisory, as the vendor has chosen not to address the vulnerability. This decision highlights the importance of responsible disclosure and the need for vendors to prioritize security vulnerabilities. As a result, users must remain vigilant and take steps to protect themselves from potential exploitation, such as limiting their interaction with potentially malicious content.

---

> *If you want to study yourself � look into the hearts of other people. If you want to study other people � look into your own heart.
Author: Friedrich von Schiller*

Source: [ZDI-26-294: (0Day) Microsoft Windows library-ms NTLM Response Information Disclosure Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-294/)
