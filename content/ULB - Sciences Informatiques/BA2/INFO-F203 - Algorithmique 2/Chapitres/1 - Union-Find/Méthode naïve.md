---
title: Méthode naïve
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!todo]+ Principe
> La **méthode naïve** utilise un tableau pour stocker directement l'identifiant de la classe de chaque élément.

> [!info]+ Complexité
> Le coût en nombre d'accès est toujours au moins égal au nombre $n$ d'éléments dans la structure.
## Implémentation
```java
public UF(int n) {
    count = n;
    id = new int[n];
    for (int i = 0; i < n; i++)
        id[i] = i;
}

public void union(int p, int q) {
    int pID = id[p];
    int qID = id[q];

    // p and q are already in the same component
    if (pID == qID) return;

    for (int i = 0; i < id.length; i++)
        if (id[i] == pID) id[i] = qID;
    count--;
}
```
