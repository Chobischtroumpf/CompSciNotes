---
title: Quicksort
authors: Alessandro Dorigo
tags:
  -
---

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
