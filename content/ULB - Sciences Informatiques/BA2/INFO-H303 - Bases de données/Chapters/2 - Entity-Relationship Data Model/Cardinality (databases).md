---
title: Cardinality (databases)
authors: Alessandro Dorigo
tags:
  - Databases
---


Minimum and maximum number of relationship instances in which each entity can participate
The cardinality information belongs to the schema

- Optional (min card = 0)
- Mandatory (min card >= 1)

![[86d71ac1ba9654839bfd89cde405a072.png]]
Two ways of noting cardinalities:
1) On the side of the origin entity as above (e.g., each Building participates in a number of instances of Owns comprised between 1 and 1, i.e., equal to 1)
2) On the side of the target entity (e.g., starting from any Building, the number of Persons reached thru Owns is comprised between 1 and 1, i.e., equal to 1)

Binary -> one to one, one to many, many to many

Example
![[53ceab3f4d6ddbd7838f708697f7872d.png]]
