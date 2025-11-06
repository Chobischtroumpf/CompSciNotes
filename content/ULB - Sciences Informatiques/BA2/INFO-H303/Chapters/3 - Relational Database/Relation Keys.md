---
title: Relation Keys
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Définition
> **Superkey** = one (or more) attributes that (together) possess the property of unique tuple identification
> - Their values always uniquely identify at most one tuple in the relation
> - Unicity constraint = no two tuples with the same value for those attributes

> [!info]+ Définition
> **Key** = minimal superkey, i.e., a group of attributes that loses the property of unique identification if any one attribute is removed from the group

> [!tip]+ Properties of Keys
> - The set of all attributes of a relation is a superkey (because the value of a relation is a set of tuples)
> - In general, a relation has several keys (candidate keys)
> - The definition of keys is intensional information (i.e., it belongs to the schema) ⇒ it must be satisfied by all legal extensions of the relation
