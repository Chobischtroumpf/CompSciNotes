---
title: Loi exponentielle
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On mesure le **temps d'attente** jusqu'à la première occurrence d'un événement dans un **[[Loi de Poisson|processus de Poisson]]**.
> - Les événements sont **indépendants** et se produisent à un **taux constant** $\lambda$.
> - $\lambda$ est le **taux d'occurrence** moyen des événements par unité de temps. Plus $\lambda$ est grand, plus les événements sont fréquents.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/répartition} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \lambda e^{-\lambda x} \\
> F_X(x) &= 1 - e^{-\lambda x}
> \end{aligned}
> & \mathbb{R}^+ & \frac{1}{\lambda} & \frac{1}{\lambda^2} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: Supposons qu'on modélise l'arrivée des bus à un arrêt, où l'intervalle de temps entre deux arrivées successives suit une loi exponentielle avec un taux de $\lambda = 2$ arrivées par heure.
> - **Variable**: Soit $X$ le temps d’attente jusqu’à l'arrivée du prochain bus.
> - **Probabilité**: La probabilité que le bus arrive après **plus de 30 minutes** (soit $X > 0.5$ heure) est donnée par:
> $$\mathbb{P}(X > 0.5) = e^{-\lambda \cdot 0.5} = e^{-2 \cdot 0.5} = e^{-1} \approx 0.3679$$
> - **Espérance**: Le temps d’attente moyen avant l'arrivée du bus est:
> $$\mathbb{E}[X] = \frac{1}{\lambda} = \frac{1}{2} = 0.5 \text{ heure} (30 \text{ minutes})$$
> - **Variance**: La variance du temps d’attente est:
> $$\text{Var}(X) = \frac{1}{\lambda^2} = \frac{1}{4} = 0.25 \text{ heure}^2$$

> [!abstract]- Proposition
> La loi exponentielle est le pendant continu de la [[Loi géométrique|loi géométrique]]. Les deux lois partagent la propriété de la perte de mémoire:
> $$\mathbb{P}(X > a + b | X > a) = \mathbb{P}(X > b)$$
>
> **Démonstration:**
> $$\begin{align*}
> \mathbb{P}(X > a + b | X > a) &= \frac{\mathbb{P}(X > a + b, X > a)}{\mathbb{P}(X > a)} = \frac{\mathbb{P}(X > a + b)}{\mathbb{P}(X > a)} \\
> &= \frac{\int_{a + b}^{\infty} \lambda \cdot e^{-\lambda x} dx}{\int_{a}^{\infty} \lambda \cdot e^{-\lambda x} dx} = \frac{e^{-\lambda (a + b)}}{e^{-\lambda a}} = e^{-\lambda \cdot b} \\
> &= \mathbb{P}(X > b).
> \end{align*}$$

^373ea8

> [!abstract]- Corollaires
> 1. Le temps d’attente entre deux arrivées suivra la même loi exponentielle;
> 2. Le temps d’attente jusqu’à l’arrivée suivante à partir d’un moment quelconque suivra la même loi exponentielle.
