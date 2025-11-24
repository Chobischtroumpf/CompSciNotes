---
title: Programming Tuple Insertion
authors: Alessandro Dorigo
tags:
  -
---


> [!tip]
> If insertion violates a constraint, then:
> - Either reject insertion
> - Or correct violation

> [!Example]- Examples
> - Tuple to be inserted has a null value for primary key: ask user for a value and proceed with insertion
> - Value for a foreign key does not exist in the relation where the attribute(s) is primary key: ask user for a new tuple in that relation (possibility of cascading updates)
