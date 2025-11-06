---
title: Loi géométrique
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On compte le **nombre d'essais** avant d'obtenir le **premier succès** dans des répétitions **indépendantes**.
> - $p$ est la probabilité de succès à chaque essai.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = k) = (1 - p)^{k - 1}p & \mathbb{N} \backslash \{0\} & \frac{1}{p} & \frac{1- p}{p^2} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: Une IA essaie de trouver un nouvel algorithme pour résoudre un problème NP. La probabilité de succès, c'est-à-dire de trouver un meilleur algorithme lors de chaque tentative, est de 6% ($p = 0.06$).
> - **Variable**: Soit $X$ le nombre d'essais nécessaires pour trouver un nouvel algorithme. $X$ suit une **loi géométrique** avec $p = 0.06$.
> - **Probabilité**: La probabilité que l'IA trouve un algorithme exactement au $k$-ième essai est donnée par:
> $$\mathbb{P}(X = k) = (1 - 0.06)^{k - 1} \times 0.06$$
> - Par exemple, la probabilité que l'IA trouve un meilleur algorithme au **3e essai** est:
> $$\mathbb{P}(X = 3) = (0.94)^2 \times 0.06 = 0.0531$$
> - **[[Espérance (expected value)#^c716f7|Espérance]]**: Le nombre moyen d'essais nécessaires avant de trouver un nouvel algorithme est:
> $$\mathbb{E}[X] = \frac{1}{0.06} = 16.67$$
   Cela signifie qu'en moyenne, l'IA devra essayer **16 ou 17 fois** avant de trouver un meilleur algorithme.
> - **[[Variance#^4c0c18|Variance]]**: La variance du nombre d'essais est:
> $$\text{Var}(X) = \frac{1 - 0.06}{(0.06)^2} = 260.28$$
> Cela signifie que la dispersion autour du nombre moyen d'essais nécessaires est assez large.

> [!abstract]- Proposition
> Sachant que l’on déjà essayé $m$ fois sans succès, la probabilité de totaliser $n+m$ épreuves est égale à la probabilité de $n$ épreuves au début. En d’autres termes, toutes les épreuves passées sont perdues.
>
> Formellement, la perte de mémoire s’exprime comme
> $$\mathbb{P}(X = n + m \mid X \geq m + 1) = \mathbb{P}(X = n)$$
>
> **Démonstration:**
> $$\begin{align*}
> \mathbb{P}(X = n + m | X \geq m + 1) &= \frac{\mathbb{P}((X = n + m) \cap (X \geq m + 1))}{\mathbb{P}(X \geq m + 1)} \\
> &= \frac{\mathbb{P}(X = n + m)}{[1 - F_X(m)]} \\
> &= \frac{(1 - p)^{n+m-1}p}{(1 - p)^m} \\
> &= (1 - p)^{n-1}p \\
> &= \mathbb{P}(X = n) \quad \square
> \end{align*}$$

^579235

> [!abstract]- Corollaire
> La [[Loi géométrique#^579235|perte de mémoire]] est valable en deux directions, c’est-à-dire, elle caractérise la loi géométrique:
> - Si une [[Variable aléatoire#^dcd8d2|variable]] discrète $X \in \mathbb{N}$ vérifie la [[Loi géométrique#^579235|perte de mémoire]], alors $X$ doit suivre une [[Loi géométrique|loi géométrique]].
