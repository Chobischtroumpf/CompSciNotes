---
title: Loi uniforme continue
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - La variable aléatoire $X$ est dans l'intervalle $[a,b]$.
> - Sa [[Fonctions de probabilités#Fonction de densité (Probability Density Function - PDF)|fonction de densité]] est **constante** sur $[a,b]$ et **nulle partout ailleurs**.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/répartition} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{1}{b - a}1_{\{a \leq x \leq b\}} \\
> F_X(x) &=
> \begin{cases}
> 0, & \text{pour } x \leq a \\
> \frac{x - a}{b - a}, & \text{pour } a \leq x < b \\
> 1, & \text{pour } x \geq b
> \end{cases}
> \end{aligned}
> & [a,b] & \frac{a + b}{2} & \frac{(b - a)^2}{12} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**:
> - **Variable**:
> - **Probabilité**:
> - **Espérance**:
> - **Variance**:
