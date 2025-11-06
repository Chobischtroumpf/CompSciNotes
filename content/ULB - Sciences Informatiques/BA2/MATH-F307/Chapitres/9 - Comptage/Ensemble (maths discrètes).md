---
title: Ensemble (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Comptage
  - Maths
---


Formellement appris en `MATH-F307`. Pour les ensembles vus en algèbre linéaire, voir *link*.

> [!info]+ Définition
> Un **ensemble** est une collection non ordonnée d’éléments distincts.

^81200e

> [!example]+ Exemples
> - $\{a, b, c\} = \{c, b, a\} = \{b, c, a\}$: L'ordre des éléments n'a pas d'importance.
> - $\{a, b, a\} = \{a, b\}$: Les éléments sont distincts, donc les doublons sont ignorés.
> - $\{a, b, \{a\}\} \neq \{a, b\}$: Un ensemble peut contenir des sous-ensembles comme éléments, donc $\{a\}$ est traité comme un élément unique différent de $a$.
> - Soit $E = \{a, b\}$. L'ensemble des parties de $E$, noté $P(E)$, est:
>   $$P(E) = \{\varnothing, \{a\}, \{b\}, \{a, b\}\}$$
>   où $P(E)$ est appelé l’**ensemble des parties** ou **ensemble puissance** de $E$.
