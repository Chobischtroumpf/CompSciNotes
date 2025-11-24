---
title: Stabilité
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Un algorithme numérique est dit **stable** (ou bien posé) si:
> 1. Il existe pour tout $n$ une solution unique $x^{(n)}$
> 2. Pour chaque $\epsilon > 0$ il existe un $\eta > 0$ et un $n_0$ tel que pour tout $n > n_0$:
> $$\|\delta d^{(i)}\| \leq \eta \text{ pour tout } i = 1,...,m \Rightarrow \|\bar{x}^{(n)} - x^{(n)}\| \leq \epsilon$$

^f6ba30

> [!example]+ Exemple
> ![[05708f38fe733518422e4cd9d330771c.png]]
> ![[69085e4e36361ab7f82d29dbfa92058a.png]]
