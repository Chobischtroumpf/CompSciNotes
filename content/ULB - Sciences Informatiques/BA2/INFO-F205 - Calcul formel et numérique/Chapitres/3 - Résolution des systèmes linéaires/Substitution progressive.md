---
title: Substitution progressive
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> La substitution progressive (ou directe) est une méthode permettant de résoudre un système linéaire triangulaire inférieur de manière séquentielle en calculant chaque inconnue à partir des inconnues déjà déterminées.

### Principe fondamental

Pour un système triangulaire inférieur $Lx=b$ où $L$ est une matrice triangulaire inférieure non singulière (avec $l_{ii} \neq 0$ pour tout $i$), la méthode consiste à calculer les inconnues en commençant par $x_1$ puis en remontant successivement vers $x_n$​.
Autrement dit :
$$x_1 = \frac{b_1}{l_{11}}$$
$$x_i = \frac{b_i - \sum_{j=1}^{i-1} l_{ij}x_j}{l_{ii}}, \quad i = 2, \ldots, n$$
