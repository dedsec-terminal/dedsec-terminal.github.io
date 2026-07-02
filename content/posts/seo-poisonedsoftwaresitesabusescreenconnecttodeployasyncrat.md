---
title: "SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT"
date: 2026-07-01T17:53:06+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Here is a summary of the article in three concise paragraphs:

Unknown threat actors are using the ScreenConnect remote access tool to deploy and execute AsyncRAT, a type of malware. This is part of a large-scale campaign that involves creating fake websites that mimic popular software download pages, such as OBS Studio and Bandicam. These websites are hosted on over 90 domain names across 10 languages, including English, Russian, and Chinese, and are designed to trick users into downloading malicious installer archives.

The malicious installers bundle a legitimate Microsoft binary with a rogue DLL library, which is loaded onto the device via DLL side-loading. This deploys the ScreenConnect service, allowing the threat actors to maintain control over compromised endpoints. Once ScreenConnect is running, it creates and executes a PowerShell script that configures Microsoft Defender exclusions, disables User Account Control prompts, and creates a VBScript file. This script ultimately leads to the execution of the AsyncRAT module, which is extracted from a hidden file and run using process hollowing.

The AsyncRAT malware establishes a connection to a remote server, allowing the threat actor to control infected Windows systems, steal sensitive data, and monitor user activity. The malware also sets up a scheduled task to ensure persistence, even after a system reboot. The threat actors use search engine optimization techniques to push their fake websites to the top of search results, making it more likely that users will download the malicious installers. This campaign has affected individual users and organizations, highlighting the need for caution when downloading software from the internet.

---

> *Open minds lead to open doors.*

Source: [SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT](https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html)
