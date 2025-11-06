---
title: Programming Tuple Suppression
authors: Alessandro Dorigo
tags:
  -
---


> [!tip]+ If suppression violates a referential constraint, then:
> - Either reject suppression
> - Or propagate suppression to the tuples that reference the suppressed tuples
> - Or set to null the attribute values that reference the suppressed tuple (unless these attributes are part of the primary key)

> [!Example]- Examples
> - Suppress a department ⇒ suppress its locations
> - Suppress an employee ⇒ suppress his/her dependents
> - Suppress a department ⇒ set to null the reference to a department in projects, until projects are assigned to another department
