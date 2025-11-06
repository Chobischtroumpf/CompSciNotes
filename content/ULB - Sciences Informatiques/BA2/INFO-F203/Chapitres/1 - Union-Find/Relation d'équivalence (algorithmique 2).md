---
title: Relation d'équivalence (algorithmique 2)
authors: Alessandro Dorigo
tags:
  - Algo
---


Formellement appris en `INFO-F203`. Pour la definition détaillée d'une relation d'equivalence, voir [[Relation d’équivalence|relation d'equivalence]].

> [!tip]+ Remarque
> La classe d'équivalence d'un élément $x$ est l'ensemble des éléments $y$ tels que $x \equiv y$
### Structure
- Ensemble d'éléments pouvant être connectés deux à deux
- La relation d'équivalence est la connexité
- Deux éléments font partie de la même classe s'il existe un chemin entre eux
### Opérations fondamentales
1. Ajouter une connexion entre deux éléments donnés
2. Décider si deux éléments appartiennent à la même classe
