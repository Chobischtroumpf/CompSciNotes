---
title: Congestion
authors: Alessandro Dorigo
tags:
  - MathDis
  - Network
---


> [!info]+ Définition ([[Problème de routage#^fe8a80|problème de routage]])
> La congestion d'une solution du [[Problème de routage#^fe8a80|problème de routage]] est définie comme le nombre maximal de [[Chemin#^377ffc|chemins]] $P^\pi_k$ passant par un même commutateur.
>
> Autrement dit, c'est le plus grand nombre de fois qu'un commutateur est utilisé par les différents chemins.

^4df71b

> [!info]+ Définition ([[Réseaux de communication#^026870|réseau]])
> La **congestion** d'un [[Réseaux de communication#^026870|réseau]] $N \times N$ est le nombre maximum de chemins de données passant par un même commutateur, dans le pire des cas parmi les meilleurs cas possibles de routage.
>
> ![[8bdd0eadd72511e15d48130556e284ce.png]]

^5c306c

> [!tip]+ Remarque
> La congestion d’un réseau $N \times N$ est toujours $\leq N$, car on a au plus $N$ chemins dans chaque solution.

> [!example]+ Exemples
> ![[21a603965e3bbc13daef98e18aee5eb2.png]]
> ![[901791d2b083e243b5d9031f2757d1e8.png]]
