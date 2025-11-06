---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

Un arbre est une structure de données composée de nœuds et d’arêtes, où chaque nœud, à l'exception de la racine, est connecté à un unique nœud parent, formant ainsi une hiérarchie sans cycles. La racine est le nœud sans parent, situé au sommet de l'arbre. Un chemin dans un arbre est une suite de nœuds connectés par des arêtes, où chaque paire de nœuds successifs est directement reliée.

| ![[Pasted image 20240306142542.png]] | -------------------------------------------------------------------------------------------------- |
| :----------------------------------: | :------------------------------------------------------------------------------------------------: |

## Définitions clés

|      Nom       |                                       Définition                                       |
| :------------: | :------------------------------------------------------------------------------------: |
|      Nœud      |                             Élément constitutif d’un arbre                             |
|     Arête      |                                 Lien entre deux nœuds                                  |
|     Racine     |                      Nœud sans parent, point de départ de l’arbre                      |
|     Chemin     |                  Suite de nœuds reliés par des arêtes sans répétition                  |
|     Degré      |                 Nombre de sous-arbres directement connectés à un nœud                  |
|    Feuilles    |                             Nœuds sans enfants, degré zéro                             |
| Nœuds internes |                             Nœuds ayant au moins un enfant                             |
|    Hauteur     | Plus long chemin de la racine à une feuille, représentant le niveau maximum de l’arbre |
### Caractéristiques des arbres
- Un arbre avec $n$ nœuds possède toujours $n-1$ arêtes, car à l’exception de la racine, chaque nœud est connecté exactement une fois à un autre nœud.
- Un arbre est **$m$-aire** si chaque nœud non-feuille peut avoir au maximum $m$ enfants.
## Structures spécifiques des arbres $m$-aires

| Structure |                                                                                                                                                   Définition                                                                                                                                                    |
| :-------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   Plein   |                                                                                                 Un arbre $m$-aire plein est tel que chaque nœud a soit aucun enfant (une feuille), soit exactement $m$ enfants                                                                                                  |
|  Rempli   |                                                                                                              Un niveau $i$ est rempli si tous les nœuds du niveau $i-1$ ont exactement $m$ enfants                                                                                                              |
|  Complet  | Un arbre est complet si tous les niveaux, sauf éventuellement le dernier, sont entièrement remplis et que les nœuds au dernier niveau sont tous le plus à gauche possible. Un arbre $m$-aire complet de hauteur $n$ a $m^k$ nœuds au niveau $k < n$ et entre $0$ et $m^n$ nœuds au niveau $n$, alignés à gauche |
|  Parfait  |                                                                                     Un arbre est parfait lorsque toutes les feuilles se trouvent au même niveau et que tous les nœuds internes ont précisément $m$ enfants                                                                                      |

| ![[Pasted image 20240306142722.png]] | ![[Pasted image 20240306142926.png]] | ![[Pasted image 20240306143258.png]] |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
|             Arbre plein              |            Arbre complet             |            Arbre parfait             |
## Arbres binaires
- Le type d’arbre $m$-aire le plus classique apparaît lorsque $m$ vaut $2$, on parle alors d’***arbres binaires***
	- Un arbre binaire peut aussi être plein, complet ou parfait
	- De plus, chaque nœud ayant des enfants a un enfant gauche et/ou un enfant droit

