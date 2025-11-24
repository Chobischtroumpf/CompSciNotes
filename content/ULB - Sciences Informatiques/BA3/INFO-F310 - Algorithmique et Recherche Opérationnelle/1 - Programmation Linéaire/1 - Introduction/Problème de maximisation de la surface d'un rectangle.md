---
title: Problème de maximisation de la surface d'un rectangle
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Énoncé
> Supposons que l'on veut plier un fil de fer de longueur $L$ en rectangle de manière a maximiser la surface $A$ du rectangle:
> $$A = \ell \times w$$
> $$\ell + w = \frac{L}{2}$$
>
> ![[37212db4d1e7222790cb3cb106027bab.png]]

## Solutions
1) Méthode analytique: $$A = (\frac{L}{2} - w) w = \frac{1}{2} Lw - w^2 = \frac{dA}{dw} = \frac{L}{2} - 2w = 0$$
   On a donc $w = \ell = \frac{L}{4}$
2) Déplacement de solution en solution pour atteindre
	1) l'optimum (méthode exacte)
	2) une solution admissible dans le voisinage d'un optimum (approximations)
	3) une "bonne" solution en un temps raisonnable (heuristiques)
