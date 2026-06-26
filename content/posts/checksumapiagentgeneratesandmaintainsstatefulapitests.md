---
title: "Checksum API Agent generates and maintains stateful API tests"
date: 2026-06-25T13:51:39+00:00
draft: false
categories:
  - threat-intel
author: "DedSec-Terminal"
---

Checksum has introduced the API Agent, a continuous testing tool that generates and maintains stateful API tests. This agent creates multi-step tests that reflect real-world API usage, keeping them up-to-date as the API evolves, and integrates them into existing development pipelines. The goal is to bridge the gap between rapid API development and the slower process of writing tests to cover new endpoints.

Traditional spec-based generators only test individual endpoints, neglecting the complex interactions and state changes that occur between them. In contrast, the API Agent generates stateful, multi-step tests that capture dynamic values like IDs and tokens, covering both successful and error flows. These tests are produced in a standard format, such as PyTest, making them readable and maintainable for engineers. By using the API Agent, teams have seen a significant reduction in test failure rates, with an average decrease of 82% compared to manual test maintenance.

The API Agent streamlines the testing process, allowing engineers to generate complete API journeys with automatically wired values between steps. It can start from a spec or captured traffic, without requiring a repository connection, and achieve meaningful coverage across a large API surface in a matter of days. When changes occur, the agent identifies affected journeys and proposes updates for review, ensuring that tests remain accurate and reliable. By integrating with Checksum's end-to-end agent, teams can now manage both API and end-to-end coverage from a single platform.

---

> *A life spent making mistakes is not only more honourable but more useful than a life spent in doing nothing.
Author: Bernard Shaw*

Source: [Checksum API Agent generates and maintains stateful API tests](https://www.helpnetsecurity.com/2026/06/25/checksum-api-agent-generates-and-maintains-stateful-api-tests/)
