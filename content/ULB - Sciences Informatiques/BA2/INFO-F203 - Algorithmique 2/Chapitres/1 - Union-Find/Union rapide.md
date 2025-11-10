---
title: Union rapide
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!todo]+ Principe
> Cette méthode utilise une représentation en arbre où chaque élément pointe vers son parent, créant une structure arborescente pour représenter les classes d'équivalence.
### Structure
- La valeur `parent[p]` contenue à l'indice $p$ du tableau est celle d'un élément appartenant à la même classe d'équivalence que $p$
- On interprète `parent[p]` comme un pointeur vers une autre valeur dans le tableau
- La racine d'un arbre est un élément qui est son propre parent (`parent[p] = p`)
- L'identifiant d'une classe d'équivalence est la racine de son arbre

Pour procéder à l’union de deux classes, on trouve les racines `rootP` et `rootQ` des deux
éléments `p` et `q` en entrée, et on change la valeur de `parent[rootP]` en `rootQ`. On trans-
forme donc l’arbre représentant la classe contenant `p` en un sous-arbre de l’arbre contenant
`q`.
## Implémentation
```java
public int find(int p) {
    while (p != parent[p])
        p = parent[p];
    return p;
}

public void union(int p, int q) {
    int rootP = find(p);
    int rootQ = find(q);
    if (rootP == rootQ) return;
    parent[rootP] = rootQ;
    count--;
}
```

> [!tip]+ Remarque
> Le coût d'un appel à `find(p)` est proportionnel à la hauteur de l'arbre contenant `p`. Sans autre modification, dans le pire des cas, cette méthode peut être aussi inefficace que la méthode naïve.

> [!example]+ Représentation des classes d’équivalence en arbres
> ![[0c2bb579281d7940ac43011786cc62fd.png]]
> En haut, on a les nœuds, et en bas les nœuds vers lesquels ils pointent.
