---
title: Régression
authors: Alessandro Dorigo
tags:
  - Stats
---


Avec un échantillon $(X_1, Y_1), \dots, (X_n, Y_n)$ associé a deux variables aléatoires, le **modèle de régression linéaire simple** postule un lien linéaire entre les $Y_i$ et les $X_i$ de la forme

$$Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i \quad \quad i = 1, \dots, n$$

où

- $(i) \ \boldsymbol{\beta} = \begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix} \in \mathbb{R}^2$ est un paramètre (inconnu): le *paramètre de régression*, composé d’une *pente* $\beta_1$ et d’une ordonnée à l’origine $\beta_0$.
- $(ii) \ \varepsilon_1, \ldots, \varepsilon_n$ sont des variables aléatoires non observées.

Dans le cas dit "général", les hypothèses traditionnellement faites sur les erreurs sont que $\mathbb{E}[\varepsilon_i] = 0 \quad \forall i$ et

$$\mathbb{E}[\varepsilon_i \varepsilon_j] = \begin{cases} \sigma^2: i = j \\ 0 \ \ : i \neq j \end{cases}$$
