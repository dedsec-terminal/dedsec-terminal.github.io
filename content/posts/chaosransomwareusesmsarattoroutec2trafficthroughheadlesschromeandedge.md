---
title: "Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge"
date: 2026-07-23T13:11:09+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

Here are three concise paragraphs summarizing the Chaos ransomware group's use of msaRAT to route command-and-control (C2) traffic through headless Chrome and Edge browsers:

The Chaos ransomware group has been using a Rust implant called msaRAT to route C2 traffic through a victim's own browser. The implant starts a headless Chrome or Edge browser and uses the Chrome DevTools Protocol to drive the browser, allowing it to send and receive C2 messages without opening an outbound connection. The messages are then relayed through Twilio's TURN service, making it appear as if the browser is communicating with Cloudflare and Twilio, rather than the attacker's server.

The msaRAT implant looks for Chrome or Edge on the victim's system and starts the browser in headless mode, enabling the Chrome DevTools Protocol and creating a new user data directory. It then injects JavaScript into the browser, which fetches STUN and TURN configuration from a Cloudflare Worker and builds a peer connection. The implant uses this connection to send and receive encrypted C2 messages, which are then executed by the Windows command line. The use of a headless browser and WebRTC data channels makes it difficult for defenders to detect the C2 traffic.

The delivery of the msaRAT implant is relatively straightforward, involving a curl download of a fake Windows update MSI file that loads a DLL into memory. However, the technique used to route C2 traffic through a headless browser is more sophisticated and may be difficult for defenders to detect. Defenders can look for signs of a headless browser being launched by an installer or service, and correlate this with loopback traffic to the debugging port and outbound WebRTC traffic. However, the indicators of compromise (IOCs) published by Cisco Talos are narrow and may not be effective in detecting all instances of the malware.

---

> *In the sky, there is no distinction of east and west; people create distinctions out of their own minds and then believe them to be true.
Author: Buddha*

Source: [Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge](https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html)
