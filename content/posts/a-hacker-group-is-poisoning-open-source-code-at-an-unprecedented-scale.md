---
title: "A Hacker Group Is Poisoning Open Source Code at an Unprecedented Scale"
date: 2026-05-21T09:00:00+00:00
draft: false
categories:
  - cves
---

A hacker group known as TeamPCP has been carrying out a massive series of software supply chain attacks, corrupting hundreds of open-source tools and extorting victims for profit. The group has breached numerous companies, including GitHub, Anthropic, and Mercor, and has accessed thousands of code repositories. TeamPCP's tactics involve gaining access to a network where an open-source tool is being developed, planting malware in the tool, and then using stolen credentials to publish malicious versions of other software development tools.

The group has automated many of its attacks using a self-spreading worm called Mini Shai-Hulud, which creates encrypted credentials stolen from victims and leaves a message referencing the sci-fi novel Dune. TeamPCP appears to be financially motivated and often deploys ransomware or data extortion campaigns against its targets.

The scale of TeamPCP's attacks has expanded dramatically in recent months, with the group hacking more software utilities and leading to a cascading effect of supply chain attacks. The fallout has been severe, with breaches of the European Commission's public website, source code of Anthropic's Claude, and many other organizations.

To protect themselves, organizations can practice security "hygiene" by carefully managing authentication tokens, imposing access restrictions, and rotating credentials regularly. Experts also recommend safeguards such as "age-gating" updates to open-source tools, vetting and installing security updates, and holding off on immediate updates to code that's been newly published and may be malicious.

The attacks raise hard questions about how to safely use open-source software in an era of mounting supply chain attacks. Experts recommend taking trust-but-verify measures, such as analyzing updates for malware before rolling them out across a network, and implementing a "cool-down" period before downloading and running code.

Key takeaways:

* TeamPCP has carried out a massive series of software supply chain attacks, corrupting hundreds of open-source tools and extorting victims for profit.
* The group's tactics involve gaining access to a network where an open-source tool is being developed, planting malware in the tool, and then using stolen credentials to publish malicious versions of other software development tools.
* TeamPCP appears to be financially motivated and often deploys ransomware or data extortion campaigns against its targets.
* Organizations can protect themselves by practicing security "hygiene", rotating credentials regularly, and implementing safeguards such as "age-gating" updates to open-source tools.
* The attacks raise hard questions about how to safely use open-source software in an era of mounting supply chain

---

> *Though no one can go back and make a brand new start, anyone can start from now and make a brand new ending.*

Source: [A Hacker Group Is Poisoning Open Source Code at an Unprecedented Scale](https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/)
