---
title: "Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers"
date: 2026-07-10T11:47:43+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

A vulnerability known as XRING has been discovered in XQUIC, Alibaba's open-source QUIC and HTTP/3 library. The flaw allows a remote client to crash an HTTP/3 server with a short burst of legal traffic, requiring no login or malformed packets. The issue is caused by a single incorrect variable on one line of code, which leads to a memory copy operation that runs off the end of memory, resulting in a crash.

The vulnerability affects all releases of XQUIC up to v1.9.4, including Tengine, Alibaba's Nginx-based web server, which is used to front the company's cloud and CDN on sites such as Taobao and Alipay. To mitigate the issue, operators can set SETTINGS_QPACK_MAX_TABLE_CAPACITY to 0, which turns off QPACK's dynamic table, or drop HTTP/3 support entirely. However, there is currently no fixed release or CVE assigned to the vulnerability.

The XRING flaw is the latest in a series of remote crashes in HTTP/2 and HTTP/3 stacks, including a use-after-free in NGINX's HTTP/3 module and the HTTP/2 Bomb, which caused remote denial of service against several popular web servers. FoxIO researcher Sébastien Féry disclosed the XRING vulnerability on July 8, after attempting to contact Alibaba's security team five times without receiving a response. The vulnerability has been demonstrated to cause a crash, but it is unclear whether it can be exploited further to achieve code execution.

---

> *Slow down and everything you are chasing will come around and catch you.
Author: John De Paola*

Source: [Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers](https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html)
