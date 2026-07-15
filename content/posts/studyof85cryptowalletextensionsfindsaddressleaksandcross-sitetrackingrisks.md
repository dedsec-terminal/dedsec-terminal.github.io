---
title: "Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks"
date: 2026-07-14T11:55:00+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers at KU Leuven tested 85 popular crypto wallet browser extensions and found significant privacy risks. The wallets, used by approximately 35 million people, can leak user addresses, allowing outsiders to track and link separate addresses together. This is not a result of a hack, but rather how the wallets were designed to interact with websites and blockchain servers. The researchers identified five privacy weaknesses, including the ability of servers to learn connections between a user's separate addresses and the failure of logging out to actually revoke access.

The study found that 17 wallets exposed connections between a user's separate addresses, and 36 wallets allowed websites to track users even after they had logged out. Additionally, 23 wallets were found to hand out user addresses to tracking scripts, potentially allowing attackers to link a pseudonymous crypto profile to a real identity. The researchers demonstrated that this could be done by loading a crypto app inside an invisible frame on an unrelated website, allowing the tracker to access the user's address without their knowledge or consent.

The researchers reported their findings to the affected wallet makers, but many declined to treat the issues as bugs. Some, such as Coinbase Wallet and Coin98, have since fixed the problems, but others, like MetaMask, have stated that they have no immediate plans to address the issues. The researchers argue that the real fix is not to warn users, but to change the design of the wallets and establish an ecosystem standard for logging out and protecting user privacy. The study highlights the need for greater attention to privacy and security in the development of crypto wallets and the importance of addressing these issues to protect users' identities and financial information.

---

> *Silence is the true friend that never betrays.
Author: Confucius*

Source: [Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks](https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html)
