---
title: Équations différentielles du 1er ordre homogènes
authors: Alessandro Dorigo
tags:
  - Maths
---


> [!info]+ Definition
> Une équation différentielle du premier ordre est dite **homogène** si elle peut s’écrire sous la [[Équations différentielles du 1er ordre à variables séparables#^007524|forme normale]] et si la fonction $f$ satisfait la condition d'homogénéité suivante:
>
> $$f(ax, ay) = f(x, y) \quad \forall a \in \mathbb{R}$$
>
> Cette condition signifie que $f$ est une **fonction homogène de degré zéro**.
### Méthode de Résolution
Pour résoudre une équation différentielle homogène, on utilise le changement de variable suivant:

$$y(x) = x \cdot u(x)$$

où $u(x)$ est une fonction à déterminer. Ensuite, on dérive $y(x)$ par rapport à $x$:

$$y'(x) = u(x) + x \cdot u'(x)$$
#### Étapes de Résolution
1. **Substituer** $y(x) = x \cdot u(x)$ et $y'(x) = u(x) + x \cdot u'(x)$ dans l'équation différentielle initiale $y' = f(x, y)$.
2. **Simplifier l'équation** pour obtenir une équation différentielle en $u$ et $x$.
3. **Résoudre l'équation différentielle** obtenue pour $u(x)$.
4. **Substituer** la solution $u(x)$ dans $y(x) = x \cdot u(x)$ pour obtenir la solution générale.
