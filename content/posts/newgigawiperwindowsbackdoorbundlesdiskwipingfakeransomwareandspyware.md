---
title: "New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware"
date: 2026-07-09T18:08:07+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the article:

Microsoft has analyzed a new Windows backdoor called GigaWiper, which is a combination of three older destructive programs: a disk wiper, fake ransomware, and spyware. The malware is written in Go and runs on Windows, taking orders as numbered commands. It can wipe the entire disk, overwrite the Windows drive, or run fake ransomware that scrambles files without saving the key, making it impossible to recover the data.

GigaWiper also has spyware capabilities, allowing it to take screenshots, record the screen, and open a hidden VNC session to control the infected PC. It can collect system details, manage running programs and services, edit the registry, and wipe Windows event logs to cover its tracks. The malware pretends to be OneDrive and creates a scheduled task to run every minute, hiding its command traffic behind legitimate business services like RabbitMQ, Redis, and MinIO.

The origin of GigaWiper is attributed to a likely Iran-nexus group, with ties to the Crucio ransomware and FlockWiper malware. Microsoft recommends turning on tamper protection, blocking known command servers, and running endpoint detection in block mode to prevent GigaWiper infections. Defenders can spot the malware by looking for specific signals, such as a OneDrive Update scheduled task, unusual RabbitMQ or Redis traffic, and processes taking ownership of Windows boot files outside maintenance windows. Early detection and clean, offline backups are crucial to defending against GigaWiper, as there is no patch to fix the malware.

---

> *Self-complacency is fatal to progress.
Author: Margaret Sangster*

Source: [New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware](https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html)
