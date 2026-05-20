---
title: "CISA Admin Leaked AWS GovCloud Keys on Github"
date: 2026-05-20
draft: false
categories:
  - threat-intelligence
author: "DedSec-Terminal"
---

Until this past weekend, a contractor for the Cybersecurity & Infrastructure Security Agency (CISA) maintained a public GitHub repository that exposed credentials to several highly privileged AWS GovCloud accounts and a large number of internal CISA systems. Security experts said the public archive included files detailing how CISA builds, tests and deploys software internally, and that it represents one of the most egregious government data leaks in recent history.

On May 15, KrebsOnSecurity heard from Guillaume Valadon, a researcher with the security firm GitGuardian. Valadon’s company constantly scans public code repositories at GitHub and elsewhere for exposed secrets, automatically alerting the offending accounts of any apparent sensitive data exposures. Valadon said he reached out because the owner in this case wasn’t responding and the information exposed was highly sensitive.

The GitHub repository that Valadon flagged was named “Private-CISA,” and it harbored a vast number of internal CISA/DHS credentials and files, including cloud keys, tokens, plaintext passwords, logs and other sensitive CISA assets.

Valadon said the exposed CISA credentials represent a textbook example of poor security hygiene, noting that the commit logs in the offending GitHub account show that the CISA administrator disabled the default setting in GitHub that blocks users from publishing SSH keys or other secrets in public code repositories.

“Passwords stored in plain text in a csv, backups in git, explicit commands to disable GitHub secrets detection feature,” Valadon wrote in an email. “I honestly believed that it was all fake before analyzing the content deeper. This is indeed the worst leak that I’ve witnessed in my career. It is obviously an individual’s mistake, but I believe that it might reveal internal practices.”

One of the exposed files, titled “importantAWStokens,” included the administrative credentials to three Amazon AWS GovCloud servers. Another file exposed in their public GitHub repository — “AWS-Workspace-Firefox-Passwords.csv” — listed plaintext usernames and passwords for dozens of internal CISA systems. According to Caturegli, those systems included one called “LZ-DSO,” which appears short for “Landing Zone DevSecOps,” the agency’s secure code development environment.

*When the winds of change blow, some build walls, others build windmills. — Chinese proverb*

Source: [Krebs on Security](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) · [Read Original →](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)
