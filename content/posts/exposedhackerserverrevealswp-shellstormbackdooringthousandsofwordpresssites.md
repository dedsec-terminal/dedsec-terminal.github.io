---
title: "Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites"
date: 2026-07-10T11:30:02+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

A cybercrime crew, tracked as WP-SHELLSTORM, left one of its servers exposed on the internet for three weeks, revealing the operation's inner workings. The server contained hacking tools, activity logs, and target lists naming over 1.4 million websites, mostly WordPress and Joomla sites. The crew used automated scanners to exploit publicly known bugs in website plugins, uploading webshells to compromised sites, which allowed them to run commands, read files, and steal passwords.

The exposed files showed that the crew targeted sites running out-of-date plugins, with the Breeze caching plugin and Joomla's JCE editor being the most exploited. The crew's toolkit covered 27 known flaws, but a handful of bugs did most of the work. The biggest producer was a bug in the Breeze caching plugin, which was used to backdoor over 17,000 sites. However, the actual number of compromised sites was far smaller, with researchers estimating around 5,700 live webshells. The crew's tools and techniques were not advanced, but their scale and automation allowed them to compromise sites at scale.

The exposure of the server has provided valuable insights into the crew's operations, including their use of a SNOWLIGHT dropper to install VShell, a stealthy backdoor. The crew's sloppy tradecraft, including leaving the server open and using fluent Simplified Chinese in their code, suggests that they are Chinese or Chinese-speaking. The researchers assess with medium-to-high confidence that the operator is financially motivated rather than state-directed. Website owners are advised to patch vulnerable plugins, including Breeze and JCE, and to check for signs of compromise, such as the crew's webshell filename patterns and suspicious process names.

---

> *Every problem has a gift for you in its hands.
Author: Richard Bach*

Source: [Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites](https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html)
