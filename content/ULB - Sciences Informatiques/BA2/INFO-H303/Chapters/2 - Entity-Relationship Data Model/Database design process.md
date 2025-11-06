---
title: Database design process
authors: Alessandro Dorigo
tags:
  - Databases
---


![[Pasted image 20250217154350.png]]

Real world -> Requirements collection -> Database requirements -> Conceptual design -> Conceptual schema -> Logical design -> Logical schema -> Physical design -> Internal schema

No one should know everything
Higher level means less access
HRs have most access, but not total access

1) Dimension (table size, columns)
2) Split by sectors
3) Evaluate impact by adding columns by consulting with the other sectors
4) Choose technology after mapping all info out (99% of the time relational mapping lol)
