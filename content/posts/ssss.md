---
title: "Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials"
date: 2026-05-19T05:28:06+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

In yet another software supply chain attack, threat actors have compromised the popular GitHub Actions workflow, actions-cool/issues-helper, to run malicious code that harvests sensitive credentials and exfiltrates them to an attacker-controlled server.
"Every existing tag in the repository has been moved to point to an imposter commit that does not appear in the action's normal commit history," StepSecurity researcher Varun Sharma said. "That commit contains malicious code that exfiltrates credentials from CI/CD pipelines that run the action."
An imposter commit refers to a deceptive software supply chain attack strategy in which malicious code is injected into a project by referencing a commit or tag that exists only in an adversary-controlled fork, rather than the original trusted repository. As a result, attackers can bypass standard Pull Request (PR) reviews and achieve arbitrary code execution.
The imposter commit, per the cybersecurity company, contains code that, upon being executed within a GitHub Actions runner, performs a series of actions -
- Downloads the Bun JavaScript runtime to the runner.
- Reads memory from the Runner.Worker process to extract credentials.
- Makes

---

> *Work while you have the light. You are responsible for the talent that has been entrusted to you.
Author: Henri-Frederic Amiel*

Source: [Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)
