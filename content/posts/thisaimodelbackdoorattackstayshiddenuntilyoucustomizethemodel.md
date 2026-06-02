---
title: "This AI model backdoor attack stays hidden until you customize the model"
date: 2026-06-02T04:30:56+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Researchers have discovered a new type of AI model backdoor attack called BadBone, which remains hidden until the model is customized for a specific task. This attack plants a backdoor in a pre-trained model, which is then inherited by downstream tasks that adapt the model. The backdoor is dormant until two conditions are met: the model is customized using prompt learning, and the attacker's trigger appears in an input. This makes it difficult to detect, as the model behaves normally until it is customized and the trigger is present.

The BadBone attack is more stealthy than traditional backdoor attacks, which can be detected by feeding the model unusual inputs and watching for suspicious responses. In contrast, the BadBone backdoor remains inert during security checks, allowing it to pass as a clean model. Six published defenses were tested against the poisoned models, and most of them failed to detect the backdoor. The attack is successful, with a trigger fooling the customized model nearly 99% of the time, while the model continues to perform well on everyday inputs.

The discovery of the BadBone attack highlights the risks associated with downloading pre-trained models from unverified sources. It emphasizes the need for new defenses, such as prompt-agnostic behavioral consistency checks and cross-task anomaly analysis. The research team has released its code publicly to facilitate defensive research and has provided directions for developing new defenses. The attack demonstrates that AI models can be a vulnerable part of the software supply chain, and organizations should be cautious when using pre-trained models and consider the potential risks associated with customization and deployment.

---

> *Keep your eyes on the stars and your feet on the ground.
Author: Theodore Roosevelt*

Source: [This AI model backdoor attack stays hidden until you customize the model](https://www.helpnetsecurity.com/2026/06/02/ai-model-backdoor-attack-research/)
