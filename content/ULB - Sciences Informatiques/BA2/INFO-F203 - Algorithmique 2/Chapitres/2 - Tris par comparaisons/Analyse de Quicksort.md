---
title: Analyse de Quicksort
authors: Alessandro Dorigo
tags:
  - Algo
---


Cette note concerne l'analyse de complexité de [[Quicksort]], initialement vu en `INFO-F103`.
## Analyse au pire des cas
L'analyse du pire cas nous révèle une facette intéressante de cet algorithme:

> [!abstract]- Théorème
> Le tri rapide utilise $\thicksim n^2/2$ comparaisons dans le pire cas pour trier un tableau de taille $n$.
## Démonstration
> [!info]+ Démonstration
> Le pire cas se produit lorsqu'à chaque étape de l'algorithme :
> - Le pivot choisi se trouve être l'élément minimal ou maximal
> - Un des sous-tableaux est vide
> - L'autre sous-tableau contient tous les éléments sauf le pivot
>
> Dans ce cas, le nombre de comparaisons suit la relation :
> $$T(n) = T(n - 1) + (n - 1)$$
> où $(n - 1)$ représente le nombre de comparaisons nécessaires pour le partitionnement.

> [!tip]+ Remarque
> C'est précisément ce pire cas qui a motivé l'introduction de la randomisation dans l'algorithme.
## Randomisation et analyse en moyenne
Pour éviter le pire cas, nous utilisons une version randomisée de l'algorithme.

> [!abstract]- Théorème
> Le tri rapide randomisé utilise $\thicksim 2n \ln n$ comparaisons en moyenne pour trier un tableau de $n$ valeurs distinctes.
### Analyse mathématique
Pour l'analyse en moyenne, soit $C(n)$ le nombre moyen de comparaisons pour un tableau de taille $n$. Nous avons:
$$C(n) = (n + 1) + \frac{1}{n}\sum_{i = 0}^{n - 1}(C(i) + C(n - i - 1))$$

Cette formule s'explique car:
- Le pivot peut être n'importe quel élément avec probabilité $1/n$
- Chaque choix de pivot crée deux sous-problèmes de tailles $i$ et $n-i-1$
- $(n+1)$ comparaisons sont nécessaires pour le partitionnement

La résolution de cette récurrence mène à:
$$\frac{C(n)}{n + 1} = \frac{C(n - 1)}{n} + \frac{2}{n + 1}$$

Par un "téléscopage" astucieux de cette équation, on obtient:
$$\frac{C(n)}{n + 1} = \frac{2}{3} + \frac{2}{4} + \frac{2}{5} + ... + \frac{2}{n + 1} \leq 2H_{n + 1}$$
où $H_n$ est le nombre harmonique d'ordre $n$.

> [!tip]+ Remarque
> Comme $H_n \sim \ln n$, nous obtenons finalement $C(n) \sim 2n\ln n$.
## Implications pratiques
Cette analyse révèle que:
1. La randomisation transforme un algorithme de complexité quadratique en un algorithme de complexité quasi-linéaire en moyenne
2. La constante multiplicative (2) est relativement petite, ce qui fait du tri rapide un algorithme très efficace en pratique
3. La performance est proche de la borne inférieure théorique pour les algorithmes de tri par comparaisons

> [!tip]+ Remarque
> Bien que le tri fusion garantisse une complexité de $O(n\log n)$ dans tous les cas, le tri rapide est souvent plus rapide en pratique grâce à sa meilleure utilisation du cache et sa simplicité d'implémentation.
