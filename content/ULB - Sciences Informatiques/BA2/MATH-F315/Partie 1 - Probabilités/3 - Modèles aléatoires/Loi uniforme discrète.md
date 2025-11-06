---
title: Loi uniforme discrète
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - La variable aléatoire $X$ prend une valeur quelconque dans l'ensemble $\{a, a + 1, \dots, b\}$, où $b \geq a$ et $a, b \in \mathbb{Z}$.
> - Chaque valeur de l'ensemble a une **probabilité égale** d'être choisie.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = i) = \frac{1}{b - a + 1} & \{b,b + 1, \dots, a\} & \frac{b + a}{2} & \frac{(b - a + 1)^2 - 1}{12} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: Supposons qu'on veuille modéliser un tirage au sort où chaque nombre entier entre 1 et 10 a la même chance d'être tiré.
> - **Variable**: Soit $X$ la variable aléatoire qui représente le numéro tiré. $X$ suit une **loi uniforme discrète** avec $a = 1$ et $b = 10$.
> - **Probabilité**: La probabilité de tirer n'importe quel nombre entre 1 et 10 est égale à:
> $$\mathbb{P}(X = i) = \frac{1}{10}, \quad i \in \{1, 2, \dots, 10\}$$
> Chaque numéro a donc une probabilité de $0.1$ d'être tiré.
> - **Espérance**: La valeur moyenne attendue (l'espérance) est:
> $$\mathbb{E}[X] = \frac{1 + 10}{2} = 5.5$$
> Cela signifie que la moyenne des numéros tirés se situera autour de **5.5**.
> - **Variance**: La variance, qui mesure la dispersion autour de la moyenne, est:
> $$\text{Var}(X) = \frac{(10 - 1)(10 - 1 + 2)}{12} = 8.25$$
