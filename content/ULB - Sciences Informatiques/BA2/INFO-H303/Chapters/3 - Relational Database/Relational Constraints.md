---
title: Relational Constraints
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> > [!info]+ Définition
> > **Relational Constraints** are rules that restrict the possible states of a relational database to those that satisfy specific conditions. They are formal assertions about the schema (not the data) that must be satisfied by all valid database instances at all times.
> > Constraints represent business rules, logical necessities, and integrity requirements that cannot be expressed through the basic structure of relations alone.
> - Constraints cannot be deduced from the current extension of the database (they are part of the database schema)
> - Relational constraints can be classified as:
  >    - Keys (candidate keys, primary key)
  >    - Various dependencies (functional, multi-valued, etc.)
  >    - Referential integrity
  >    - "Ad-hoc" constraints (all the constraints specific to an application domain)

> [!tip]+ Remarque
> Constraint = all that you would like to express at the level of the structure of the database (i.e., the schema) and that you cannot express with the mechanisms for structure description available in the data model.
>
> The traditional term is "integrity constraint", although "consistency constraint" or "schema constraint" would be better terms.

## Constraints versus Data Structures
- There is no fundamental difference of nature between constraints and data structures: the distinction depends on the power of the data-structuring mechanisms
- The same piece of information can be modeled as fact or as constraint, depending on its stability (e.g., headquarters are located in Houston)
