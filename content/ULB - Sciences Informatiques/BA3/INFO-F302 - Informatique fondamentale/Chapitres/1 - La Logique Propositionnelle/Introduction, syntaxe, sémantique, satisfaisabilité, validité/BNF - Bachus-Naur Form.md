---
title: BNF - Bachus-Naur Form
authors: Alessandro Dorigo
tags:
  - InfoFond
---


Avec le vocabulaire du langage de la logique propositionnelle étant composé:
- D'un ensemble (fini) de propositions $x, y, z, \dots$ noté $X, Y, \dots$
- De deux constantes: vrai ($\top$) et faux ($\bot$)
- D'un ensemble de [[Logique|connecteurs logiques]]
- Des parenthèses: $(,)$

> [!info] Definition
> Soit $X$ un ensemble de propositions. Les formules de la logique propositionnelle respecent la regle de formation BNF:
>
> $$\phi ::= \top \mid \bot \mid x \mid \phi_1 \land \phi_2 \mid \phi_1 \vee \phi_2 \mid \phi_1 \rightarrow \phi_2 \mid \phi_1 \leftrightarrow \phi_2 \mid \neg \phi_1 \mid (\phi_1)$$
>
> Ou $\phi_1$, $\phi_2$ sont des formules propositionnelles bien formées (respectent les règles syntaxiques de la logique propositionnelle)
