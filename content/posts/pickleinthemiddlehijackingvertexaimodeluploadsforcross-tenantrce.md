---
title: "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE"
date: 2026-06-16T10:00:29+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Vulnerability Overview**
A vulnerability was discovered in the Google Cloud Vertex AI software development kit (SDK) for Python, which allowed an attacker to hijack a victim's model upload and achieve remote code execution (RCE) within the target's Vertex AI serving infrastructure. The vulnerability, known as "Pickle in the Middle," relied on a predictable default bucket name and a missing ownership check in the SDK's staging logic.

**Exploitation Method**
The attacker could exploit this vulnerability by preemptively creating a bucket with the predicted name in their own project, a technique known as bucket squatting. The SDK would then silently upload the victim's model artifacts to the attacker-controlled bucket. The attacker could replace the legitimate model with a malicious one, which would execute arbitrary code when deployed and loaded, using the pickle deserialization mechanism. This vulnerability affected google-cloud-aiplatform SDK versions 1.139.0 and 1.140.0, which were the latest versions at the time of testing.

**Mitigation and Fix**
Google has fixed the issue in version 1.148.0 of the SDK, released on April 15, 2026. Developers are recommended to upgrade to the fixed version to prevent exploitation. The Unit 42 AI Security Assessment and Unit 42 Frontier AI Defense service can help identify and mitigate complex AI-specific risks. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team. The vulnerability highlights the importance of secure coding practices and regular security testing to prevent similar vulnerabilities in the future.

---

> *Fear is a darkroom where negatives develop.
Author: Usman Asif*

Source: [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)
