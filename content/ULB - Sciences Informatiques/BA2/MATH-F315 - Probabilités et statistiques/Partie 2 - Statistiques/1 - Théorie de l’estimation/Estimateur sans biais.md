---
title: Estimateur sans biais
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un [[Estimateur#^56cd5c|estimateur]] $\hat{\theta}$ est dit **sans [[Biais#^74266c|biais]]** si:
>
> $$\mathbb{E}_\theta[\hat{\theta}] = \theta, \quad \forall \theta \in \Theta$$
>
> *Cela signifie que, en moyenne, l'estimateur fournit la valeur exacte du paramètre.*

^a4d3b2

> [!tip]+ Remarque
> Pour que cette définition soit valide, il est nécessaire que:
> 1. $\mathbb{E}_\theta[\hat{\theta}]$ existe et que
> 2. $\mathbb{E}_\theta[\hat{\theta}]$ soit fini.

> [!example]+ Exemples
> ![[4f2006d2edeba103f70d0649de132aa0.png]]
> ![[fd877581d7033f5dc9c1a3797d8e2f8b.png]]
> ![[89cdee55292897f8f2e1d83a4e00dbe0.png]]
