---
title: Intervalle de confiance pour une proportion
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!abstract]- Énoncé
> Soient $X_1, \dots, X_n$ [[Indépendantes et Identiquement Distribuées#^1a45cf|i.i.d.]] $\text{Bin}(1,p), p \in (0,1)$. On a que pour $\hat{p} = \overline{X}^{(n)}$ que:
>
> $$\mathbb{E}[\overline{X}^{(n)}] = p \quad \quad \quad \text{Var}[\overline{X}^{(n)}] = \frac{p(1-p)}{n}$$
>
> On sait grâce au [[Théorème central limite#^3800c6|TCL]] que $\frac{\overline{X}^{(n)} - p}{\sqrt{\frac{p(1-p)}{n}}} \to \mathcal{N}(0,1)$. On a donc que:
>
> $$ \mathbb{P}_p \left[ z_{\alpha/2} \leq \frac{\hat{p} - p}{\sqrt{\frac{p(1-p)}{n}}} \leq z_{1-\alpha/2} \right] \simeq 1 - \alpha \quad \forall p \in (0,1) $$

> [!tip]+ Remarque
> Pour $n$ “grand” ($np(1 − p) > 9$), la construction d’un [[Intervalle de confiance#^5071ba|intervalle de confiance]] peut être fondée sur la [[Loi normale|loi normale]] approchée de $\hat{p}$:
>
> $$ \mathbb{P}_p \left[
> \hat{p} - z_{1-\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
> \leq p
> \leq \hat{p} + z_{1-\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
> \right] \simeq 1 - \alpha \quad \forall p \in (0,1) $$
>
> Pour $n$ “petit”, cette construction doit être fondée sur la [[Loi binomiale|loi binomiale]] exacte de $n\hat{p}$; les intervalles recherchés s’obtiennent par lecture de tables et d’abaques.
