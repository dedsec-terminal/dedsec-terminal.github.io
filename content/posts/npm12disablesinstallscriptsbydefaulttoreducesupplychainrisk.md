---
title: "npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk"
date: 2026-07-09T16:49:02+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

npm version 12 has been released with significant changes to reduce supply chain risk. By default, install scripts are now disabled, and users must explicitly allow them to run. This change affects dependency lifecycle scripts, such as preinstall, install, and postinstall, as well as implicit node-gyp builds. Additionally, Git dependencies and remote URLs are no longer resolved unless explicitly allowed.

To review and approve trusted scripts, users must run a command to generate an allowlist, which is then committed to the "package.json" file. These changes were previewed last month, and GitHub recommends developers upgrade to npm 11.16.0 or newer to review warnings and prepare for the update. The latest release also deprecates granular access tokens (GATs) that bypass two-factor authentication (2FA), limiting their ability to perform sensitive account and package management actions.

The changes to GATs will be implemented in two phases, with the first change taking effect in early August 2026 and the second in January 2027. GitHub advises developers to stop using 2FA-bypass tokens and instead perform operations interactively with 2FA. To prepare for the changes, developers should plan to move automated publishing to trusted publishing or staged publishing with human approval. Meanwhile, pnpm 11.10 has introduced a new "_auth" setting for configuring registry authentication, which enhances security by preventing malicious project files from redirecting registry tokens.

---

> *Ability will never catch up with the demand for it.
Author: Confucius*

Source: [npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk](https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html)