| ![[Pasted image 20240306143349.png]] | Les enfants gauche / droit du nœud d’indice $i$ se trouvent respectivement aux indices $2i + 1$ et $2i + 2$ (voir [[#7 Les files à priorités]]) | ![[Pasted image 20240307103438.png]] |
| :----------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------: |

## Interface d'un arbre récursif
- `getRootVal`: indique la valeur contenue dans la racine de l’arbre considéré
- `setRootVal`: modifie la valeur contenue dans la racine de l’arbre considéré
- `getLeftChild`: donne accès au sous-arbre gauche de la racine de l’arbre considéré
- `getRightChild`: donne accès au sous-arbre droit de la racine de l’arbre considéré
- `modifyLeft`: modifie le sous-arbre gauche de la racine de l’arbre considéré
- `modifyRight`: modifie le sous-arbre droit de la racine de l’arbre considéré

-> [[Chap 05 - slides_arbres.pdf#Arbre binaire via listes Python]]
-> [[Chap 05 - slides_arbres.pdf#Arbre binaire]]
## Interface d'un arbre binaire non récursif (+ nœud)
Un arbre binaire peut aussi être vu comme composé physiquement de nœuds.
- Un nœud de l’arbre possède donc alors explicitement un enfant gauche et un enfant droit (qui sont des nœuds et non plus des sous-arbres)

| ![[Pasted image 20240307104535.png]] | -------------------------------------------------------------------------------- |
| :----------------------------------: | :------------------------------------------------------------------------------: |

- `treeGetRoot`: donne accès au nœud qui est à la racine de l’arbre considéré
- `treeGetLeft`: donne accès à l’enfant gauche du nœud considéré
- `treeGetRight`: donne accès à l’enfant droit du nœud considéré
- `treeSetLeft`: modifie le nœud enfant gauche (et donc sa descendance) du nœud considéré dans l’arbre
- `treeSetRight`: modifie le nœud enfant droit (et donc sa descendance) du nœud considéré dans l’arbre

-> [[Chap 05 - slides_arbres.pdf#Arbre binaire non récursif via nœuds]]
### Interface d'un nœud
- `getInfo`: indique la valeur contenue dans le nœud
- `getLeft`: donne accès au nœud enfant gauche du nœud courant
- `getRight`: donne accès au nœud enfant droit du nœud courant
- `setInfo`: modifie la valeur contenue dans le nœud
- `setLeft`: modifie le nœud enfant gauche du nœud courant
- `setRight`: modifie le nœud enfant droit du nœud courant

-> [[Chap 05 - slides_arbres.pdf#Nœud d'un arbre binaire non récursif]]
## Parcours d'arbres binaires
- Il existent différentes manières de parcourir un arbre en fonction de l’ordre dans lequel nous considérons les nœuds de cet arbre.

| ![[Pasted image 20240307110553.png]] | -------------------------------------------------- |
| :----------------------------------: | :------------------------------------------------: |

### Parcours préfixé
- Le ***parcours préfixé*** ou ***parcours en préordre*** consiste à traiter d’abord la racine, puis le sous-arbre gauche et enfin le sous-arbre droit.
$$
1 - 2 - 4 - 5 - 3 - 6 - 7
$$
-> [[Chap 05 - slides_arbres.pdf#Parcours préfixé d’arbres récursifs]]
-> [[Chap 05 - slides_arbres.pdf#Parcours préfixé d’arbres non récursifs]]
### Parcours infixé
- Le ***parcours infixé*** ou ***parcours en inordre***, ou encore ***parcours symétrique***, consiste à traiter d’abord le sous-arbre gauche, puis la racine et enfin le sous-arbre droit.
$$
4 - 2 - 5 - 1 - 6 - 3 - 7
$$
-> [[Chap 05 - slides_arbres.pdf#Parcours infixé d’arbres récursifs]]
-> [[Chap 05 - slides_arbres.pdf#Parcours infixé d’arbres non récursifs]]
### Parcours suffixé
- Le ***parcours suffixé*** ou ***parcours en postordre*** traite d’abord le sous-arbre gauche, puis le sous-arbre droit et enfin la racine.
$$
4 - 5 - 2 - 6 - 7 - 3 - 1
$$
-> [[Chap 05 - slides_arbres.pdf#Parcours suffixé d’arbres récursifs]]
-> [[Chap 05 - slides_arbres.pdf#Parcours suffixé d’arbres non récursifs]]
### Parcours par niveau
- Le ***parcours par niveau*** ou ***parcours en largeur*** traite les nœuds niveau par niveau, en partant de la racine.
$$
1 - 2 - 3 - 4 - 5 - 6 - 7
$$
-> [[Chap 05 - slides_arbres.pdf#Parcours par niveau d’arbres récursifs]]
-> [[Chap 05 - slides_arbres.pdf#Parcours par niveau d’arbres non récursifs]]
## Théorème 1:
- Un arbre binaire parfait de hauteur $n$ possède $2^n$ feuilles.

Soit $n \in \mathbb{N}$ la hauteur d'un arbre binaire parfait. On définit $f_n$ comme le nombre de feuilles de cet arbre. Pour un arbre binaire parfait, nous avons les propriétés suivantes:

1. Pour $n=1$, $f_1 = 2$ car un arbre de hauteur $1$ possède $2^1$ feuilles.
2. Supposons que pour une hauteur $n$, l'arbre possède $2^n$ feuilles, soit $f_n = 2^n$.
3. Pour passer de la hauteur $n$ à $n+1$, on double le nombre de feuilles (chaque feuille devient le parent de deux nouvelles feuilles), donc $f_{n+1} = 2 \times f_n = 2 \times 2^n = 2^{n+1}$.

Ainsi, par induction, on peut affirmer qu'un arbre binaire parfait de hauteur $n$ possède $2^n$ feuilles, soit $f_n = 2^n$.
## Théorème 2:
- Un arbre binaire parfait de hauteur $n$ possède $2^{n+1} - 1$ nœuds.

Soit $n \in \mathbb{N}$ la hauteur d'un arbre binaire parfait. On note $N_n$ le nombre total de nœuds dans cet arbre à la hauteur $n$. Pour un tel arbre, nous avons:

 1. Pour $n=0$ (hauteur $0$, seulement la racine), $N_0 = 2^{0+1} - 1 = 1$, ce qui est vérifié puisqu'un arbre de hauteur $0$ a effectivement un seul nœud (la racine).
2. Supposons que pour une hauteur $n$, le nombre total de nœuds est $N_n = 2^{n+1} - 1$.
3. Démontrons que cette propriété est vraie pour $n+1$. Un arbre de hauteur $n+1$ se compose de la racine, et de deux sous-arbres binaires parfaits de hauteur $n$ (chaque sous-arbre ayant $N_n = 2^{n+1} - 1$ nœuds). Ainsi, le nombre total de nœuds à la hauteur $n+1$ est:
$$
N_{n+1} = 1 + 2 \cdot N_n = 1 + 2(2^{n+1} - 1) = 2^{n+2} - 1
$$
Cela confirme que pour un arbre binaire parfait de hauteur $n$, le nombre total de nœuds est $2^{n+1} - 1$.
## Théorème 3:
- Un arbre binaire qui possède $m$ nœuds internes, possède au plus $m + 1$ feuilles.

Soit un arbre binaire avec $m$ nœuds internes. Nous démontrons que cet arbre contient au maximum $m + 1$ feuilles, notées $f$. Considérons:

1. Dans un arbre binaire parfait, le nombre total de nœuds est $2^{n+1} - 1$, avec $f_n = 2^n$ feuilles à la hauteur $n$.
2. En soustrayant le nombre de feuilles du total de nœuds, le nombre de nœuds internes est alors $m = 2^{n+1} - 1 - f_n = 2^n - 1$.
3. Ainsi, le nombre de feuilles $f$ est donné par $f = m + 1$, car chaque nœud interne, sauf la racine, contribue à la formation d'une feuille.

En conséquence, un arbre binaire avec $m$ nœuds internes possède au plus $m + 1$ feuilles, confirmant la relation entre les nœuds internes et les feuilles dans un arbre binaire.
## Forêts et arbres $m$-aires
- Une forêt est un ensemble d’arbres.
	- Par exemple, nous pouvons dire que l’ensemble des sous-arbres de la racine d’un arbre $m$-aire est une forêt.

| ![[Pasted image 20240308115034.png]] | -------------------------------------------------------------------- |
| :----------------------------------: | :------------------------------------------------------------------: |

- Un nœud possède zéro, un ou plusieurs enfants, et zéro, un ou plusieurs frères.
### Interface d’une forêt
- `getRootVal`: indique la valeur contenue dans la racine de l’arbre considéré
- `setRootVal`: modifie la valeur contenue dans la racine de l’arbre considéré
- `getChild`: donne accès au premier enfant de la racine de l’arbre considéré
- `getBrother`: donne accès au frère de la racine de l’arbre considéré
- `modifyChild`: modifie les enfants de la racine de l’arbre considéré
- `modifyBrother`: modifie les frères de la racine de l’arbre considéré

-> [[Chap 05 - slides_arbres.pdf#Forêt ou arbre m-aire]]
### Parcours des forêts / arbres $m$-aires
- Les forêts / arbres $m$-aires ont également des ***parcours en préordre***, en ***postordre*** et ***par niveau***.

-> [[Chap 05 - slides_arbres.pdf#Parcours en preordre d'une foret / arbre m-aire]]
-> [[Chap 05 - slides_arbres.pdf#Parcours en postordre d'une foret / arbre m-aire]]
-> [[Chap 05 - slides_arbres.pdf#Parcours par niveau d'une foret / arbre m-aire]]
