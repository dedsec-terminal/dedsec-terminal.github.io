---
title: "Apple makes its quantum-resistant encryption open source"
date: 2026-05-27T11:04:25+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Apple has made its quantum-resistant encryption open source, allowing external researchers to review and evaluate the company's post-quantum cryptography implementations. The encryption is part of Apple's corecrypto library, which is used in all Apple operating systems and services, including iMessage, VPNs, and TLS networking. This move is significant as post-quantum cryptography is designed to protect encrypted data from future quantum computers that could potentially break widely used public-key encryption algorithms.

The corecrypto library provides encryption, hashing, random number generation, and digital signatures on over 2.5 billion active devices. Apple added post-quantum cryptography support to the library in 2024, using algorithms standardized by NIST, such as ML-KEM and ML-DSA. The company has applied various protections, including formal verification, to ensure the security and reliability of the library. Formal verification uses mathematical methods to prove that software behaves as intended under defined conditions, and Apple has developed a custom system to support multiple programming languages and codebases.

The verification process has identified issues that conventional testing may not have detected, and Apple has collaborated with a research company to develop tools to verify the implementations against official FIPS standards. The company believes that combining formal verification with conventional methods provides the strongest assurance possible. By making its quantum-resistant encryption open source, Apple is allowing independent experts to review and evaluate the work, which will help to ensure the security and reliability of the corecrypto library and the devices that rely on it.

---

> *Live through feeling and you will live through love. For feeling is the language of the soul, and feeling is truth.
Author: Matt Zotti*

Source: [Apple makes its quantum-resistant encryption open source](https://www.helpnetsecurity.com/2026/05/27/apple-quantum-resistant-encryption-open-source/)
