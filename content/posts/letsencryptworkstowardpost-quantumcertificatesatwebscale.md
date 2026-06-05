---
title: "Let’s Encrypt works toward post-quantum certificates at web scale"
date: 2026-06-05T10:45:17+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Let's Encrypt is working towards implementing post-quantum certificates at web scale through Merkle Tree Certificates (MTCs), a new approach that adds post-quantum authentication to the web without sacrificing speed and reliability. The project aims to have a staging environment ready by late 2026 and a production-ready environment by 2027. This move is in response to the potential threat of quantum computers breaking current encryption methods, which could compromise the security of online transactions.

The transition to post-quantum security requires significant changes to Let's Encrypt's infrastructure, including certificate issuance, revocation systems, and operational tooling. The organization is participating in the IETF PLANTS and ACME working groups to develop standards for MTCs. The adoption of post-quantum certificates will also depend on support from browsers, libraries, and ACME clients. Let's Encrypt is tracking standards work around ML-DSA signatures in X.509 and TLS, as well as ecosystem changes such as ML-DSA support in the Go standard library.

The implementation of MTCs is crucial as it allows for post-quantum authentication without increasing the size of TLS handshakes, which would lead to increased bandwidth usage and connection overhead. MTCs work by issuing certificates in batches, with a single signature covering an entire batch, and using landmarks to keep authentication paths up to date outside the TLS handshake. Let's Encrypt will provide updates on the development and deployment of MTCs, and encourages ACME client developers and operators to follow the work in the IETF PLANTS working group to ensure a smooth transition to post-quantum security.

---

> *To be upset over what you don't have is to waste what you do have.
Author: Ken S. Keyes*

Source: [Let’s Encrypt works toward post-quantum certificates at web scale](https://www.helpnetsecurity.com/2026/06/05/lets-encrypt-mcts-web-post-quantum-authentication/)
