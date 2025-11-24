---
title: Test chi-carré d'ajustement
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Énoncé
> Le **test du chi-carré d'ajustement** permet de vérifier si les observations suivent une [[Fonctions de probabilités#Fonction de répartition (Cumulative Distribution Function - CDF)|distribution]] attendue. Il est utile pour évaluer des [[Hypothèse (stats)|hypothèses]] sur la [[Fonctions de probabilités#Fonction de répartition (Cumulative Distribution Function - CDF)|distribution]] d'une population (par exemple, vérifier si des dés sont équilibrés).
>
> On teste si les fréquences observées correspondent à des fréquences théoriques données $p_1^0, p_2^0, \dots, p_I^0$.


> [!abstract]- Test
>
> **1. Problème de test:**
> $$
> \begin{cases}
> H_0 : p_1 = p_1^0, p_2 = p_2^0, \dots, p_I = p_I^0 \quad (\text{les proportions suivent les valeurs théoriques}) \\
> H_1 : \exists i \ \text{t.q.} \ p_i \neq p_i^0 \quad \quad \quad \quad \quad \quad \quad \ (\text{au moins une proportion diffère})
> \end{cases}
> $$
>
> **2. Statistique de test:**
> $$Q^{(n)} = \sum_{i=1}^I \frac{(n_i - n p_i^0)^2}{n p_i^0}$$
>
> où $n_i$ est l’effectif observé pour la catégorie $i$ et $n p_i^0$ l’effectif théorique.
>
> **3. Règle de décision:**
> Sous $H_0$, la [[Statistique|statistique]] suit une [[Loi chi carré|loi du chi-carré]] à $I-1$ degrés de liberté:
> $$Q^{(n)} \approx \chi^2_{I-1}$$
>
> $RH_0$ au niveau $\alpha$ si:
> $$Q^{(n)} > \chi^2_{I-1; 1-\alpha}$$
