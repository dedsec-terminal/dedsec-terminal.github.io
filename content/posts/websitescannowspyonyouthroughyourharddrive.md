---
title: "Websites Can Now Spy on You Through Your Hard Drive"
date: 2026-06-01T09:30:00+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Websites can now use a new technique called FROST (fingerprinting remotely using OPFS-based SSD timing) to spy on their visitors by measuring subtle interactions with their solid-state drives. This technique allows sites to monitor other sites a visitor is viewing and what apps are open on their devices. FROST exploits a side channel, a form of leak resulting from physical manifestations such as electromagnetic emanations, data caches, or the time required to complete a task, to decrypt encrypted traffic and infer other confidential data.

The FROST technique uses JavaScript to interact with the OPFS (origin private file system), an allocated storage space reserved for a specific site to run code needed to complete a given task. By measuring the I/O interactions and running them through a pretrained convolutional neural network, the attacker can deduce various apps and websites open on the device. The technique has limitations, such as requiring a large OPFS file and storing it on the same SSD the visitor is using. However, it can be used to track open websites and apps, and can be performed without any interaction from the visitor other than opening the site hosting the attack.

To prevent FROST attacks, users can close tabs as soon as they're no longer needed, and monitor the creation and size of OPFS files allocated by unknown websites. Browser makers can also limit the maximum size of OPFS files to shut down the side channel. The researchers have proposed ways to prevent FROST attacks, but there are no indications that these attacks have been performed in the wild. The research is scheduled to be presented at the DIMVA conference in July, and provides many more technical details on the FROST technique and its limitations.

---

> *Nothing diminishes anxiety faster than action.
Author: Walter Anderson*

Source: [Websites Can Now Spy on You Through Your Hard Drive](https://www.wired.com/story/websites-can-now-spy-on-you-through-your-hard-drive/)
