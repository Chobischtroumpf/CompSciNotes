---
title: Attribute
authors: Alessandro Dorigo
tags:
  - Databases
---


> [!info]+ Definition
> An **attribute** is a **column** in a database [[Table#^a376c8|table]] that represents a specific property of an [[Entity#^8bb8a4|entity]]. Each attribute has a **data type** and may have constraints. (e.g., `StudentNo` in a `Student` table uniquely identifies each student).

^eca05e

Attributes model details of entities or relationships
![[Pasted image 20250303142820.png]]

• An entity or relationship instance has a value for each attribute
• Attributes have a value set or domain (set of possible values)
• Domain values are distinct, more abstract than their interpretation as lower level
data (name of person, profession of person, name of city are distinct domains
although represented as strings of characters)

Attribute of an entity or of a relationship?
• Relationship attributes are really necessary only for n-ary and many-to-many binary
relationships
• Otherwise, attributes can be attached to entities, although it may be natural to attach
attributes to binary relationships
3 MovingDate can be an attribute of relationship LivesIn or of entity type Person
3 if the history of residences becomes relevant (i.e., the maximal cardinality of
Person in LivesIn is ≥ 1), then MovingDate is necessarily an attribute of LivesIn
3 schema evolution (from modeling a single residence to modeling their history) is
made easier

Attribute Cardinalities
• Like relationships, attributes have minimal and maximal cardinalities
• Optional ⇔ Mandatory
3 mandatory: min-card ≥ 1
3 optional: min-card = 0
• Several possible meanings for “null values”:
3 not applicable: (a person does not have a university degree)
3 unknown but known to exist: (phone number exists, unknown to the
database)
3 unknown, not known to exist: (phone number may exist)
• Single-valued ⇔ Multivalued
3 single-valued: max-card = 1 (one value for each entity, e.g., Age)
3 multivalued: max-card > 1 (a set of values for each entity, e.g. Degrees)
