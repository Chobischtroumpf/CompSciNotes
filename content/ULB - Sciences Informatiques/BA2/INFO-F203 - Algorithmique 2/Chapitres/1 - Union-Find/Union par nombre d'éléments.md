---
title: Union par nombre d'éléments
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!info]
> Si, dans la **méthode d’union rapide**, on remplace la **hauteur** par le **nombre d’éléments** dans chaque sous-arbre, on obtient une **union par taille (union by size)** au lieu d’une **union par hauteur (union by rank)**.

Au lieu de comparer les **hauteurs** des arbres, on attache toujours l’arbre **contenant le plus petit nombre d’éléments** à la racine de l’arbre **contenant le plus grand nombre d’éléments**.
### Avantages par rapport à l’union par hauteur
1. Meilleur équilibrage en pratique:
    - L’union par **taille** a tendance à produire des arbres encore plus plats que l’union par **hauteur**, car la hauteur ne capture pas toujours la structure réelle de l’arbre.
2. Même complexité asymptotique;
3. Calcul plus simple:
    - La **hauteur** est une **propriété difficile à maintenir** efficacement car elle ne se met pas à jour de manière évidente lors des fusions;
    - Le **nombre d’éléments** est plus facile à maintenir car il suffit d’ajouter les tailles des deux ensembles fusionnés.
## Implémentation
```java
class UFSize {
    private int[] parent;
    private int[] size;  // Stocke le nombre d'éléments de chaque arbre

    public UnionFind(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;  // Chaque ensemble commence avec une taille de 1
        }
    }

    public int find(int p) {
        if (p != parent[p]) {
            parent[p] = find(parent[p]);  // Compression de chemin
        }
        return parent[p];
    }

    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);

        if (rootP == rootQ) return;

        // Attacher l'arbre le plus petit à l'arbre le plus grand
        if (size[rootP] < size[rootQ]) {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        } else {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        }
    }
}
```
