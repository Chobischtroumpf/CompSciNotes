---
title: Écart quadratique moyen
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> L'**écart quadratique moyen ($\text{EQM}$)** de l'estimateur $\hat{\theta}$ par rapport au paramètre $\theta$ est défini par:
>
> $$\text{EQM}_\theta(\hat{\theta}) = \mathbb{E}_\theta[(\hat{\theta} - \theta)^2]$$
>
> Il mesure l'erreur moyenne quadratique entre $\hat{\theta}$ et $\theta$.
>
> - L'$\text{EQM}$ n'existe que si l'estimateur $\hat{\theta}$ est **carré intégrable**, c'est-à-dire:
> $$\mathbb{E}_\theta[\hat{\theta}^2] < \infty$$

^091951

> [!tip]+ Remarque
> Un [[Estimateur#^56cd5c|estimateur]] $\hat{\theta}_1$ est considéré comme "meilleur" qu'un autre [[Estimateur#^56cd5c|estimateur]] $\hat{\theta}_2$ si, pour tout $\theta \in \Theta$, on a:
>
> $$\mathbb{E}_\theta[(\hat{\theta}_1 - \theta)^2] \leq \mathbb{E}_\theta[(\hat{\theta}_2 - \theta)^2]$$

> [!abstract]- Preuve de $\text{EQM}_\theta(\hat{\theta})$
> ![[Pasted image 20241119161553.png]]
> ![[Pasted image 20241119161619.png]]
>
> L’écart quadratique moyen est donc la [[Variance#^4c0c18|variance]] augmentée du carré du [[Biais#^74266c|biais]].

> [!example]+ Exemple
> ![[Pasted image 20241119161711.png]]
> - **À gauche**: Un estimateur sans biais ($\text{Biais} = 0$) mais avec une grande dispersion (variance élevée).
> - **À droite**: Un estimateur biaisé mais avec une faible dispersion.
>
> **Conclusion**: Il est généralement préférable d'avoir un estimateur avec **biais nul et dispersion minimale**, plutôt qu'un estimateur biaisé, même avec une faible variance.
