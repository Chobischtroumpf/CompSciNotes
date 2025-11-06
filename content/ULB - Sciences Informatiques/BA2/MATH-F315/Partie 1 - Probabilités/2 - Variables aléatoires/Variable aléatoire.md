---
title: Variable aléatoire
authors: Alessandro Dorigo
tags:
  - VarAlea
  - Proba
---


> [!info]+ Définition
> Une **variable aléatoire** est une fonction $X$ qui associe chaque issue d'un espace de résultats à une valeur numérique.
> - $X:\Omega \rightarrow \mathbb{R}$

^dcd8d2

> [!example]+ Exemple
> On a un univers $\Omega = \{(n,m) \in \mathbb{N} \times \mathbb{N} \mid n,m \in \{1,2,3,4,5,6\} \}$ (deux dés).
>
> Une variable aléatoire $X$ possible de cet univers peut être la somme des deux dés:
> $$X:\Omega \rightarrow \mathbb{N}_0 : (n,m) \mapsto n+m$$
## Probabilités liées aux variables aléatoires

> [!abstract]- Formules
> $$ \mathbb{P}(X \in S):=\mathbb{P}(\{u \in \Omega \mid X(u) \in S\}) $$
> (pour un $S \subseteq \mathbb{R}$)
>
> $$ \mathbb{P}(X=y):=\mathbb{P}(\{u \in \Omega \mid X(u)=y\}) $$
> $$ \mathbb{P}(X \leq y):=\mathbb{P}(\{u \in \Omega \mid X(u) \leq y\}) $$
> $$ \mathbb{P}(X \geq y):=\mathbb{P}(\{u \in \Omega \mid X(u) \geq y\}) $$
> $$ \mathbb{P}(y_1 \leq X \leq y_2):= \mathbb{P}(\{u \in \Omega \mid y_1 \leq X(u) \leq y_2\}) $$
