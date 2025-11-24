---
title: Analyse rétrograde
authors: Alessandro Dorigo
tags:
  -
---

L'analyse rétrograde examine à quel problème modifié correspond exactement la solution approchée calculée.

> [!abstract]- Stabilité de la substitution
> Soit $A$ une matrice triangulaire non singulière. La solution approchée $\hat{x}$ du système linéaire $Ax = b$ obtenue en virgule flottante peut être considérée comme la solution exacte d'un système $(A + \delta A)x = b$ où :
> $$|\delta A| \leq \gamma_n|A| = \frac{nu}{1 - nu}|A|$$
> où $u$ est la précision machine et $n$ la taille du système.
