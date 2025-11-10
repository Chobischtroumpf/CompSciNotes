---
title: Information de Fisher
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> L'**information de Fisher**, notée $\mathcal{I}(\theta)$, est une mesure de la quantité d'information que les données $\mathbf{X}$ fournissent sur le paramètre $\theta$. Elle est définie comme:
>
> $$\mathcal{I}(\theta) = \int \left( \frac{\partial}{\partial \theta} \log L_\theta(x) \right)^2 L_\theta(x) \ dx$$
>
> où $L_\theta(x)$ est la fonction de [[Vraisemblance#^121cc0|vraisemblance]]. Cette quantité est aussi égale à la variance de la dérivée du logarithme de la [[Vraisemblance#^121cc0|vraisemblance]]:
>
> $$\mathcal{I}(\theta) = \text{Var}_\theta \left( \frac{\partial}{\partial \theta} \log L_\theta(\mathbf{X}) \right)$$

^c6b970
