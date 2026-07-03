---
title: "How We Added WebAuthn to a Browser-Based RDP Client"
date: 2026-07-02T22:00:39+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a 3-paragraph summary of the article:

The Prisma Browser team developed a browser-based RDP client that supports WebAuthn redirection, a feature that allows users to authenticate with security keys, such as YubiKeys, within a remote desktop session. This was a challenging task, as no browser API could handle the required functionality, and the protocol specification was incomplete. The team had to reverse-engineer Microsoft's Windows implementation, which involved using internal, undocumented code paths.

The team's initial approach was to use the `navigator.credentials` API, but this didn't work because the API constructs its own `clientDataJSON` object, which doesn't match the one expected by the server. To solve this, they built a custom browser API that accepts a pre-computed `clientDataHash` and passes it directly to the authenticator. This API is a thin wrapper around Chromium's FIDO2 stack, which provides authenticator discovery, credential selector UI, and other features. The team also had to work around limitations of the WebHID API and libfido2, which are not suitable for in-browser use.

The team encountered further challenges when testing their implementation against different Windows servers. They found that newer Windows servers send additional data, including `clientDataJSON`, while older servers only send a 32-byte hash. To make their implementation work with older servers, they had to reverse-engineer Microsoft's `mstsc.exe` client, which uses a private, unexported API to handle WebAuthn requests. The team used IDA Pro and Frida to analyze the client's behavior and discovered that it uses a dual-personality approach, with a public API for browsers and apps, and a private API for the RDP client. By understanding this implementation, the team was able to make their own client work with older Windows servers, providing a seamless WebAuthn experience for users.

---

> *If your actions inspire others to dream more, learn more, do more and become more, you are a leader.
Author: John Quincy Adams*

Source: [How We Added WebAuthn to a Browser-Based RDP Client](https://unit42.paloaltonetworks.com/webauthn-added-to-browser-based-rdp/)
