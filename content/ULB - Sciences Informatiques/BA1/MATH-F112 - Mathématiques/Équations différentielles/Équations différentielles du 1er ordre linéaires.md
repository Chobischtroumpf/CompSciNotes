---
title: Équations différentielles du 1er ordre linéaires
authors: Alessandro Dorigo
tags:
  - Maths
---


> [!info]+ Definition
> Une **équation différentielle du premier ordre linéaire** s’écrit sous la forme:
>
> $$q(x) \cdot y' + p(x) \cdot y = f(x)$$
>
> où:
> - $q(x)$ et $p(x)$ sont des fonctions de $x$,
> - $f(x)$ est une fonction donnée,
> - $y(x)$ est la fonction inconnue.
## Méthode de Résolution
La résolution d’une équation différentielle linéaire du premier ordre se fait en plusieurs étapes:

---
### 1. Résolution de l'Équation Linéaire Homogène Associée (ELHA)
L’**équation linéaire homogène associée (ELHA)** est obtenue en posant $f(x) = 0$:

$$q(x) \cdot y' + p(x) \cdot y = 0$$
#### Solution de l'ELHA
La solution générale de l’ELHA est donnée par:

$$y_H = C \cdot e^{-\int \frac{p(x)}{q(x)} \, dx}$$

- $C$ est une constante arbitraire.
- On peut parfois résoudre cette équation en utilisant la **séparation des variables** suivie d'une intégration.
---
### 2. Résolution de l'Équation avec Second Membre (SPEL)
Pour résoudre l’**équation avec second membre**, on utilise la méthode de la **variation de la constante**.
#### Forme de la Solution Particulière
On cherche une solution particulière sous la forme:

$$y_P = u(x) \cdot e^{-\int \frac{p(x)}{q(x)} \, dx}$$

où $u(x)$ est une fonction à déterminer.
#### Substitution dans l’Équation de Base
On remplace $y_P$ et $y_P'$ dans l'équation différentielle d'origine:

$$q(x) \cdot y_P' + p(x) \cdot y_P = f(x)$$

On obtient alors une équation permettant de déterminer $u(x)$.

---
### 3. Solution Générale
La **solution générale** de l'équation différentielle est la somme de la solution homogène et de la solution particulière:

$$y(x) = y_H(x) + y_P(x)$$

---
### 4. Application des Conditions Initiales (si présentes)
Si des conditions initiales sont données, par exemple $y(x_0) = y_0$, on procède comme suit:
1. **Substituer** $y(x)$ et $x_0$ dans l'équation.
2. **Résoudre** pour trouver la constante $C$.
