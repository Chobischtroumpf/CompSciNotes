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
| ![[Pasted image 20251004123231.png]] | ![[Pasted image 20251004123237.png]] |
| :----------------------------------: | :----------------------------------: |
|            $\land$-règles            |            $\lor$-règles             |


> [!example] Exemples
> ![[Pasted image 20251004122636.png]]
> ![[Pasted image 20251004122806.png]]
