---
title: "Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI"
date: 2026-06-06T08:29:05+00:00
draft: false
categories:
  - malware
author: "DedSec-Terminal"
---

A researcher has discovered that free apps on smart TVs are being used as web-scraping proxies for AI companies through a company called Bright Data. The company embeds its SDK in consumer apps, which turns devices, including smart TVs, into exit nodes that relay web-scraping traffic. This is done behind an opt-in screen that claims to use the device's connection "occasionally," but in reality, the SDK can use up to 200 GB of traffic per month and can even tie together a person's phone and computers.

The researcher found that the channel used to carry scraping jobs has no real authentication and bypasses VPNs on iOS devices. This means that the device can continue to relay traffic in the background while the user is watching TV or on a call, without their knowledge. The SDK is used by several smart TV app makers, including PlayWorks Digital, CloudTV, and Longvision, although it's unclear if these apps still include the SDK. Bright Data's platform support and public partner list suggest that the issue is widespread, and the company's successor to Luminati has been operating a similar model since 2015.

To mitigate this issue, users can block the web addresses used by the SDK, such as proxyjs.brdtnet.com and clientsdk.bright-sdk.com, using a router-level tool like Pi-hole or NextDNS. Companies can also scan for apps that carry the SDK on staff phones. However, it's worth noting that Bright Data could change how the SDK connects in the future, which would require updating any blocklist. The researcher's findings highlight the need for greater transparency and control over how devices are used for web scraping, and the potential risks of "free" apps that use device connections for commercial purposes.

---

> *To hell with circumstances; I create opportunities.
Author: Bruce Lee*

Source: [Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI](https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html)
