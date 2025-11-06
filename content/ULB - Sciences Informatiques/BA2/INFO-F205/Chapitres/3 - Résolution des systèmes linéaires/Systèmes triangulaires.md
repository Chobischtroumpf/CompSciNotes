---
title: Systèmes triangulaires
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> La matrice des coefficients $A$ est dite triangulaire supérieure si $a_{ij} = 0, \forall i,j : 1 \leq j < i \leq n$.
>
> La matrice des coefficients $A$ est triangulaire inférieure si $a_{ij} = 0, \forall i,j : 1 \leq i < j \leq n$.

![[Substitution progressive]]

![[Substitution rétrograde]]

> [!abstract]- Formule "Coût computationnel"
> La résolution d'un système triangulaire demande :
> - $n$ divisions
> - $\frac{n(n-1)}{2}$ multiplications
> - $\frac{n(n-1)}{2}$ additions (ou soustractions)
>
> Au total, l'algorithme nécessite $n^2$ opérations en virgule flottante (flops).
