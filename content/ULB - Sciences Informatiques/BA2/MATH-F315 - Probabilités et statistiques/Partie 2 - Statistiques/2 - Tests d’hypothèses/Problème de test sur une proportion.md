---
title: Problème de test sur une proportion
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un **[[Problème de test#^e7993b|problème de test]] sur une proportion** concerne l'estimation et la comparaison d'une proportion $p$ dans une population à partir d'un échantillon $\mathbf{X} = (X_1, \dots, X_n)$, où chaque $X_i$ est une variable indicatrice prenant la valeur 1 (succès) ou 0 (échec).
>
> L'objectif est de tester les hypothèses suivantes:
>
> - $H_0 : p = p_0$ (proportion égale à une valeur hypothétique $p_0$),
> - $H_1 : p \neq p_0, p > p_0$, ou $p < p_0$ (selon le type de test choisi).
>
> **Estimation et propriétés:**
>
> - La proportion observée $\hat{p}$, donnée par:
>
> $$\hat{p} := \frac{1}{n} \sum_{i=1}^n X_i$$
>
> est un [[Estimateur#^56cd5c|estimateur]] de $p$ avec les propriétés suivantes:
>
> 1. [[Estimateur sans biais#^a4d3b2|Sans biais]]: $\mathbb{E}[\hat{p}] = p$,
> 2. [[Variance#^4c0c18|Variance]]: $\text{Var}(\hat{p}) = \frac{p(1-p)}{n}$,
> 3. [[Fonctions de probabilités#Fonction de répartition (Cumulative Distribution Function - CDF)|Distribution]] exacte: $\hat{p} \sim \text{Bin}(n, p)$.

> [!tip]+ Remarque
> Pour $np(1-p) > 9$, on peut utiliser l'approximation normale suivante (dérivée du [[Théorème central limite#^3800c6|théorème central limite]]):
>
> $$\hat{p} \sim \mathcal{N}\left(p, \frac{p(1-p)}{n}\right)$$
