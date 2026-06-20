---
title: "Companies are discarding the logs they need to catch a breach"
date: 2026-06-19T05:00:43+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Many large enterprises are intentionally discarding most of their log data to reduce costs, with half of organizations dropping or never collecting an average of 86% of their logs. This decision is made by teams responsible for observability, platform engineering, or cost control, who are driven by spending targets. However, this choice has significant security implications, as logs are essential for threat hunting, incident response, and forensics. By discarding log data, organizations may be leaving themselves vulnerable to undetected breaches and limiting their ability to investigate security incidents.

The decision to discard log data is often made without consideration for security needs, and security teams may not even be aware of what data is being collected or retained. The cost of log management is a significant factor, with spending on logging tools averaging $2.5 million per year at large enterprises. To reduce costs, teams may limit storage duration, sample a subset of common logs, or stop collecting certain categories of data. However, this can narrow the field of view that security teams depend on to investigate incidents, making it more difficult to detect and respond to breaches.

The use of AI workloads is exacerbating the problem, as it generates large volumes of log and telemetry data, driving up costs and leading to further data discard. However, AI systems also rely on log data to function, and discarding this data can leave organizations with limited visibility into their AI applications. Furthermore, AI agents that read and write logs can become targets for tampering or injection, highlighting the need for security teams to examine the security implications of log data management. Ultimately, the decision to discard log data is a governance issue, and security leaders need to confirm what data is being collected, retained, and discarded to ensure their organization's security needs are being met.

---

> *Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less.
Author: Marie Curie*

Source: [Companies are discarding the logs they need to catch a breach](https://www.helpnetsecurity.com/2026/06/19/report-log-management-security-risk/)
