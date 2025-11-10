---
title: Old
authors: Alessandro Dorigo
tags: []
---

## Tri bulle
![[ced1a26bbdee886e1ea9cfa01bd6b6f5.png]]
[[Chap 03 - slides_tris.pdf#Tri bulle]] / [[Chap 03 - slides_tris.pdf#Tri bulle (short)]]

Le tri bulle compare chaque paire d'éléments adjacents dans un tableau et les échange si nécessaire, ce qui fait "remonter" progressivement les éléments les plus grands (ou les plus petits, selon l'ordre de tri souhaité) vers la fin du tableau, comme des bulles dans l'eau.
## Tri par sélection
![[850ed9d1d4b93b2b06b9ea601e96a647.png]]
[[Chap 03 - slides_tris.pdf#Tri par selection]]

Ce tri parcourt le tableau pour sélectionner l'élément le plus petit (ou le plus grand) et l'échange avec l'élément en première position. Ensuite, il réitère le processus pour la portion restante du tableau, en plaçant à chaque fois l'élément sélectionné à la bonne position.
## Tri par insertion
![[50fad757a3fab78a418ace79c3be5e3c.png]]
![[86d311f77884e53af29a31c106816988.png]]
[[Chap 03 - slides_tris.pdf#Tri par insertion]]

Le tri par insertion prend chaque élément du tableau en partant du second et le compare aux éléments précédents, le déplaçant à sa position correcte parmi les éléments déjà examinés. C'est comme organiser des cartes.
## Tri shell
![[d52425473a828bd51639b3f728dfe57a.png]]
![[99ef3ae93eaa8377cf484106f3448be4.png]]
![[76c574ecbb70009bdeaeab0c027fe8e5.png]]
[[Chap 03 - slides_tris.pdf#Tri shell]]

Le tri Shell est une amélioration du tri par insertion, où la liste est divisée en sous-listes en utilisant un incrément (gap) qui diminue progressivement jusqu'à 1. Cela permet de comparer et d'échanger des éléments éloignés, réduisant ainsi les inversions à corriger lors de la phase finale avec un gap de 1. Quand le gap est 1, le tri Shell devient un tri par insertion classique, mais à ce stade, le tableau est déjà "presque trié", permettant ainsi de finir le tri rapidement. Il s’agit d’un tri non stable.
## Merge sort
![[9c1643d2245d21ca403a4ee038f7fe84.png]]
![[152002c959c9d86def2060e81fb3217c.png]]
[[Chap 03 - slides_tris.pdf#Merge sort]]

Le merge sort utilise la technique de "diviser pour régner" pour trier les éléments d’une liste. Il divise la liste en deux sous-listes, trie chaque sous-liste récursivement, puis fusionne les sous-listes triées pour obtenir une liste triée finale. Cela permet un tri efficace avec une complexité de $O(n \log(n))$.
## Quicksort
L’algorithme de tri rapide ou *quicksort* consiste à "couper" la liste à trier en deux sous-listes, toujours suivant le principe de la programmation diviser pour résoudre.

On peut par exemple scinder la liste en deux parties respectivement de taille `m`et `n`, où `m + n = taille de la liste`.

Nous scindons la liste à trier en deux sous-listes de taille `m` et `n`. L’idée est de placer dans la première sous-liste les `m` plus petits éléments de la liste, sans toutefois les trier entre-eux et donc de placer les `n` éléments suivants dans la seconde sous-liste, toujours sans les trier entre-eux, puis on recommence ce même procédé sur chaque sous-liste.

Il y a donc deux parties dans l’algorithme:
1. Choisir un élément pivot dans la liste et placer les éléments plus petits que ce pivot dans la première sous-liste et les éléments restants dans la seconde sous-liste;
2. Réaliser deux appels récursifs pour recommencer la procédure dans les deux sous-listes.

Une fois le pivot déterminé, il faut diviser la liste en deux sous-listes telles que:
- La première sous-liste ne contienne que des valeurs inférieures ou égales à la valeur du pivot
- La seconde sous-liste ne contienne que des valeurs supérieures à la valeur du pivot

Après le partitionnement, le pivot est placé en bonne position dans la liste triée. Il faut donc alors recommencer la procédure pour les sous-listes composées, d’une part, des éléments se trouvant à gauche du pivot et, d’autre part, des éléments se trouvant à droite du pivot.

[[Chap 03 - slides_tris.pdf#Quicksort (v1)]]

Une autre façon de réaliser la partition consiste à parcourir la liste initiale à partir de la gauche jusqu’à rencontrer le premier élément `y` supérieur au pivot puis, dans un second temps, de le parcourir à partir de la droite jusqu’à rencontrer le premier élément `z` inférieur au pivot.

Une fois ces deux parcours réalisés, on peut échanger ces deux éléments, `y` et `z`, mal placés. On poursuit ainsi jusqu’à atteindre la position finale du pivot.

[[Chap 03 - slides_tris.pdf#Quicksort (v2)]]
### On peut optimiser tout cela de manière drastique
[[Chap 03 - slides_tris.pdf#Quicksort]]

![[7afa0c3c3e3caf4a6c2c531c72d80340.png]]
## Complexités

|    Tri    |             Complex max             |  Complex min   |   Stable    |  En place   |
| :-------: | :---------------------------------: | :------------: | :---------: | :---------: |
|   Bulle   |              $O(n^2)$               |     $O(n)$     |   $\surd$   |   $\surd$   |
| Sélection |              $O(n^2)$               |    $O(n^2)$    | $\bigtimes$ |   $\surd$   |
| Insertion |              $O(n^2)$               |     $O(n)$     |   $\surd$   |   $\surd$   |
|  Fusion   |           $O(n \log(n))$            | $O(n \log(n))$ |   $\surd$   | $\bigtimes$ |
|   Shell   | $O(n \log^2(n)) \rightarrow O(n^2)$ |     $O(n)$     | $\bigtimes$ |   $\surd$   |
|  Rapide   |              $O(n^2)$               | $O(n \log(n))$ | $\bigtimes$ |   $\surd$   |
