---
title: Résolution symbolique
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


Cette approche utilise les propriétés analytiques et mathématiques du problème pour en dériver la solution $x$.

> [!example]+ Exemple "Équation du Second Degré"
> Pour l'équation $d_1x^2 + d_2x + d_3 = 0$, où $d = [d_1, d_2, d_3]$, la solution analytique est:
> $$x = \frac{-d_2 \pm \sqrt{d_2^2 - 4d_1d_3}}{2d_1}$$

> [!example]+ Exemple "Équation Différentielle"
> Pour l'équation différentielle ordinaire du premier ordre:
> $$x' = -x, \quad x(0) = 1$$
> La solution analytique est $x(t) = e^{-t}$

> [!tip]+ Remarque
> Malheureusement, une solution analytique n'est pas toujours calculable. Par exemple, pour l'intégrale:
> $$\int_0^\pi \sqrt{1 + \cos^2(x)}dx$$
> Aucune solution analytique n'est disponible.
