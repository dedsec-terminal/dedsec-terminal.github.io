---
title: "FortiBleed Targeted FortiGate Firewalls in 110 Million-Credential Harvesting Operation"
date: 2026-06-23T18:20:49+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A large-scale credential-harvesting operation known as FortiBleed has been targeting over 430,000 FortiGate firewalls globally, with the primary goal of collecting credential lists and deploying bespoke sniffers on compromised firewalls. The campaign, active since February 2026, is driven by a Russian-speaking initial access broker (IAB) seeking financial gain. The operation involves collecting credentials, searching for exposed services, brute-forcing accessible systems, and deploying sniffers to capture cleartext and hashed credentials from traffic passing through compromised devices.

The FortiBleed campaign utilizes a Golang-based tool called FortigateSniffer, which takes advantage of the FortiOS built-in diagnostic command to passively capture authentication traffic from infected appliances. The tool monitors traffic across 24 protocols, parses authentication data, and extracts credentials. The threat actors may have also used an open-source, AI-native offensive security platform called CyberStrike to assist with parts of the workflow. The campaign has a heavy focus on Small and Medium Businesses (SMBs) with fewer than 200 employees, targeting multiple sectors and regions, including the United States and India.

The FortiBleed campaign has resulted in the identification of over 110 million credentials, including RADIUS credentials, NTLM hashes, Kerberos hashes, and MySQL authentication tokens. The operation takes place over five stages, from reconnaissance to exfiltration of sensitive data. The threat actors have been estimated to have launched at least 659 credential-harvesting pipelines, with the group ranking targets according to economic value before allocating exploitation resources. The operation's sniffing mechanism includes a geofencing filter and limits activity to specific IP ranges and time frames, suggesting a high level of sophistication and organization.

---

> *Sometimes your joy is the source of your smile, but sometimes your smile can be the source of your joy.
Author: Thich Nhat Hanh*

Source: [FortiBleed Targeted FortiGate Firewalls in 110 Million-Credential Harvesting Operation](https://thehackernews.com/2026/06/fortibleed-targeted-fortigate-firewalls.html)
