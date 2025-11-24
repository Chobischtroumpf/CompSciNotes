---
title: Substitution rétrograde
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Définition
> La substitution rétrograde est une méthode permettant de résoudre un système linéaire triangulaire supérieur de manière séquentielle en calculant chaque inconnue à partir des inconnues déjà déterminées, en commençant par la dernière.

## Principe fondamental

Pour un système triangulaire supérieur $Ux = b$ où $U$ est une matrice triangulaire supérieure non singulière (avec $u_{ii} \neq 0$ pour tout $i$), la méthode consiste à calculer les inconnues en commençant par $x_n$ puis en descendant successivement vers $x_1$.
Et donc, pour un système triangulaire supérieur $Ux = b$ :

$$x_n = \frac{b_n}{u_{nn}}$$

$$x_i = \frac{b_i - \sum_{j=i+1}^{n} u_{ij}x_j}{u_{ii}}, \quad i = n-1, \ldots, 1$$
