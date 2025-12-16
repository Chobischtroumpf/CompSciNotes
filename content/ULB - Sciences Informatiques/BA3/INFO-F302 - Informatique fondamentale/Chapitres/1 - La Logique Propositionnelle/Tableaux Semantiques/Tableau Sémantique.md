---
title: Tableau Sémantique
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Le **tableau sémantique** est un algorithme pour établir la [[Satisfaisabilité]] de formules de la logique propositionnelle.

## Fonctionnement

> [!abstract]+ Construction de l'Arbre
> À partir d'une formule $\phi$, on construit un arbre $T_\phi$ dont les nœuds sont des ensembles de formules :
>
> 1. **Initialisation** : L'arbre contient uniquement $\{\phi\}$
>
> 2. **Expansion** : Tant qu'une feuille $F$ contient une formule $\psi$ simplifiable :
>    - Si $\psi$ est simplifiable par une $\land$-règle : créer un fils $F'$ en supprimant $\psi$ de $F$ et en ajoutant la ou les formules obtenues
>    - Si $\psi$ est simplifiable par une $\lor$-règle : créer deux fils $F_1$ et $F_2$, chacun obtenu en supprimant $\psi$ et en ajoutant respectivement les formules obtenues
>
> 3. **Conclusion** :
>    - Si toutes les feuilles contiennent une paire de littéraux complémentaires → non satisfaisable
>    - Sinon → satisfaisable

## Littéral

> [!note]+ Définition
> Un **littéral** est une proposition $x$ ou la négation d'une proposition $\neg x$.

## Règles de Simplification

![[Règles de Simplification#^71c7ba]]

![[Règles de Simplification#^f8ffbf]]

## Exemples

> [!example]+ Formule Satisfaisable
> Soit $\phi = (x \lor y) \land (\neg x \lor z)$
>
> **Construction du tableau** :
> ```
> {(x ∨ y) ∧ (¬x ∨ z)}
>           |
>    {x ∨ y, ¬x ∨ z}
>       /          \
>      /            \
> {x, ¬x ∨ z}  {y, ¬x ∨ z}
>    /      \       /      \
>   /        \     /        \
> {x,¬x,z} {x,z} {y,¬x,z} {y,z}
>    ✗      ✓       ✓      ✓
> ```
>
> La formule est satisfaisable (trois branches ouvertes).

> [!example]+ Formule Non Satisfaisable
> Soit $\phi = x \land \neg x$
>
> **Construction du tableau** :
> ```
> {x ∧ ¬x}
>     |
>  {x, ¬x}
>     ✗
> ```
>
> La formule n'est pas satisfaisable (toutes les branches fermées).

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Satisfaisabilité]]** : Propriété testée par l'algorithme
> - **[[Règles de Simplification]]** : Détail des règles $\land$ et $\lor$
> - **[[Problème SAT]]** : Application à grande échelle
> - **[[Sémantique]]** : Base théorique de l'algorithme
