---
title: Test bilatéral sur une proportion
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> On teste
> $$H_0 : p \leq p_0$$
> contre
> $$H_1 : p > p_0$$

> [!abstract]- Statistique de test
> $$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$
> Sous $Z \approx \mathcal{N}(0, 1)$.
>
> Loi sous $H_0 : p = p_0$:
> $$\hat{p} \approx \mathcal{N}\left(p_0, \frac{p_0(1-p_0)}{n}\right) \quad \text{ ou } \quad Z \approx \mathcal{N}(0,1)$$

> [!tip]+ Règle de décision
> On rejette $H_0(RH_0)$ si:
>
> $$Z > z_{1-\alpha}$$
> ou de manière équivalente:
> $$\hat{p} > p_0 + z_{1-\alpha} \sqrt{\frac{p_0(1-p_0)}{n}}$$
> où $z_{1-\alpha}$ est le quantile d’ordre $1 - \alpha$ de la [[Loi normale centrale réduite#^dd4c44|loi normale centrée réduite]].
