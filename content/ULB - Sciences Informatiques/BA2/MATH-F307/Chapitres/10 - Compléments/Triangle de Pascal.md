---
title: Triangle de Pascal
authors: Alessandro Dorigo
tags:
  - MathDis
  - Complements
---


Definition?

On peut l’étendre à tout le demi-plan $n \geq 0$ en mettant des zéros:

$$\binom{n}{k} = \begin{cases} 0 & k < 0 \\ 0 & k > n \end{cases}$$

Remarque: On peut l’étendre à tout le plan (y compris $n < 0$) en gardant vraies les équations

$$ \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k} \quad \text{et} \quad \binom{n}{k} = \binom{n}{n-k}$$

Le triangle de Pascal modulo 2 s'appelle le Triangle de Sierpiński
![[Pasted image 20241212101356.png]]

> [!abstract]- Théorème 10.1.1 (formule de somme parallèle):
> Si $m \geq k$:
> $$\sum_{n=k}^{m} \binom{n}{k} = \binom{k}{k} + \binom{k+1}{k} + \cdots + \binom{m}{k} = \binom{m+1}{k+1}$$
>
> ![[Pasted image 20241212101625.png]]
>
> Ça nous permet de calculer la somme des $m − k + 1$ premiers coefficients d’une diagonale du triangle de Pascal.
>
> ![[Pasted image 20241212101722.png]]
