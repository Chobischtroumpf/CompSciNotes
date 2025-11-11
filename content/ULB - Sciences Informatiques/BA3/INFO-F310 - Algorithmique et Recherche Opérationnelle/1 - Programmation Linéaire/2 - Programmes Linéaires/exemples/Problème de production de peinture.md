---
title: Problème de production de peinture
authors: Alessandro Dorigo, iamscrambledeggs
tags:
  - Algo
  - Maths
---


> [!info] Énoncé
> Une société produit de la peinture d’intérieur et d’extérieur a partir de deux composantes de base $M_1$ et $M_2$.
>
> ![[000b468b8416918560278aee3cac5c1e.png]]
>
> - Demande maximum en peinture d’intérieur: 2 tonnes par jour
> - La production en peinture d’intérieur ne peut dépasser que d'une tonne celle en peinture d’extérieur

**var**
- var x1 >= 0 : nb de peinture d'extérieur produite/jour
- var x2 >= 0 : nb de peinture d'int produite/jour

**fonction objectif**
à optimiser (max profit) : $\max z = 5x_1 + 4x_2$

- contraintes
	- $6x_1 + 4x_2 \leq 24$
	- $x_1 + 2x_2 \leq 6$
	- $x_2 \leq 2$
	- $x_2 - x_1 \leq 1$
	- $x_1, x_2 \geq 0$
- solution admissible : $x_1 = 3, x_2 = 1 (\leftrightarrow z = 19)$
	- → trouver la solution admissible optimale
	- (infinité de solutions admissibles)
