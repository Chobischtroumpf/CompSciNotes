---
title: Relationship type
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ Definition
> A **relationship type** $R$ models an **association** between two or more $E_1, \dots, E_n$ [[Entity#^8bb8a4|entities]] (e.g., `WorksFor` between `Employee` and `Department`).
>
> ![[e10850c7735b4db5397a11806d59df71.png]]

- `(1,1)` on the **Employee** side → Each **employee** **must** work for exactly **one** department.
- `(1,n)` on the **Department** side → Each **department** can have **one or more** employees.
