---
title: Relationship instance
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ Definition
> A **Relationship instance** $r_i = (e_1, \dots, e_n) \in R$ is a specific **occurrence** of a relationship where each $e_i \in E_i$ links between individual entities (e.g., an individual employee working for a department).
>
> ![[Pasted image 20250217160028.png]]

- If an **employee (`e1`) is connected to `d1`**, it means **employee `e1` works for department `d1`**.
- If multiple employees (`e2, e3, e4`) are connected to `d2`, they all work for that same department.
- The **"WorksFor"** relationship **enforces** that every employee has exactly **one** department, but departments may have **multiple** employees.
