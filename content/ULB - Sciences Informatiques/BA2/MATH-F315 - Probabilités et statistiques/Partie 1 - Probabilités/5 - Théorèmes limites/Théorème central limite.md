---
title: Théorème central limite
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


Matière non comprise a l'examen!!!

> [!info]+ Définition
> Soient $X_1, X_2, \dots, X_n$ des **observations [[Indépendantes et Identiquement Distribuées#^1a45cf|indépendantes et identiquement distribuées (i.i.d.)]]**, avec une [[Espérance (expected value)#^c716f7|espérance]] $\mu_X = \mathbb{E}(X)$ et une [[Variance#^4c0c18|variance]] $\sigma_X^2$ bien définies et finies.
>
> La **somme** des [[Variable aléatoire#^dcd8d2|variables aléatoires]] $S_n = \sum_{k=1}^n X_k$ peut être transformée en une nouvelle variable standardisée $Z_n$, donnée par:
> $$Z_n = \frac{S_n - n\mu_X}{\sigma_X \sqrt{n}} = \frac{\overline{X_n} - \mu_X}{\sigma_X / \sqrt{n}}$$
> où $\overline{X_n} = \frac{S_n}{n}$ est la [[Moyenne (sample mean)#^5d95b9|moyenne empirique]] des observations.
>
> Alors, selon le **Théorème Central Limite**, lorsque $n$ devient très grand ($n \to \infty$), la distribution de $Z_n$ converge vers une **loi normale centrée réduite**:
> $$\lim_{n \to \infty} F_{Z_n}(z) = \Phi(z)$$
> où $\Phi(z)$ est la fonction de répartition de la loi normale centrée réduite $\mathcal{N}(0, 1)$.

^3800c6
