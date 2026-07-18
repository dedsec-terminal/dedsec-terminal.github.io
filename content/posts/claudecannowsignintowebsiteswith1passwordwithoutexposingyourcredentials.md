---
title: "Claude can now sign into websites with 1Password without exposing your credentials"
date: 2026-07-17T09:17:44+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

1Password has introduced a beta integration with Anthropic's AI assistant, Claude, allowing users to sign into websites without exposing their credentials. This integration, available to paid Claude subscribers and 1Password customers, enables Claude to complete browser tasks requiring authentication without accessing users' passwords or other secrets. To use this feature, users must connect their 1Password account to Claude from the Connectors section in Claude Desktop and have the 1Password desktop app and browser extension installed.

When Claude needs to sign in to a website, it requests the required login from 1Password, and the extension shows which credential is being requested and why, allowing users to approve or deny access. The credentials are filled into the page through a secure channel managed by 1Password, and secret values never enter Claude's context window, memory, or Anthropic's infrastructure. Access is limited to the current task, and when the task ends, Claude must request permission again before using the same credential. This integration is designed to provide a new security model for agents, where users can give agents permission to use a credential without letting the agent see it.

The integration includes a feature called Agentic Mode, which prevents agents from interacting with the 1Password extension and automatically activates when Claude takes control of the browser. This mode locks down the extension, hides its interface from Claude, and limits access to the credentials approved for the current task. Users can revoke access or stop an active task at any time, and every request for credentials requires explicit user approval. Currently, the integration supports logins and one-time passwords (TOTP), but does not support payment cards, identities, or other item types.

---

> *You can do what's reasonable or you can decide what's possible.*

Source: [Claude can now sign into websites with 1Password without exposing your credentials](https://www.helpnetsecurity.com/2026/07/17/1password-anthropic-claude-integration/)
