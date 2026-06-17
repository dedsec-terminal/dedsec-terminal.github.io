---
title: "Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting"
date: 2026-06-16T19:05:41+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A vulnerability was discovered in the Google Cloud Vertex AI SDK for Python, allowing an attacker to hijack a victim's machine learning model upload and run code inside Google's serving infrastructure. The attack, dubbed "Pickle in the Middle," required only a Google Cloud project and the victim's project ID, which is often publicly available. The attacker could create a temporary Cloud Storage bucket with a predictable name, allowing them to intercept and replace the victim's model files with malicious ones.

The vulnerability was caused by the SDK's failure to verify the ownership of the temporary Cloud Storage bucket used for model uploads. If the bucket did not exist, the SDK would generate a predictable name based on the project ID and region, allowing an attacker to create the bucket first and intercept the model files. The attacker could then replace the uploaded model with a malicious one, which could run code when loaded by Vertex AI. The attack relied on speed, with the attacker needing to replace the model within a short time frame (approximately 2.5 seconds) before Vertex AI read the file.

Google has patched the vulnerability in version 1.148.0 of the Vertex AI SDK, adding a random UUID to the bucket name and verifying bucket ownership to prevent bucket squatting. Users are advised to update to the latest version and set an explicit staging bucket to a Cloud Storage location they control when uploading models. This is the second predictable-bucket-name flaw to be discovered in Vertex AI this year, highlighting the importance of secure coding practices and regular security updates.

---

> *In separateness lies the world's great misery, in compassion lies the world's true strength.
Author: Buddha*

Source: [Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting](https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html)
