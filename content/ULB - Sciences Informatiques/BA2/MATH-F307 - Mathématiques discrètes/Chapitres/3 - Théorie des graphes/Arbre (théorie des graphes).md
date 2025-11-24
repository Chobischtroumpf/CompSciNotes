---
title: Arbre (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
  - Arbre
---


Formellement appris en `MATH-F307`. Pour les arbres vus de manière algorithmique, voir *link*.

> [!info]+ Définition
> Un **arbre** est un graphe [[Graphe connexe#^942c76|connexe]] et acyclique. Ses sommets de [[Degré#^3c01ed|degré]] $1$ sont appelés des **feuilles**. Un graphe acyclique (réunion disjointe d'arbres) est une **forêt**.

^dcd789

> [!abstract]- Lemme 3.4.1
> Tout sous-graphe [[Graphe connexe#^942c76|connexe]] d'un arbre est aussi un arbre.
> - Si un sous-graphe d’un graphe $G$ possède un cycle, alors $G$ possède aussi un cycle. $\square$

>[!abstract]- Lemme 3.4.2
> Tout arbre à $\geq 2$ sommets possède au moins une feuille.
>
> ![[86f93cf4b856ba63533c3f316b68b9a7.png]]

> [!abstract]- Théorème 3.4.3
> Tout [[Arbre (théorie des graphes)#^dcd789|arbre]] à $n$ sommets possède exactement $n − 1$ arêtes.
>
> ![[f83b1863cfe1f0c1c314da1575195ef8.png]]

> [!abstract]- Théorème 3.4.4
> Pour tout graphe $G$, les affirmations suivantes sont équivalentes:
> 1) $G$ est [[Graphe connexe#^942c76|connexe]] et acyclique (un [[Arbre (théorie des graphes)#^dcd789|arbre]]);
> 2) $G$ est [[Graphe connexe#^942c76|connexe]] et $\vert E (G)\vert = \vert V (G)\vert − 1$;
> 3) G est [[Graphe connexe#^942c76|connexe]] et $\vert E (G)\vert = \vert V (G)\vert − 1$.
>
> ![[cf73a59a6dbe0f9975cd4be6ba17afff.png]]
> ![[4d1103c6a9ae841dd7c17cf78c886b8f.png]]
# Arbres couvrants
> [!info]+ Définition
> Un [[Arbre (théorie des graphes)#^dcd789|arbre]] $A \subseteq G$ est dit **couvrant** si $V(A) = V(G)$.
>
> ![[ed742d1562a47c14e7e2dd9e025d2fb3.png]]

^d6e627
## Problème principal
Étant donné un graphe [[Graphe connexe#^942c76|connexe]] $G$ et un poids $w(e) \in \mathbb{R}$ pour chaque arête, trouver un arbre couvrant $A$ de poids minimum.

On peut utiliser l'algorithme glouton pour ce problème:
1. Trier les arêtes par poids croissant: $$w(e_1) \leq w(e_2) \leq \cdots \leq w(e_m)$$
2. Initialiser l'ensemble: $$F \gets \emptyset$$
3. Pour chaque $i = 1, \dots, m$:
   - Si $F + e_i$ est acyclique: $$F \gets F + e_i$$

> [!abstract]- Théorème 3.4.5
> Tout graphe [[Graphe connexe#^942c76|connexe]] $G$ possède un [[Arbre (théorie des graphes)#^990ad1|arbre couvrant]].
>
> ![[593dfa85317aa619b3196710d103c6cd.png]]
