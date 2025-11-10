---
title: Tours de Hanoï
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
  - Algo
---


Le problème des tours de Hanoï consiste à déplacer des disques de tailles différentes d’une colonne de départ vers une colonne d’arrivée.
- **Paramètre**: $n$ disques de tailles différentes.
- **Règle**: Tout disque doit reposer soit sur le plateau, soit sur un disque plus grand.
- **But**: Transférer tous les disques en colonne 2 (destination) en respectant les règles.
> [!info]+ Définition
> Soit $T(n)$ le nombre minimum de mouvements nécessaires pour déplacer $n$ disques en suivant les règles du problème.

> [!example]+ Exemples
>
> ![[8452b058e671969feee43e6bdd32208b.png]]
> 	![[4b792552cdffacf58af087d19adbf0c8.png]]
### Observation cruciale
Pour résoudre le problème, on observe la relation de récurrence suivante:
$$\begin{cases}
T(0) = 0 \\
T(n + 1) = T(n) + 1 + T(n)= 2T(n) + 1 \quad \forall n \geq 0
\end{cases}$$
> [!abstract]- Théorème 7.0.1
> Pour tout $n \in \mathbb{N}$, on a:
> $$T(n) = 2^n - 1$$
> ![[ff0fdead1512b0457d66435d6fefcc09.png]]
