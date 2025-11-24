---
title: Tableau sémantique
authors: Alessandro Dorigo
tags:
  - InfoFond
---


> [!info] Définition
> Algorithme pour établir la [[Satisfaisabilité|satisfaisabilité]] de formules de la logique propositionnelle.
>
> **Fonctionnement**:
> - A partir d'une formule $\phi$, on construit un arbre $T_\phi$ dont les nœuds sont des ensembles de formules:
> 1. Au départ, l'arbre contient que $\{ \phi \}$
> 2. Tant qu'une feuille $F$ contient une formule $\psi$ qui est simplifiable
> 	1. si $\phi$ est simplifiable par une $\land$-règle, alors on crée un fils $F^{'}$ à $F$ où $F^{'}$ est obtenu supprimant $\phi$ de $F$ et en ajoutant la formule (dans le cas d’une double négation) ou les deux formules (pour les autres cas) obtenues par la simplification, à l’ensemble $F^{'}$
> 	2. si est $\phi$ simplifiable par une $\lor$-règle, alors on crée deux fils $F_1$ et $F_2$, chacun étant obtenu en supprimant $\phi$ de $F$ et en ajoutant respectivement les formules obtenues par la simplification
> 3. Si toutes les feuilles de l'arbre contiennent une paire de littéraux complémentaires, alors non-satisfaisable, sinon satisfaisable

> [!info] Littéral
> Une proposition $x$ ou la négation d'une proposition $\neg x$.

^7b1f83

> [!tip] Règles de simplification
>
| ![[d697d180188f31027657045fcbb4416c.png]] | ![[8b8903efd411fd36fda6b9577aa5dfc4.png]] |
| :----------------------------------: | :----------------------------------: |
|            $\land$-règles            |            $\lor$-règles             |


> [!example] Exemples
> ![[ad2deb914f3dc58543d764cf2a478cce.png]]
> ![[b1d1fa5852ef24fc1dc5a4ab3f895dd6.png]]
