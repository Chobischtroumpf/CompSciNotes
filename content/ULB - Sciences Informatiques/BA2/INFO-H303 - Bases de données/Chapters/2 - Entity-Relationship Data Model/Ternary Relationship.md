---
title: Ternary Relationship
authors: Alessandro Dorigo
tags:
  - Databases
---


Ternary Relationship Example
![[a8a221baf452ea5857e51d943f66be1a.png]]
![[4111791ae697804773ecfb2b3b6af5ec.png]]
![[2ee3fec940af9ae803ee7c8c2390fb4a.png]]

• The 3 binary relationships have the same number of instances as the ternary relation-
ship (5)
• The binary relationships are derived by “projection” from the ternary relationship ⇒
there is certainly no more information in the 3 binary relationships than in the ternary
relationship
• What about the reverse? Is there more information in the ternary relationship than
in the 3 binary relationships?

• There is less information in the 3 binary relationships derived form a ternary
relationship than in the ternary relationship
![[eda84f64b958f39af00188ed0f340286.png]]
• There is no way to tell from the binary relationships that supplier Dupont does
not supply pen to Client1

Correct modeling:
![[dafd346d2dbe4caf18355a9d4aae2268.png]]

• How to correctly do without n-ary relationships:
3 “objectify” or “reify” the n-ary relationship into a weak entity type (whose
identifier is composite and made of the identifiers of the n participating entities,
see later), and
3 link the the new entity type to each original entity type with a binary relationship
• In the example above, the new entity type could model orders, invoices, ..., according
to the semantics of the original Supply relationship
• Advantage of using binary relationships only: the data model is simpler
• Advantage of using n-ary relationships:
3 they may express the most natural model (if the underlying reality is naturally
perceived as an n-ary association)
3 the “objectified relationship” and the accompanying binary relationships may or
may not be natural in the perception of the application domain
3 schemas with only binary relationships are typically larger: they have more entity
types and more relationships than the equivalent schemas with n-ary relationships
• Summary: doing away with n-ary relationship yields a simpler data model (binary
relationships only) at the expense of larger schemas and possibly less natural models
• Both views (an n-ary relationship and its “objectified” entity type) could coexist in
a rich and redundant data model (this may be natural, as both perceptions may be
reasonable in the underlying reality)
• Further discussion: what about the cardinalities of binary relationship obtained by
projection, by reification?
