---
title: "npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain Attacks"
date: 2026-05-23T16:35:10+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

GitHub has introduced new security features for npm to enhance the protection of the software supply chain. The first feature, called staged publishing, requires a human maintainer to approve a package release using two-factor authentication (2FA) before it becomes publicly available for installation. This ensures that every publish, including those from non-interactive CI/CD workflows and trusted publishing with OpenID Connect (OIDC) authentication, has a "proof of presence". To use staged publishing, package maintainers must have publish access, 2FA enabled, and the package must already exist on the npm registry.

Package maintainers can submit their packages to a staging area using the "npm stage publish" command, which is available in npm CLI 11.15.0 or newer. GitHub recommends pairing staged publishing with trusted publishing using OIDC for optimal protection. This update aims to prevent supply chain attacks by adding an extra layer of security and control over package publishing. By requiring explicit approval from a human maintainer, staged publishing reduces the risk of malicious packages being published and installed by unsuspecting users.

In addition to staged publishing, GitHub has introduced three new install source flags for npm. These flags - --allow-file, --allow-remote, and --allow-directory - allow developers to control installs from local file paths, remote URLs, and local directories, respectively. These flags enable developers to apply an explicit allowlist approach to every non-registry install source, providing more fine-grained control over package installation. This update is particularly important given the recent surge in software supply chain attacks targeting open-source ecosystems, where attackers have been compromising popular packages at an unprecedented scale.

The introduction of these new features is a response to the growing threat of supply chain attacks, which have been on the rise in recent months. By providing more control and security over package publishing and installation, GitHub aims to protect the npm ecosystem and prevent malicious actors from compromising packages. The new features are designed to be easy to use and integrate into existing workflows, making it simpler for developers to prioritize security and protect their users from potential threats.

---

> *Go put your creed into the deed. Nor speak with double tongue.
Author: Ralph Emerson*

Source: [npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain Attacks](https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html)
