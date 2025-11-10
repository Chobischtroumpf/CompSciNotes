---
title: Relation Schema and Relation Value
authors: Alessandro Dorigo
tags:
  -
---

## Formal Definitions

![[Relation Schema]]
![[Tuples]]
![[Relation Value]]

## Alternative Notations

- Some notations leave domains implicit: $R(A_1, \ldots, A_n)$ (but domains must be specified in the relation schema, i.e., CREATE TABLE in SQL)
- Some notations leave attributes implicit: $\{⟨d_1, \ldots, d_n⟩ | d_i \in D_i\}$, but attributes are essential because the same domain can appear several times in the same relation

> [!tip]+ To note
> When attributes are omitted in the notation, the idea is that relation columns are ordered (i.e., that relation columns can be identified by their position): this is not the correct definition of the relational model

## Mathematical Foundation

> [!abstract]- Formula
> Relations, and algebraic and calculus operations on them can be naturally formalized in terms of an indexed Cartesian product of domains:
> $$A_1 : D_1 \times \ldots \times A_n : D_n$$
> The value of a relation = a subset of the indexed Cartesian product
