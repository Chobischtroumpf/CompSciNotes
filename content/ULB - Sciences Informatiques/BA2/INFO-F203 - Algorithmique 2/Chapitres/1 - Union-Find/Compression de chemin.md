---
title: Compression de chemin
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!todo]+ Principe
> La **compression de chemin** est une optimisation supplémentaire qui vient s'ajouter à l'[[Union rapide pondérée|union rapide pondérée]]. L'idée est de raccourcir les chemins vers la racine à chaque fois qu'on les parcourt, rendant les opérations futures plus efficaces.

^a76fe1
### Logique
Lors de l'exécution de la méthode `find`, une fois qu'on a identifié la racine de l'arbre, on fait un second passage sur le chemin parcouru pour faire pointer chaque nœud directement vers la racine.

> [!tip]+ Remarque
> La compression de chemin ne modifie pas la racine des arbres, elle ne fait que réorganiser leur structure interne. La relation d'équivalence reste donc inchangée.
## Implémentation
```java
public int find(int p) {
    // Premier passage : trouver la racine
    int root = p;
    while (root != parent[root])
        root = parent[root];

    // Second passage : compression du chemin
    while (p != root) {
        int newp = parent[p];
        parent[p] = root;  // Faire pointer directement vers la racine
        p = newp;
    }
    return root;
}
```
## Implémentation récursive
```java
public int find(int p) {
    if (p != parent[p]) {
        parent[p] = find(parent[p]);  // Compression de chemin récursive
    }
    return parent[p];
}
```

> [!tip]+ Remarque
> La compression de chemin permet d'obtenir des arbres presque plats, où la plupart des nœuds pointent directement vers la racine. Cette structure quasiment plate permet d'avoir des opérations `find` très rapides en pratique.

> [!info]+ Complexité
> La complexité de $m$ opérations sur $n$ éléments dans la méthode d'[[Union rapide pondérée#^91229e|union rapide pondérée]] combinée à la compression de chemin est $\mathcal{O}(m\alpha(m,n))$, où $\alpha(m,n)$ est la [[Fonction d'Ackermann inverse#^7702a5|fonction d'Ackermann inverse]].

> [!example]+ Exemple
> Considérons un arbre où nous avons le chemin: 6 → 5 → 0 → 1
> Après un appel à `find(6)`, le chemin sera compressé et nous aurons: 6 → 1, 5 → 1, 0 → 1
> Tous les nœuds du chemin pointent maintenant directement vers la racine 1.
>
> ![[3b41664c6bda141c01fcbc83543a3cc9.png]]
