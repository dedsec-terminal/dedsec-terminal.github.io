---
title: "A forensic tool for backdoored code completions in AI assistants"
date: 2026-07-20T05:00:56+00:00
draft: false
categories:
  - research
author: "DedSec-Terminal"
---

Here are 3 concise paragraphs summarizing the article:

A team of researchers from the University of Louisville and the University of North Texas has developed a forensic tool called CodeTracer to detect and trace backdoored code completions in AI assistants. The tool is designed to work after a model has already produced a harmful completion, tracing it back to the training examples that taught the behavior. This is a crucial step in identifying the source of the problem and preventing similar issues in the future.

CodeTracer works in three stages: reading the harmful completion and building a structured summary of the unsafe behavior, searching the training data for code that carries the same underlying logic, and asking a language model to weigh each candidate against the summary and decide whether it holds the same unsafe pattern. The tool uses a combination of natural language processing and code analysis techniques to identify the source of the problem. In testing, CodeTracer was able to accurately identify the source of the problem with a low false negative rate and a low cost per completion.

The researchers evaluated CodeTracer using a large dataset of Python source files from GitHub repositories, including a small number of poisoned examples. The results showed that CodeTracer was able to accurately identify the source of the problem in most cases, with a false negative rate of less than 0.03%. The tool was also able to withstand direct attacks, including attempts to hide malicious code or steer the language model's judgment. The researchers believe that CodeTracer has the potential to be a valuable tool for developers and security teams, and plan to extend the idea to AI agents in the future.

---

> *They say that time changes things, but you actually have to change them yourself.
Author: Andy Warhol*

Source: [A forensic tool for backdoored code completions in AI assistants](https://www.helpnetsecurity.com/2026/07/20/tracing-backdoored-code-completions/)
