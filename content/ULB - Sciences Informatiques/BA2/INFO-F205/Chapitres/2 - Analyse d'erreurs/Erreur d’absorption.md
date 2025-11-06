---
title: Erreur d’absorption
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L’**erreur d’absorption** se produit lorsqu’on additionne **un très grand et un très petit nombre**, **effaçant** la contribution du plus petit.
>
> **Problème**: Si $d_1 \gg d_2$, alors en machine:
> $$ d_1 + d_2 \approx d_1 $$ car $d_2$ est perdu par manque de chiffres significatifs.

^218d33

> [!example]+ Exemple: Perte d'information
> Calcul de $x = d_1 + d_2$ avec:
> - $d_1 = 1.00001 \times 10^1$
> - $d_2 = 1.23456 \times 10^{-4}$
> 	- Résultat en machine: $1.00001 \times 10^1$ (les chiffres de $d_2$ sont perdus).
