---
title: "PCPJack Hijacks 230 AWS, Google Cloud, and Azure Servers for Covert SMTP Relay Network"
date: 2026-06-05T05:34:19+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

The threat actor known as PCPJack has hijacked over 230 cloud servers from Amazon Web Services (AWS), Google Cloud, and Microsoft Azure to create a covert SMTP email relay network. The compromised servers, located across the US, Europe, and Asia, were converted into SMTP proxies and synced to a downstream consumer every five minutes. The infrastructure was still active when it was discovered by threat intelligence company Hunt.io.

Hunt.io found that the threat actor had left two open directories on a command-and-control (C2) server, revealing source code, compiled binaries, and other tools used in the operation. The directories contained a Sliver-integrated SMTP proxy deployment toolkit, Chisel tunneling and proxy binaries, and deployer scripts designed to automate the conversion of compromised Linux servers into SOCKS5 proxies. The scripts also included an SMTP quality gate that probed for outbound access to Gmail's SMTP server, ensuring that only hosts that could relay email were used in the pipeline.

The ultimate goal of the operation is unclear, but the infrastructure is capable of delivering spam or phishing emails at scale. The verified proxy list is synced every five minutes to a separate downstream server, which is currently inaccessible. Hunt.io describes the campaign as opportunistic, with the possibility of multiple actors sharing the same infrastructure. The discovery of the hijacked servers and the covert SMTP relay network highlights the need for cloud service providers and users to be vigilant about security and monitor their infrastructure for suspicious activity.

---

> *Successful people ask better questions, and as a result, they get better answers.
Author: Tony Robbins*

Source: [PCPJack Hijacks 230 AWS, Google Cloud, and Azure Servers for Covert SMTP Relay Network](https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html)
