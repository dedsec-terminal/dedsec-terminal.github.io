---
title: "Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read"
date: 2026-07-14T09:02:48+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the issue with xAI's Grok Build coding CLI:

xAI's Grok Build coding CLI was found to be uploading entire Git repositories, including full commit history, to a Google Cloud Storage bucket, rather than just the files needed for a coding task. A researcher, cereblab, discovered this by capturing an upload and cloning the Git bundle, which revealed that even files the agent was told not to open were being uploaded. The upload was found to be separate from the model itself, with a significant gap between the data needed by the model and the data being uploaded.

The issue was found to be a default behavior of the Grok Build CLI, with the "Improve the model" setting having no effect on the upload of the repository. The researcher also found that credential files, including API keys and passwords, were being uploaded without redaction. xAI has since addressed the issue by disabling the upload of codebases, but the company has not provided details on why the behavior was implemented, how long it was in place, or how many users were affected.

As a result of the issue, users who have used the Grok Build CLI are advised to rotate any credentials that may have been uploaded, including those in tracked files and Git history. xAI has stated that all user data uploaded before the issue was addressed will be deleted, but users should still take steps to protect their sensitive information. The incident highlights the importance of checking what data is being uploaded by cloud coding tools and ensuring that sensitive information is protected. xAI's response to the issue has been limited, and the company has not provided a clear explanation of the behavior or its implications.

---

> *Life is a succession of moments. To live each one is to succeed.
Author: Corita Kent*

Source: [Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html)
