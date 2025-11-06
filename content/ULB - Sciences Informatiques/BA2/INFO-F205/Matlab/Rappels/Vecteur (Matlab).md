---
title: Vecteur (Matlab)
authors: Alessandro Dorigo
tags:
  - Maths
  - Matlab
---


L’élément central pour les opérations est la [[Matrice (Matlab)|matrice]] (ce qui comporte les vecteurs comme cas particuliers). La déclaration d’un **vecteur** se fait via les crochets:

```matlab
x = [x1, x2, ...]
x = [x1 x2 ...]
```

La notation `beg:end` (ou de manière plus générale `beg:step:end`) génère un vecteur contenant toutes les valeurs de la forme `beg + t*step` pour `t` entre `0` et `⌊(end-beg)/step⌋`.
