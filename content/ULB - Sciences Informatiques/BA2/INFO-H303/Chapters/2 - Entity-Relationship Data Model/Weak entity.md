---
title: Weak entity
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ Definition
> A **weak entity** is an [[Entity#^8bb8a4|entity]] that cannot be uniquely identified by its own attributes alone and depends on a related strong entity for its identification.

1) It lacks a Primary Key (no unique identifier)
2) Requires a strong entity
3) Uses a Partial Key
4) Has an identifying Relationship
5) Depends on total participation (every weak entity must be associated with a strong entity)

> [!example]
> ![[Pasted image 20250303160151.png]]
> In this example, the various dependents of a given employee can be distinguished by their name, but dependents of distinct employees can have the same name; to distinguish a dependent from all other dependents, the name of the dependent and the identification of an employee are needed.
>
> Suppress the weak entity in this example:
> - Add a `SSN` attribute to `Dependent`
> - Add the following constraint: for each dependent `d`, the value of its `SSN` attribute is equal to the `SSN` value of the employee linked to `d` by an instance of relationship `DepOf`
