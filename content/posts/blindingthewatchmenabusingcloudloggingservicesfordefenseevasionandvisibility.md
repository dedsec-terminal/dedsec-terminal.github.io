---
title: "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility"
date: 2026-06-09T22:00:21+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

**Introduction to Cloud Logging Services and Attack Techniques**
Cloud logging services, such as Amazon Web Services (AWS) CloudTrail and Google Cloud Logging, provide comprehensive visibility into actions performed within cloud resources, making them essential for security monitoring. However, this reliance also makes logging services a high-value target for attackers. Attackers can exploit these services to create weak spots, evade detection, and establish continuous visibility within a target's environment. The primary attack techniques against cloud logging services fall into two categories: Defense Evasion and Continuous Visibility.

**Defense Evasion Techniques**
Defense Evasion techniques enable attackers to remain undetected within a compromised cloud environment. These methods involve manipulating or evading logging mechanisms, which are crucial for security monitoring and incident response. Attackers can use various techniques to accomplish this, including stopping logging, deleting log storage destinations, deleting log routers, impairing logging via attacker-controlled encryption keys, and log poisoning. For example, an attacker with the necessary permissions can disable logging in AWS by invoking the stop-logging API call or in Google Cloud by disabling the sink. Additionally, an attacker can delete the log storage destination, such as an S3 bucket in AWS or a log bucket in Google Cloud, to prevent logs from being written.

**Protection and Mitigation**
To protect against these attack techniques, organizations can implement the appropriate configurations and detect service misuse. Palo Alto Networks customers can utilize products and services such as the Unit 42 Cloud Security Assessment and the Unit 42 Incident Response team to identify misconfigurations and security gaps. Additionally, cloud providers offer features such as log bucket locking in Google Cloud, which can prevent deletion of log buckets. By understanding these attack scenarios and implementing the necessary protections, organizations can better defend their cloud environments against attackers seeking to exploit cloud logging services for defense evasion and continuous visibility.

---

> *The greatest antidote to insecurity and the sense of fear is compassion � it brings one back to the basis of one's inner strength
Author: Dalai Lama*

Source: [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)
