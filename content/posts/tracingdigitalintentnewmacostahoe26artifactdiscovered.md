---
title: "Tracing Digital Intent: New MacOS Tahoe 26 Artifact Discovered"
date: 2026-06-12T22:00:14+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

**Introduction to App.MenuItem Artifact**
A new artifact has been discovered in macOS Tahoe 26, providing forensic examiners with a detailed record of user actions. The App.MenuItem artifact is a Biome stream that logs specific menu selections made by users across the operating system. This artifact offers a step-by-step record of user actions, from compressing files to emptying the trash, providing critical context for user activity.

**Location and Analysis of App.MenuItem**
The App.MenuItem artifact is located at ~/Library/Biome/streams/restricted/App.MenuItem/local and contains SEGB-encapsulated protobuf entries. To parse this artifact, examiners can use open-source tools like ccl-segb, as standard forensic tools may not yet support it. By exporting the file, running the ccl-segb Python script, and converting the output to CSV format, examiners can analyze the data and reconstruct a user's workflow. This artifact provides a narrative view of user behavior, showing deliberate actions such as selecting "Move to Trash" followed by "Empty Trash".

**Value and Limitations of App.MenuItem**
The App.MenuItem artifact is valuable for reconstructing digital intent, as it captures the exact text of menu items selected by the user, along with the timestamp of the activity. However, it has limitations, relying on the menu item text itself, which may not always contain the file or folder name. When correlated with file system logs, App.MenuItem provides the "human" context that technical logs often miss. The discovery of this artifact adds a powerful new layer to forensic investigations, allowing examiners to understand user behavior and reconstruct sequences of events with greater precision.

---

> *Transformation does not start with some one else changing you; transformation is an inner self reworking of what you are now to what you will be.
Author: Byron Pulsifer*

Source: [Tracing Digital Intent: New MacOS Tahoe 26 Artifact Discovered](https://unit42.paloaltonetworks.com/new-macos-artifact-discovered/)
