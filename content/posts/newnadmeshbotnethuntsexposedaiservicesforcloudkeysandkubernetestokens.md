---
title: "New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens"
date: 2026-07-17T17:12:23+00:00
draft: false
categories:
  - cves
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A new Go botnet called NadMesh has been discovered, which targets exposed AI services to steal cloud keys and Kubernetes tokens. The botnet uses a Shodan harvester to scan for vulnerable services such as ComfyUI, Ollama, and Gradio, and has claimed 3,811 unique AWS keys. The operator's dashboard shows a high number of credential hauls and model inventories, suggesting that the botnet is successful in its exploits.

The botnet is designed to exploit cloud credentials, Kubernetes cluster privileges, and model access, with a focus on MCP (Model Control Protocol) tools. The operator's priority is to exploit MCP services, followed by Kubernetes, Docker API, and Redis. The botnet uses various exploits, including JSON-RPC tools and weak passwords, to gain access to vulnerable services. The researchers note that the botnet's removal is built to fail, with multiple persistence mechanisms and obfuscation techniques making it difficult to detect and remove.

To protect against NadMesh, users are advised to secure exposed services and admin functionality, such as Docker API, Jenkins script console, and Redis, by putting them behind authentication or removing them from the public internet. Users should also patch vulnerable services, including Marimo notebooks and rclone RC servers, and check for suspicious files and cron jobs. If an infection is detected, users should isolate the host, revoke credentials, and review where the old credentials were used while they were live. The researchers provide indicators of compromise, including a C2 domain and an agent sample, to help users detect and respond to NadMesh infections.

---

> *If we could learn to like ourselves, even a little, maybe our cruelties and angers might melt away.
Author: John Steinbeck*

Source: [New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens](https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html)
