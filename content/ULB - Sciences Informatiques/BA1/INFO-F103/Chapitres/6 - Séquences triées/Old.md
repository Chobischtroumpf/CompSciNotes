---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

Une séquence triée tel que décrite dans ce chapitre est un type de donnée abstraite.
## Interface d'une séquence triée
* `getNext` : donne accès à l'élément de la séquence triée qui suit l'élément courant
* `getPrevious` : donne accès à l'élément de la séquence triée qui précède l'élément courant
* `getData` : indique la valeur contenue dans l'élément courant dans la séquence triée
* `getFirst` : donne accès au premier élément de la séquence triée
* `getLast` : donne accès au dernier élément de la séquence triée
* `insert` : insère un élément d'une valeur donnée dans la séquence triée
* `remove` : supprime l'élément courant de la séquence triée
* `find` : donne accès à un élément de la séquence triée, s'il existe, d'une valeur donné

-> [[Chap 06 - slides_abr.pdf#Sequence triée]]
## Types de séquences triées
### Stockée de manière contiguë en mémoire:
##### Avantage:
- Une séquence triée de cette façon permet une recherche d'élément efficace grâce à une recherche dichotomique.
##### Désavantag:
- Gestion lourde pour l’insertion et suppression d'éléments car celle-ci entraîne des décalages d'éléments vers la droite et la gauche.
### Stockée dans une liste chaînée triée:
##### Avantage:
- Les opérations d'insertion et de suppression d'éléments seront aisées à réaliser
##### Désavantage:
- La recherche d'un élément dans la séquence sera d'une complexité en temps linéaire
- Les opérations d'insertion et de suppression pourraient être précédées d'une recherche dans la liste avant de pouvoir être réalisées
#### Types de listes triées
![[Pasted image 20240311155848.png]]
Une liste triée peut être bidirectionnelle, circulaire, et avec un élément bidon en tête de liste.

-> [[Chap 06 - slides_abr.pdf#Liste Circulaire Bidirectionnelle]]
### Stockée dans une séquence triée sur mesure:
On utilise un arbre binaire particulier dont les nœuds sont les éléments de la séquence triée et respectant la propriété suivante:
- Soit `x` l’information présente dans le nœud courant, on impose que le sous-arbre gauche du nœud courant ne contienne que des éléments dont la valeur est inférieure ou égale à `x` et que le sous-arbre droit ne contienne que des éléments dont la valeur est supérieure ou égale à `x`
