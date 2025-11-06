---
title: Base and Derived Relations
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ **Base Relations**
>  Base Relations are explicitly created, named relations that have their own persistent storage within the database. They represent the primary data containers in a relational database and are directly manipulated through insert, update, and delete operations.

> [!info]+ **Derived Relations**
> Derived Relations are relations whose contents are defined by a query expression operating on other relations (base or derived). They do not have their own independent stored data but are computed on demand from their defining expressions.
## Derived Relations: Views

> [!info]+ Définition
> **Views** are derived relations that can be presented to application programs (ANSI external schemas)

- Views are redundant and consistent with the underlying base relations
- Views simplify application programs
- Views may or may not be materialized (i.e., stored on disk): this is an efficiency issue that should be under the control of the DBMS and invisible to users
- Storing them:
  - Introduces physical redundancy and complicates integrity enforcement
  - Accelerates querying and slows updating

## Derived Relations: Snapshots

> [!info]+ Définition
> **Snapshots** are derived relations that are not synchronized at all times with base relations

- Refreshed from base relations at regular intervals
- Users of snapshots accept to work with data that is not up-to-date to gain efficiency in access times (particularly for distributed data)
- To easily establish consistency at refreshing times, snapshots may be restricted to read-only access
