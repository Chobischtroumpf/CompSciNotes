---
title: Solution d'une équation de récurrence linéaire non-homogène
authors: Alessandro Dorigo
tags:
  - MathDis
---


 > [!info]+ Définition
> Une équation de récurrence linéaire non-homogène est une équation de la forme :
> $$f(n) - a_1f(n-1) - a_2f(n-2) - \cdots - a_df(n-d) = g(n)$$
> où $g(n)$ est une fonction non nulle.
> Les coefficients $a_1, a_2, ..., a_d$ sont constants.

> [!tip]+ Remarque
> La résolution se fait en trois étapes :
> 1. Résoudre l'équation homogène associée en remplaçant $g(n)$ par 0
>    $$f(n) - a_1f(n-1) - a_2f(n-2) - \cdots - a_df(n-d) = 0$$
>    On obtient une solution générale $f_{HA}(n)$ avec $c_1,...,c_d$ à déterminer
> 2. Trouver une solution particulière $f_{SP}(n)$ de l'équation non-homogène
> 3. La solution générale est $f(n) = f_{HA}(n) + f_{SP}(n)$
>    Utiliser les conditions initiales pour déterminer les constantes

> [!example]+ Exemple
> Résolution de l'équation : $f(n) = 4f(n-1) + 3^n$ avec $f(1) = 1$
>
> **Étape 1**: Résolution de l'EHA $f(n) = 4f(n-1)$
> Solution générale : $f_{HA}(n) = c_1 \cdot 4^n$
>
> **Étape 2**: Recherche d'une solution particulière
> On pose $f_{SP}(n) = c_2 \cdot 3^n$
> $$c_2 \cdot 3^n = 4c_2 \cdot 3^{n-1} + 3^n$$
> $$c_2 \cdot 3^n = 4c_2 \cdot 3^{n-1} + 3^n \Leftrightarrow 3c_2 = 4c_2 + 3 \Leftrightarrow c_2 = -3$$
> Donc $f_{SP}(n) = -3^{n+1}$
>
> **Étape 3**: Solution générale et conditions initiales
> $$f(n) = f_{HA}(n) + f_{SP}(n) = c_1 \cdot 4^n - 3^{n+1}$$
> Avec $f(1) = 1$ :
> $$f(1) = 1 \Leftrightarrow 4c_1 - 9 = 1 \Leftrightarrow c_1 = \frac{5}{2}$$
>
> **Solution finale**:
> $$f(n) = \frac{5}{2} \cdot 4^n - 3^{n+1}, \quad \forall n \geq 1$$

> [!tip]+ Remarque
> Pour trouver une solution particulière de l'équation non-homogène, voici les règles à suivre selon la forme de $g(n)$ :
>
> 1. Si $g(n)$ est une exponentielle (ex: $g(n) = 3^n$)
>    - Essayer $f(n) = c \cdot 3^n$ (même base)
>
> 2. Si $g(n)$ est un polynôme de degré $k$ (ex: $g(n) = n^2 - 1$)
>    - Essayer $f(n) = c_1n^2 + c_2n + c_3$ (même degré)
>
> 3. Si $g(n)$ est une combinaison (ex: $g(n) = 2^n + n$)
>    - Essayer $f(n) = c_1 \cdot 2^n + c_2n + c_3$
>
> 4. Si $g(n) = 2^n$ et $f(n) = a \cdot 2^n$ ne fonctionne pas
>    - Essayer $f(n) = an \cdot 2^n$ ou $f(n) = an^2 \cdot 2^n$ si nécessaire
