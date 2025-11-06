---
title: Entity role
authors: Alessandro Dorigo
tags:
  - Databases
---


Each entity type plays a role or function in a relationship

![[Pasted image 20250303140523.png]]

• Employee plays role WorksFor and Department plays role Employs
• Role names are convenient carriers for alternative (redundant) relationship names:
relationships can thus have
3 a neutral name (Affiliation)
3 names (WorksFor, Employs) from the point of view of each entity involved,
suggesting directed traversal of the relationship
• Role names are similar to class attributes (attributes whose value is the same
for all entities in an entity type)
