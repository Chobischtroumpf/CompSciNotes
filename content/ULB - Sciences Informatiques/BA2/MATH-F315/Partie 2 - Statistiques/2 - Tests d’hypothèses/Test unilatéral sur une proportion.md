---
title: Test unilatéral sur une proportion
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> On teste
> $$H_0 : p = p_0$$
> contre
> $$H_1 : p \neq p_0$$

> [!abstract]- Statistique de test
> $$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$
> Sous $Z \approx \mathcal{N}(0, 1)$.
>
> Loi sous $H_0 : p = p_0$:
> $$\hat{p} \approx \mathcal{N}\left(p_0, \frac{p_0(1-p_0)}{n}\right) \quad \text{ ou } \quad Z \approx \mathcal{N}(0,1)$$

> [!tip]+ Règle de décision
> On rejette $H_0(RH_0)$ si:
>
> $$Z \notin [\pm z_{1 - \alpha / 2}]$$
> ou de manière équivalente:
> $$\hat{p} \notin \left[ p_0 \pm z_{1 - \alpha / 2} \sqrt{\frac{p_0(1-p_0)}{n}} \right]$$
