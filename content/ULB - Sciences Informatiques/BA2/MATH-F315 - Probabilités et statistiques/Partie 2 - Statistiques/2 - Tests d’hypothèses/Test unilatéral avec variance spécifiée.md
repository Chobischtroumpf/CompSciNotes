---
title: Test unilatéral avec variance spécifiée
authors: Alessandro Dorigo
tags:
  - Stats
---


Soient $X_1, \dots, X_n$ des variables [[Indépendantes et Identiquement Distribuées#^1a45cf|i.i.d.]] suivant une loi normale $\mathcal{N}(\mu, \sigma^2)$, avec une variance $\sigma^2$ spécifiée. ^280dee

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
> - Version normalisée (variable standardisée):
>   $$Z := \frac{\overline{X} - \mu_0}{\frac{\sigma}{\sqrt{n}}}$$
>
> Distribution sous $H_0 : \mu = \mu_0$:
> $$\overline{X} \sim \mathcal{N}(\mu_0, \frac{\sigma^2}{n}) \quad \Longrightarrow \quad Z \sim \mathcal{N}(0, 1)$$

^5d0ddd

> [!tip]+ Règle de décision
> On rejette $H_0(RH_0)$ si:
>
> $$Z > z_{1-\alpha}$$
> ou de manière équivalente:
> $$\overline{X} > \mu_0 + z_{1-\alpha} \cdot \frac{\sigma}{\sqrt{n}}$$
> où $z_{1-\alpha}$ est le quantile d’ordre $1 - \alpha$ de la [[Loi normale centrale réduite#^dd4c44|loi normale centrée réduite]].

La règle de décision signifie que l’on **rejette $H_0$** si la moyenne empirique $\overline{X}$ est "trop grande" par rapport à $\mu_0$. Ce seuil critique est déterminé par le **niveau de significativité** $\alpha$, à travers le quantile $z_{1-\alpha}$.
