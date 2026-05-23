---
title: "OceanLotus suspected of using PyPI to deliver ZiChatBot malware"
date: 2026-05-06T13:00:34+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Researchers have discovered a series of malicious wheel packages on the Python Package Index (PyPI) that are believed to be linked to the OceanLotus group. These packages, which were uploaded in July 2025, appear to be legitimate libraries but actually deliver malicious files, including .DLL and .SO files, to target both Windows and Linux platforms. The malware, named ZiChatBot, uses a unique approach by leveraging the REST APIs from the public team chat app Zulip as its command and control server, rather than traditional dedicated servers.

The attackers created fake libraries, including uuid32-utils, library, colorinal, and termncolor, which were designed to imitate popular libraries and trick users into downloading them. The termncolor library, for example, appears to be harmless but imports the malicious colorinal library as a dependency, allowing the attackers to conceal the malware. Once a user downloads and installs one of these malicious packages, the ZiChatBot dropper is extracted and placed on the victim's hard drive, and the malware is deployed.

The ZiChatBot malware is capable of executing shellcode received from the Zulip REST API and uses two separate channel-topic pairs for its operations. One pair transmits system information, while the other retrieves a message containing shellcode. The malware also establishes an auto-run mechanism to maintain persistence on the infected device. The Linux version of the dropper places ZiChatBot in the /tmp/obsHub/obs-check-update path and creates an auto-run job using crontab.

The attribution of this attack to OceanLotus is based on the similarity between the ZiChatBot dropper and another dropper analyzed in a previous Threat Intelligence report. The droppers use nearly identical algorithms and logic to decrypt and decompress their embedded payloads. OceanLotus is an active APT organization that primarily targets victims in the Asia-Pacific region, but has been expanding its activities to the Middle East. This attack demonstrates the group's ongoing effort to broaden its attack scope and explore new ways to compromise victims through diverse supply chain attacks.

The indicators of compromise, including the malicious wheel packages and dropper files, have been made available to customers of the Kaspersky Intelligence Reporting Service. Users are advised to add the full URL helper.zulipchat.com to their denylist to help locate and cure infected devices. The swift removal of the malicious software from PyPI and the deactivation of the organization registered on the Zulip service have likely prevented widespread

---

> *The way we communicate with others and with ourselves ultimately determines the quality of our lives.
Author: Tony Robbins*

Source: [OceanLotus suspected of using PyPI to deliver ZiChatBot malware](https://securelist.com/oceanlotus-suspected-pypi-zichatbot-campaign/119603/)
