---
title: "Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws"
date: 2026-07-10T14:19:50+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Security researcher Chinmohan Nayak has discovered three high-severity vulnerabilities in the OpenClaw personal artificial intelligence (AI) assistant. The flaws, identified as GHSA-hjr6-g723-hmfm, GHSA-9969-8g9h-rxwm, and GHSA-575v-8hfq-m3mc, could allow attackers to steal credentials, escalate privileges, and execute arbitrary code on the host. These vulnerabilities can be exploited through an external message sent via WhatsApp, without requiring a prior foothold in the system.

The vulnerabilities affect the host execution environment filtering mechanism and can be used to bypass authorization and policy checks. Specifically, GHSA-575v-8hfq-m3mc is a path traversal and link following vulnerability that can allow sandbox bind mounts to bypass parent-directory denylist checks. This can enable an attacker to read sensitive data, such as SSH keys, AWS credentials, and GPG secrets, and even escape the sandbox to gain full host access. The other two vulnerabilities are operating system command injection flaws that can allow an attacker to execute or persist actions beyond the caller's intended authorization.

The vulnerabilities have been patched in OpenClaw version 2026.6.6, and users are advised to update to the latest version. Additionally, OpenClaw recommends enabling sandbox mode for all non-main sessions, removing "exec" from the tool allowlist for channel-facing agents, and monitoring for suspicious activity. Users can also harden their systems by keeping channel and tool allowlists narrow, avoiding sharing gateways between untrusted users, and disabling the affected feature when not needed. By taking these steps, users can protect themselves from potential attacks that exploit these vulnerabilities.

---

> *There is only one way to happiness and that is to cease worrying about things which are beyond the power of our will.
Author: Epictetus*

Source: [Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws](https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html)
