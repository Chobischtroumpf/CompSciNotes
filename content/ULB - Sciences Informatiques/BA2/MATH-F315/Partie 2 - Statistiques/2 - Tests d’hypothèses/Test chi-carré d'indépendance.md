---
title: Test chi-carré d'indépendance
authors: Alessandro Dorigo
tags:
  - Stats
---

> [!info]+ Énoncé
> Le **test du chi-carré d’indépendance** évalue si deux [[Variable aléatoire#^dcd8d2|variables aléatoires]] discrètes $X$ et $Y$ sont indépendantes. Il repose sur un échantillon bivarié de $n$ observations.

> [!abstract]- Test
>
> **1. Problème de test:**
> $$
> \begin{cases}
> H_0 : p_{ij} = p_{i.} p_{.j} \quad \forall i, j \quad (\text{indépendance entre} \ X \ \text{et} \ Y) \\
> H_1 : \exists i, j \ \text{t.q.} \ p_{ij} \neq p_{i.} p_{.j}.
> \end{cases}
> $$
>
> où:
> - $p_{i.} = \sum_{j=1}^J p_{ij}$ (probabilité marginale de $X$),
> - $p_{.j} = \sum_{i=1}^I p_{ij}$ (probabilité marginale de $Y$).
>
> **2. Statistique de test:**
> $$Q^{(n)} = \sum_{i=1}^I \sum_{j=1}^J \frac{\left(n_{ij} - \frac{n_{i.} n_{.j}}{n}\right)^2}{\frac{n_{i.} n_{.j}}{n}}$$
>
> où:
> - $n_{ij}$: effectif observé pour la catégorie $(i, j)$,
> - $n_{i.} = \sum_{j=1}^J n_{ij}$: effectif marginal de $X$,
> - $n_{.j} = \sum_{i=1}^I n_{ij}$: effectif marginal de $Y$.
>
> **3. Règle de décision:**
> Sous $H_0$, la statistique suit une [[Loi chi carré|loi du chi-carré]] à $(I-1)(J-1)$ degrés de liberté:
>
> $$Q^{(n)} \approx \chi^2_{(I-1)(J-1)}$$
>
> $RH_0$ au niveau $\alpha$ si:
> $$Q^{(n)} > \chi^2_{(I-1)(J-1); 1-\alpha}$$
