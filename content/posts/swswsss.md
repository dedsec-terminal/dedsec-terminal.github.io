---
title: "ZDI-26-312: Apple Safari Web Inspector WebCore Style Resolver Use-After-Free Remote Code Execution Vulnerability"
date: 2026-05-12T05:00:00+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A recently discovered vulnerability in Apple Safari, identified as ZDI-26-312, allows remote attackers to execute arbitrary code on affected installations. This vulnerability can be exploited when a user visits a malicious webpage or opens a malicious file, requiring user interaction to trigger the attack. The vulnerability is classified as a use-after-free remote code execution vulnerability, which can lead to significant security breaches.

The specific flaw exists within the WebCore style resolver in Web Inspector, a component of the Safari browser. The issue arises from the lack of validation of an object's existence before performing operations on it. This oversight allows an attacker to manipulate the object and execute code in the context of the browser process. As a result, an attacker can potentially gain control over the browser and execute malicious code, compromising the security of the system.

The vulnerability can be exploited by an attacker who crafts a malicious webpage or file that targets the WebCore style resolver in Web Inspector. When a user interacts with the malicious content, the attacker can leverage the vulnerability to execute code in the browser process. This can lead to a range of malicious activities, including data theft, malware installation, and unauthorized access to sensitive information. It is essential for users to exercise caution when interacting with unknown or untrusted web content to minimize the risk of exploitation.

To mitigate this vulnerability, users should ensure that their Apple Safari browser is updated with the latest security patches. Additionally, users should be cautious when visiting unknown websites or opening files from untrusted sources, as these may contain malicious content designed to exploit this vulnerability. By taking these precautions, users can reduce the risk of falling victim to this remote code execution vulnerability and protect their systems from potential security breaches.

---

> *Love all, trust a few, do wrong to none.
Author: William Shakespeare*

Source: [ZDI-26-312: Apple Safari Web Inspector WebCore Style Resolver Use-After-Free Remote Code Execution Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-26-312/)
