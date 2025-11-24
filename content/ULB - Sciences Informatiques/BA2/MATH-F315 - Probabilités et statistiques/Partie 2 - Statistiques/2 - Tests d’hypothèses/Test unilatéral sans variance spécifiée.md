---
title: Test unilatéral sans variance spécifiée
authors: Alessandro Dorigo
tags:
  - Stats
---


Soient $X_1, \dots, X_n$ des variables [[Indépendantes et Identiquement Distribuées#^1a45cf|i.i.d.]] suivant une loi normale $\mathcal{N}(\mu, \sigma^2)$, avec une moyenne inconnue $\mu$ et une variance $\sigma^2$ **non spécifiée**. ^393696

> [!info]+ Définition
> Le **[[Test (stats)#^4bc46e|test]] unilatéral** a pour objectif de tester les [[Hypothèse (stats)#^0a3543|hypothèses]] suivantes:
>
> $$H_0 : \mu \leq \mu_0 \quad \text{(hypothèse nulle)}$$
> contre
> $$H_1 : \mu > \mu_0 \quad \text{(hypothèse alternative)}$$
>
> **[[Statistique#^92a060|Statistique]] de test:**
> - Moyenne empirique:
>   $$\overline{X} := \frac{1}{n} \sum_{i=1}^n X_i$$
> - Version standardisée avec écart-type empirique $S$:
>   $$T := \frac{\overline{X} - \mu_0}{\frac{S}{\sqrt{n}}}$$
>   où
>   $$S^2 := \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X})^2$$
>
> **Distribution sous $H_0 : \mu = \mu_0$:**
>
> $$T \sim t_{n-1}$$
> où $t_{n-1}$ est la loi de Student avec $n-1$ degrés de liberté.

> [!tip]+ Règle de décision
> On rejette $H_0 (RH_0)$ si:
> $$T > t_{n-1; 1-\alpha}$$
> ou de manière équivalente:
> $$\overline{X} > \mu_0 + t_{n-1; 1-\alpha} \cdot \frac{S}{\sqrt{n}}$$
> où $t_{n-1; 1-\alpha}$ est le quantile d’ordre $1-\alpha$ de la loi de Student.
### Remarques:
1. Ce test est une extension du [[Test unilatéral avec variance spécifiée|test unilatéral avec variance spécifiée]], où l’incertitude sur $\sigma^2$ est prise en compte grâce à la loi de Student.
2. Pour un échantillon large ($n \geq 30$), par le [[Théorème central limite#^3800c6|théorème central-limite]], $T \sim t_{n-1}$ peut être approximé par une [[Loi normale centrale réduite#^dd4c44|loi normale standardisée]] $\mathcal{N}(0, 1)$.
