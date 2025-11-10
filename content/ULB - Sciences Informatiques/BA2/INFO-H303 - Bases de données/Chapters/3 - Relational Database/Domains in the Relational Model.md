---
title: Domains in the Relational Model
authors: Alessandro Dorigo
tags:
  -
---

## Core Definition

> [!info]+ Definition
> **Domain** = a named set of atomic values, a set of possible values for an attribute
>
> Domains carry important structural information and define the type system of the relational model.

> [!abstract]- Properties
> For a relation schema $R(A_1 : D_1, \ldots, A_n : D_n)$:
> - Each attribute $A_i$ is associated with exactly one domain $D_i$
> - Values for attribute $A_i$ must come from domain $D_i$: $\forall t \in R, t[A_i] \in D_i$

## Importance of Domains

- Domains define comparability of values: attribute values can only be meaningfully compared if they range on the same domain (= typing checking in programming languages)
- Relations are value-based: elementary values are the smallest units of information

> [!tip]+ Of note
> Domains could be viewed as conceptual user-defined data types (e.g., part numbers, city names, person names, dates, weights), carrying more application semantics than their representation at a lower level as traditional data types (e.g., integer, real, character)

![[Current Limitations in RDBMSs]]
## Enhanced Domain Capabilities

> [!important] A richer version of domains could include:
> - Conversion functions, a set of applicable operations on domain values (e.g., computation, ordering) like abstract data types (ADTs)
> - Operations to combine values from different domains
> - Application-dependent structures not possible with RDBMSs (e.g., geometric figures, design objects): this is one advantage of object-oriented systems
