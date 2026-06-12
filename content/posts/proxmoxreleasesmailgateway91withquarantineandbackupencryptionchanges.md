---
title: "Proxmox releases Mail Gateway 9.1 with quarantine and backup encryption changes"
date: 2026-06-11T14:51:41+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Proxmox has released Mail Gateway 9.1, an open-source email security solution that acts as a mail proxy to screen incoming and outgoing traffic for spam, viruses, and phishing attempts. The new version runs on Debian 13.5 Trixie and includes updated system components such as Linux kernel 7.0, SpamAssassin 4.0.2, and ClamAV 1.4.4. These updates ensure that the platform stays current with the latest major open-source security packages.

The latest release also introduces changes to the spam quarantine interface, making it easier for administrators and end-users to review filtered messages. New features include the ability to mark quarantined emails as "seen", a quarantine overview that shows both positive and negative parts of an email's spam score, and the option to load external images only on demand. Additionally, administrators can now copy a recipient's private quarantine access link, making it easier to share access to quarantined messages.

Proxmox Mail Gateway 9.1 also adds native encryption for backups sent to a Proxmox Backup Server instance, covering email configuration settings, user-created rule system data, and historic and private statistics data. The encryption is client-side, meaning that the data is encrypted before it leaves the system and remains encrypted on the backup storage target. The new version is available for download now and can be installed on bare-metal hardware, an existing Debian system, or run as a Linux Container on Proxmox VE, with a tested upgrade path available for existing deployments on version 8.2 or 9.0.

---

> *You cannot have what you do not want.
Author: John Acosta*

Source: [Proxmox releases Mail Gateway 9.1 with quarantine and backup encryption changes](https://www.helpnetsecurity.com/2026/06/11/proxmox-mail-gateway-9-1-released/)
