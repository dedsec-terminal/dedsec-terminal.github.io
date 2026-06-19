---
title: "74,000 Fortinet firewall credentials exposed in FortiBleed data leak"
date: 2026-06-18T12:10:49+00:00
draft: false
categories:
  - data-breaches
author: "DedSec-Terminal"
---

A Russian-speaking cybercriminal group has exposed nearly 74,000 Fortinet firewall credentials in a data leak known as FortiBleed. The leak was discovered by security researcher Volodymyr "Bob" Diachenko, who found that the group had accidentally exposed the data on a server. The exposed credentials include logins and passwords for Fortinet firewalls and VPN gateways around the world, with many of the devices being on recent patches.

The credentials were compromised through automated large-scale credential harvesting, where the group intercepted SSL VPN authentication hashes, cracked them using a 45-GPU cluster, and used the passwords to gain access to internal Active Directory environments. The group successfully targeted 73,932 unique firewall URLs across 194 countries, with many of the devices having their management interface exposed to the internet. Fortinet believes that the leak includes data collected during previous incidents and via brute-forcing, and that many devices still store credentials using a weaker method that is vulnerable to cracking via brute-force attacks.

Organizations using Fortinet firewalls and gateways can check if they are affected using a look-up tool launched by Hudson Rock. If their domains and IP addresses are on the list, they should assume compromise and check for compromised accounts, backdoor users, and altered security controls. To mitigate the issue, affected devices should be upgraded to the latest FortiOS release, and their management interface should be pulled from the internet if possible. Credentials should also be rotated, multi-factor authentication enforced, and admins should log in to force the system to re-hash passwords using the more secure PBKDF2 standard. Many high-profile organizations, including government agencies and critical infrastructure sectors, are affected by the leak.

---

> *Silences make the real conversations between friends. Not the saying but the never needing to say is what counts.
Author: Margaret Runbeck*

Source: [74,000 Fortinet firewall credentials exposed in FortiBleed data leak](https://www.helpnetsecurity.com/2026/06/18/fortinet-fortibleed-data-leak/)
