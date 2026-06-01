---
title: "OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack"
date: 2026-06-01T09:31:15+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Supply Chain Attack on OpenAI Codex**: A malicious supply chain campaign has been targeting developers using OpenAI Codex through a legitimate-looking remote web UI called codexui-android. The npm package, which has over 29,000 weekly downloads, contains embedded malicious code that exfiltrates Codex authentication tokens to an attacker-controlled server. The package's GitHub repository remains clean, and the malicious code was introduced about a month after the package was published.

**Exfiltration of Sensitive Data**: The malicious code extracts the contents of Codex's "~/.codex/auth.json" file, which includes access_token, refresh_token, id_token, and account ID. The refresh_token, in particular, is concerning as it does not expire, allowing an attacker to silently impersonate the user indefinitely. The captured data is sent to a remote server masquerading as Sentry, a legitimate application monitoring and error tracking platform. The threat actor has also been using an Android application to target Codex developers, with over 50,000 downloads.

**Broader Implications and Response**: The attack highlights the increasing trend of threat actors targeting AI developer tooling and workflows to steal credentials and burrow deeper into the software supply chain. The incident also underscores the importance of secure credential management and prompt revocation of compromised credentials. The package author has claimed to be investigating the issue and removing the affected functionality, but their response has raised more questions than answers. The incident serves as a reminder for developers to treat authentication tokens with caution and to be vigilant about potential supply chain attacks.

---

> *You can do what's reasonable or you can decide what's possible.*

Source: [OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack](https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html)
