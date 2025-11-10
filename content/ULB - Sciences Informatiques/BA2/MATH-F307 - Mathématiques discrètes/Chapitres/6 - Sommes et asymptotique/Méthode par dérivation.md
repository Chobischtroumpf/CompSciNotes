---
title: Méthode par dérivation
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


Les **séries géométriques** sont relativement simples à manipuler. Cependant, en pratique, il est fréquent de rencontrer des sommes qui ne peuvent pas être transformées directement sous la forme d'une série géométrique avec des substitutions simples.

Une méthode **non évidente mais puissante** pour obtenir de nouvelles formules de sommation à partir de formules existantes consiste à **dériver ou intégrer par rapport à une variable**, ici notée $x$.

> [!example]+ Somme de $\sum_{k=1}^n kx^k$
> Considérons la somme suivante:
> $$\sum_{k=1}^n kx^k = x + 2x^2 + 3x^3 + \cdots + nx^n$$

> [!abstract]- Théorème 6.3.1
> Pour $x \neq 1$, on a la formule suivante pour la somme dérivée:
> $$\sum_{k=1}^n kx^k = \frac{x - (n+1)x^{n+1} + nx^{n+2}}{(1 - x)^2}$$
>
> **Démonstration:**
> 1. On sait que pour $x \neq 1$:
> $$\sum_{k=0}^n x^k = \frac{1 - x^{n+1}}{1 - x}$$
> 2. En différentiant chaque terme de la somme par rapport à $x$, on obtient une nouvelle somme:
> $$\sum_{k=0}^n kx^{k-1} = \text{expression simplifiée de la dérivée de la somme géométrique}$$
> 3. En multipliant les deux côtés par $x$, on trouve la formule fermée désirée pour la somme $\sum_{k=1}^n kx^k$.

> [!abstract]- Corollaire 6.3.2
> Pour $|x| < 1$, la somme infinie de cette série est:
> $$\sum_{k=1}^{\infty} kx^k = \frac{x}{(1 - x)^2}$$
>
> ![[b55569874a496930e3207d02e536b44f.png]]
