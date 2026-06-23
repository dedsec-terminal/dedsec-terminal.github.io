---
title: "ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack"
date: 2026-06-22T18:00:48+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

A supply chain attack has compromised multiple WordPress plugins from ShapedPlugin, allowing unknown threat actors to inject backdoor code into Pro plugin releases. The affected plugins include Product Slider Pro for WooCommerce, Real Testimonials Pro, and Smart Post Show Pro, with specific versions being vulnerable to the attack. The compromise only affects Pro plugin builds distributed through the vendor's Easy Digital Downloads infrastructure, while the free versions of the plugins on WordPress.org remain unaffected.

The compromised plugins incorporate a loader that fetches a payload from a remote server, installs it, and activates it as a fake plugin. This malware can capture credentials in plaintext and two-factor authentication codes, establish persistence methods, and drop a web shell with command execution features. It also extracts sensitive data, including database credentials, authentication keys, and WooCommerce order data, before deleting itself to cover its tracks. The attack has been assigned CVE identifiers and has a high CVSS score, indicating maximum severity.

ShapedPlugin has confirmed the incident and is reviewing its distribution and release processes to ensure the integrity of its products. Site owners who have installed the malicious versions are advised to take immediate action, including resetting all passwords, revoking and regenerating 2FA secrets, reviewing administrator accounts, and checking mail plugin configurations. New versions of the impacted plugins are expected to be released pending comprehensive security reviews and validation tests. The attack highlights the risks of supply chain attacks, where legitimate software updates can be compromised, exposing users to malware and other security threats.

---

> *The heart has its reasons which reason knows not of.
Author: Blaise Pascal*

Source: [ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack](https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html)
