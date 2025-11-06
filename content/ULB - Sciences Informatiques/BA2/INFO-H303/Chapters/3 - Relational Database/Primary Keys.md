---
title: Primary Keys
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Primary Key
> > [!info]+ Definition
> A **Primary Key** is a designated candidate key chosen to be the principal means of uniquely identifying tuples within a relation. It consists of one or more attributes whose combined values uniquely identify each tuple in the relation and satisfy the following properties:
>
> 1. **Uniqueness**: No two distinct tuples in any valid relation instance can have the same value for the primary key
> 2. **Minimality**: No proper subset of the primary key attributes can uniquely identify tuples (this makes it a candidate key)
> 3. **Non-null**: Primary key attributes cannot contain null values (entity integrity constraint)
> 4. **Stability**: The values should rarely or never change during the lifetime of the entity they identify

> [!tip]+ Remarque
> The concept of relation key (primary or not) should not be confused with that of indexes (also sometimes called "keys" in traditional data management)
> - A key is a semantic concept, that serves to identify objects in the application domain
> - An index is a physical concept used for performance optimization
> - A key may or may not be indexed, and an index may or may not be a key

> [!tip]+ Role in Database Design
> The primary key serves multiple critical functions:
>
> 1. It enforces entity integrity by ensuring each row represents a unique entity
> 2. It provides a guaranteed method to reference specific tuples
> 3. It often serves as the target of foreign keys from other relations
> 4. It typically determines the physical organization of data in storage
>
> For relations representing relationships (e.g., many-to-many relationships), the primary key is typically formed by combining the primary keys of the participating entity relations.

> [!example]- Exemple
> In an `Employee` relation:
>
> ```
> Employee(SSN, FirstName, LastName, BirthDate, Department)
> ```
>
> The attribute `SSN` (Social Security Number) might be designated as the primary key because:
> - Each employee has a unique SSN
> - SSN values don't change over time
> - It's a single attribute (simpler than composite keys)
> - It naturally identifies employees in the real world
