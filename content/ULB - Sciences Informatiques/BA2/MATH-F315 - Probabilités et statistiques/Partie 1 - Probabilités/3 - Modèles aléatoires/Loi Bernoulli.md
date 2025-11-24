---
title: Loi Bernoulli
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On réalise un **seul essai** (une expérience unique).
> - La variable aléatoire $X$ peut prendre deux valeurs: 1 pour un succès et 0 pour un échec.
> - $p$ est la probabilité de succès, avec $0 \leq p \leq 1$.

^2cc447

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = 1) = p, \mathbb{P}(X = 0) = 1 - p & \{0,1\} & p & p(1 - p) \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: On lance une pièce de monnaie une seule fois.
> - **Variable**: Soit $X = 1$ si le résultat est "pile" et $X = 0$ si c'est "face".
> - **Probabilité**: Si la pièce est équilibrée, $p = 0.5$ (50% de chance pour pile ou face).
> - **Espérance**: La valeur moyenne attendue est $\mathbb{E}[X] = 0.5$.
> - **Variance**: La dispersion autour de la moyenne est $\text{Var}(X) = 0.25$.
