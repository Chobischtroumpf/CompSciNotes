---
title: Fonctions Matlab
authors: Alessandro Dorigo
tags:
  - Maths
  - Matlab
---


Matlab propose toute une série de fonctions préexistantes (e.g. `sin, cos, exp, log, abs, ...`) qui peuvent être appelées tant sur des nombres que sur des [[Matrice (Matlab)|matrices]] (et donc des [[Vecteur (Matlab)|vecteurs]]) en quel cas l’opération est effectuée individuellement sur chaque entrée de la [[Matrice (Matlab)|matrice]].

> [!note]
> `log(M)` ne calcule pas le `log` matriciel, il faut utiliser la fonction `logm` pour cela.

De manière plus générale, précéder les opérateurs d’un point permet d’en utiliser la version **component-wise**. Mettre un point-virgule après les définitions de permet de ne pas afficher le résultat de l’instruction.

La fonction `isequal` détermine l’égalité entre plusieurs [[Matrice (Matlab)|matrices]] (ou [[Vecteur (Matlab)|vecteurs]]). Cette fonction peut être appelée avec plus de deux paramètres et renvoie 1 si et seulement si toutes les [[Matrice (Matlab)|matrices]] reçues ont les mêmes dimensions et les mêmes entrées aux mêmes indices.
