---
title: Current Limitations in RDBMSs
authors: Alessandro Dorigo
tags:
  -
---

> [!question]+ Limitations:
> - Domains have been underused: in SQL and RDBMSs in general, domains are restricted to the data types of traditional programming languages (e.g., integer, real, character) and date
> - In more modern languages (e.g., object-oriented), domains are application dependent (e.g., employee names, salaries)
## Practical Examples

> [!example]- Exemple
> City names and person names may both be represented as character strings at the implementation level.
>
> With proper domain support:
> ```
> CREATE DOMAIN CityName AS VARCHAR(30);
> CREATE DOMAIN PersonName AS VARCHAR(50);
> ```
> A language that would support application-oriented domains could forbid (by type checking) comparing a city name with a person name.
