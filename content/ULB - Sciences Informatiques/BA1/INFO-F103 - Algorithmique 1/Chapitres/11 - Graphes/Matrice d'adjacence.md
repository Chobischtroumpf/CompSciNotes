---
title: Matrice d'adjacence
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Définition
> La matrice d’adjacence $M$ d’un graphe d’ordre $n$ est la matrice carrée $n \times n$:
>- $M_{i,j}$ est le nombre d’arêtes ayant les sommets $i$ et $j$;
>- $M_{i,j}$ est le nombre arcs du sommet $i$ vers le sommet $j$.
>- **Pour un graphe orienté d'ordre $n$**
> $$M_{i,j} = \begin{cases} 1 & \text{si } (i,j) \in A \\ 0 & \text{si } (i,j) \notin A \end{cases}$$
> - Pour un graphe pondéré:
> $$M_{i,j} = \begin{cases} \omega_{i,j} & \text{si } (i,j) \in A \\ 0 & \text{si } (i,j) \notin A \end{cases}$$

^17ebc9

>[!abstract]- Propriétés
>- Si $G$ est *non-orienté* alors $M$ est symétrique par rapport à sa diagonale;
>- Si $G$ a peu d’arêtes (arcs) alors cette représentation est coûteuse en espace mémoire (en $n^2$);
>- Le parcours complet de $M$ prend un temps $Θ(n^2)$.


## Exemples:
### Pour un graphe orienté

| ![[fd74fcf8468ad416c56e498f599ba6ec.png]] | ![[b10170e95cee14fec88e091b3d2ec988.png]] |
| :----------------------------------: | :----------------------------------: |
### Pour un graphe orienté pondéré
![[94a4d6685bc7b7e1f709c2782bd9882a.png]]
### Pour un graphe non-orienté d'ordre $n$
![[03bcb262a75e8836f1221a595fc89616.png]]
### Codage
- Tableau statique à deux dimensions de booléens;
- S’il y a peu d’arêtes, la liste d’adjacence est préférable à la matrice d’adjacence.
