---
title: Introduction to the Relational Model
authors: Alessandro Dorigo
tags:
  -
---

## Bases of the Relational Model: Summary
- Relations
- Constraints
- Update operations
- Data manipulation (later chapters)
  - Algebra
  - Tuple relational calculus
  - Domain relational calculus
  - SQL

## Intuitive View of Relations

> [!info]+ Definition
> Relations are tables with some restrictions:
> - The order of rows is immaterial
> - The order of columns is immaterial
> - Relations have no duplicate rows ⇒ each relation has one or more key

- Popular view of the relational model = information is structured as 2-dimensional tables of simple values (with lines, or rows, or tuples, and columns, or attributes)
- A relation can also be seen as a predicate, i.e., a set of properties, assertions
- Database = collection of relations, but
  - Relational data structures are richer than tables
  - A data model is not just data structures but also operations for manipulating the data structures

> [!abstract]- Key Properties of Relations
> - The order of rows and columns is immaterial = manipulating (querying or updating) relations cannot depend or rely on relations being ordered
> - In fact, a relation is a set of tuples (row or lines in a table)
> - Sets are unordered ⇒ the tuples in a relation are unordered (there is no notion of "first" tuple or "next" tuple)
> - If the output of a program or of a query must be ordered, this should be explicitly requested in the program or query
> - The elements of a set are all distinct ⇒ there are no duplicate tuples in a relation (but SQL allows duplicate tuples)
> - A set may be implemented as a file (i.e., as some kind of table or sequential structure), but this is a physical implementation, and the order of records in a file (or of rows in a table) is not visible to users, i.e., may not be exploited in application programs (physical data independence)
