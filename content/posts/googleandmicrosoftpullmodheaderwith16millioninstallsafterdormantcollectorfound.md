---
title: "Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found"
date: 2026-07-13T17:17:24+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

Google and Microsoft have removed the ModHeader extension from their stores after researchers discovered a hidden browsing-history collector within the extension. The collector was dormant, with an empty allow-list that kept it switched off, and there is no evidence that it ever gathered or sent any browsing data. The extension, which had around 1.6 million installs across Chrome and Edge, was found to have a second system that could collect and encrypt browsing domains, but it was not active due to the empty allow-list.

The analysis, conducted by UK security firm Stripe OLT, revealed that the collector was built into the official store version of the extension, not a counterfeit. The extension's code was found to contain a device fingerprint and a hardcoded encryption key, which could be used to collect and upload browsing data to a server. However, the collector was not active, and the allow-list was empty, preventing it from collecting any data. The researchers also found that the extension had been injecting ads into search results in 2023 and had reportedly gone ad-supported around the same time.

The removal of ModHeader from the stores highlights the importance of reviewing extensions for dormant code paths and new call-home endpoints. The incident also raises concerns about the potential for popular extensions to be bought and turned into data pipes, as described by Brian Krebs in 2021. Users who had installed ModHeader are advised to remove it and rotate any secrets, such as API keys or session cookies, that they may have pasted into the extension. Defenders are also advised to block and log the domains associated with the collector to prevent any potential data collection.

---

> *Before you can inspire with emotion, you must be swamped with it yourself. Before you can move their tears, your own must flow. To convince them, you must yourself believe.
Author: Winston Churchill*

Source: [Google and Microsoft Pull ModHeader With 1.6 Million Installs After Dormant Collector Found](https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html)
