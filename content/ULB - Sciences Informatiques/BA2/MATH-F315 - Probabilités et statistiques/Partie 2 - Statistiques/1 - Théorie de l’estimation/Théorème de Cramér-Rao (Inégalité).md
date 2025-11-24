---
title: Théorème de Cramér-Rao (Inégalité)
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!abstract]- Théorème de Cramér-Rao
> Le **théorème de Cramér-Rao** établit une borne inférieure pour la [[Variance#^4c0c18|variance]] de tout [[Estimateur sans biais#^a4d3b2|estimateur sans biais]] $\hat{\theta}$ du paramètre $\theta$. Il s'énonce ainsi:
>
> - Sous certaines [[Vraisemblance#^2d4e46|conditions de régularité]], la [[Variance#^4c0c18|variance]] de $\hat{\theta}$ satisfait:
>
> $$\text{Var}_\theta(\hat{\theta}) \geq \frac{1}{\mathcal{I}(\theta)}$$
> où $\mathcal{I}(\theta)$ est l'[[Information de Fisher#^c6b970|information de Fisher]].

^767ee4

- Un estimateur atteint cette borne s'il est **[[Estimateur efficace#^2d1207|efficace]]**, c'est-à-dire qu'il utilise au mieux l'information contenue dans les données.

> [!abstract]- Preuve
> ![[52433998817e9cf0508e898f21fd48ac.png]]
