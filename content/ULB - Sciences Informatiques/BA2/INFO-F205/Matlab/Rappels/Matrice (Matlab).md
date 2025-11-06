---
title: Matrice (Matlab)
authors: Alessandro Dorigo
tags:
  - Maths
  - Matlab
---


Une **matrice** se déclare comme une suite de [[Vecteur (Matlab)|vecteurs]] séparés par un point virgule. La matrice identité 2 × 2 peut donc se définir comme ceci:

```matlab
I2 = [1 0; 0 1]
```

Il existe des fonctions servant à générer des matrices dont `eye` qui génère la matrice identité (ou tout du moins une sous-matrice d’une matrice identité), `zeros` et `ones` qui génèrent respectivement une matrice ne contenant que des `0` ou que des `1`, etc.

Si plusieurs paramètres entiers sont donnés, alors la matrice (ou plus généralement le tableau de matrices) renvoyée aura les dimensions demandées.

> [!note]
> Si un unique paramètre est donné à ces fonctions, alors elles renverront une matrice carrée dont la dimension correspond à ce paramètre.

Les dimensions d’une matrice peuvent être récupérées via la fonction `size` qui renvoie un [[Vecteur (Matlab)|vecteur]] dont les composantes correspondent aux dimensions. La fonction `length` quant à elle renvoie la plus grande des dimensions. La transposée d’une matrice (ou d’un [[Vecteur (Matlab)|vecteur]]) se fait via l’apostrophe.

```matlab
>> A = zeros(2, 3)
A =
	0  0  0
	0  0  0

>> size(A)
ans =
	2  3

>> length(A)
ans = 3

>> A'
ans =
	0  0
	0  0
	0  0
```

> [!note]
> Si `A` et `B` sont deux matrices carrées, l’instruction `C = A*B` va prendre le [[Produit Matriciel|produit matriciel]] entre `A` et `B` et si c’est le [[Produit de Hadamard|produit de Hadamard]] qui est voulu, il faut utiliser l’instruction `C = A .* B`.
