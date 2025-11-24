---
title: Identifier
authors: Alessandro Dorigo
tags:
  - Databases
---


![[f5140e5c558f1001f5b58132adbdbb78.png]]

• Identifier or key of entity type E: attribute or set of attributes of E whose
values uniquely determine an entity of E
• Alternative notations: underlined attributes or in a constraint box
• Attributes involved in an identifier must be of cardinality (1,1)
• Two facets
3 unique identification: an identifier value selects at most one entity
3 unicity constraint: no two entities of the same type with the same value
for an identifier
• Identifier definition belongs to the schema

![[099a146f007a209d4c964acc33bd426e.png]]

• Some entity types have more than one identifier
• Notation: Only one of them can be represented using the “underlined” nota-
tion, the others must be represented in the constraint box
• An identifier with several attributes can be made a composite attribute
