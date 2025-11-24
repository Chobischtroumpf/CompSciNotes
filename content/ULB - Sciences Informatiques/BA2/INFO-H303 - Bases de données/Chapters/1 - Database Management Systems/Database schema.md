---
title: Database schema
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ Definition
> The definition of the database structure, accessible by programs.

^ae34f4

- [[Database Management System (DBMS)#^4c30d6|DBMS]] software is application-independent as it consults the database structure in the data dictionary to understand and execute application programs.

> [!note]
> **Ontology** is another more recent term for designating the structure of an application domain (= schema information valid for several related applications).

> [!example]
> ![[ce65d32c7ca6c0b1adbfa9e24c4749c4.png]]

> [!tip]
> A [[Database Management System (DBMS)#^4c30d6|DBMS]] provides users with a conceptual representation of information from their point of view and a physical or internal representation with the implementation details.
> - **In practice:** Users refer (separately) to the conceptual representation and the [[Database Management System (DBMS)#^4c30d6|DBMS]] ensures the correspondence with the physical representation.

### Conceptual vs Physical Schemas

| ![[7cacb4033f60dcea16b1a6e9dc663232.png]] | ![[a5365b5ba133c7e066fa3b8b2239ae4b.png]] |
| :----------------------------------: | :----------------------------------: |
|          Conceptual Schema           |           Physical Schema            |
