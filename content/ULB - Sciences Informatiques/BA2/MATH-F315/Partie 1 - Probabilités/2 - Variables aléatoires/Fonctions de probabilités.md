---
title: Fonctions de probabilités
authors: Alessandro Dorigo
tags:
  - VarAlea
  - Proba
---


Formellement appris en `MATH-F315`. Pour les fonctions "classiques" des maths, voir *link*.
## Fonction de répartition (Cumulative Distribution Function - CDF)

> [!info]+ Définition
> La **fonction de répartition** d'une [[Variable aléatoire#^dcd8d2|variable aléatoire]] $X$, notée $F_X(x)$, donne la probabilité que $X$ prenne une valeur inférieure ou égale à $x$.

^a65013

> [!abstract]- Formule
> $$F_X(x) = \mathbb{P}(X \leq x) \quad \forall x$$

> [!example]+ Exemple
>
| ![[Pasted image 20241022153022.png]] | ![[Pasted image 20241022153140.png]] |
| :----------------------------------: | :----------------------------------: |
## Fonction de survie (Survival Function)

> [!info]+ Définition
> La **fonction de survie** est complémentaire à la [[Fonctions de probabilités#^a65013|fonction de répartition]]:

> [!abstract]- Formule
> $$S_X(x) = 1-F_X(x) = \mathbb{P}(X > x)$$

> [!example]+ Exemple
> ![[Pasted image 20241022153431.png]]
## Fonction de densité (Probability Density Function - PDF)

> [!info]+ Définition
> La **fonction de densité de probabilité** (PDF) représente la densité de la probabilité en un point $x$ et est la dérivée de la [[Fonctions de probabilités#^a65013|fonction de répartition]].

> [!abstract]- Formules
> $$f_X(x) = \frac{\partial}{\partial x}F_X(x)$$
> De plus:
> $$\int^\infty_{-\infty} f_X(u)du =1$$
> $$F_X(x)= \int^x_{-\infty} f_X(u)du$$
> $$\mathbb{P}(a\leq X \leq b) = F_X(b) - F_X(a) = \int^b_a f_X(u)du$$

> [!example]+ Exemple
>
| ![[Pasted image 20241022153009.png]] | ![[Pasted image 20241022153150.png]] |
| :----------------------------------: | :----------------------------------: |
## Fonction de masse (Mass Function)

> [!info]+ Définition
> Pour une [[Variable aléatoire#^dcd8d2|variable aléatoire]] **discrète**, la **fonction de masse** donne la probabilité que $X$ prenne une valeur spécifique $x_k$.

> [!abstract]- Formules
> $$p_X(x_k) = \mathbb{P}(X = x_k) = F_X(x_k) - F_X(x_{k-1})$$
> De plus:
> $$\sum_{k=0}^\infty p_X(x_k)=1$$
> - Doit être continue à droite

> [!example]+ Exemple
> ![[Pasted image 20241022153616.png]]
## Fonction quantile

> [!abstract]- Formule
> $$
> Q_X(\alpha) = x_\alpha \Leftrightarrow F_X(x_\alpha) = \alpha
> $$

> [!example]+ Exemple
> ![[Pasted image 20241022153812.png]]

- Médiane: $\text{med}(X) = Q_X(0.5)$
- Quartile inférieur: $Q_X(0.25)$
- Quartile supérieur: $Q_X(0.75)$
- Écart interquartile: $\text{IQR}(X) = Q_X(0.75) - Q_X(0.25)$
