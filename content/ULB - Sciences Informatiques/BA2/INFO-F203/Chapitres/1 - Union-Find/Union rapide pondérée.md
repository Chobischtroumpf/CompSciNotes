---
title: Union rapide pondérée
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!todo]+ Principe
> Cette amélioration de l'[[Union rapide|union rapide]] introduit une stratégie pour maintenir des arbres équilibrés. Lors d'une union, nous avons le choix entre attacher l'arbre de `p` à la racine de l'arbre de `q` ou l'inverse. La méthode pondérée exploite cette liberté pour minimiser systématiquement la hauteur des arbres résultants.

^91229e

### Logique
Nous conservons dans un tableau `height[]` la hauteur de chaque arbre. Lors d'une union:
- Si un arbre est plus petit que l'autre, nous l'attachons à la racine du plus grand
- Si les arbres ont la même hauteur, nous choisissons arbitrairement et incrémentons la hauteur de l'arbre résultant
## Implémentation
```java
public void union(int p, int q) {
    int i = find(p);
    int j = find(q);
    if (i == j) return;

    // Attache l'arbre le plus court à la racine du plus grand
    if (height[i] < height[j]) {
        parent[i] = j;
    } else if (height[i] > height[j]) {
        parent[j] = i;
    } else {
        parent[j] = i;
        height[i]++;
    }
    count--;
}
```

> [!abstract]- Théorème
> La hauteur d'un arbre dans la forêt construite par la procédure d'union rapide pondérée pour $n$ éléments est au plus $\log_2 n$.
>
> **Démonstration**:
> Nous procédons par induction pour prouver qu'un arbre de hauteur $h$ contient au moins $2^h$ éléments.
>
> 1. **Base de l'induction**:
>     - À l'initialisation, chaque arbre de hauteur 0 contient 1 = $2^0$ élément
>     - La propriété est donc vraie initialement
>
> 2. **Étape d'induction**:
>     - Soient deux arbres de hauteurs respectives $h_1$ et $h_2$ contenant respectivement $n_1 \geq 2^{h_1}$ et $n_2 \geq 2^{h_2}$ éléments;
>     - Supposons sans perte de généralité que $h_1 \leq h_2$;
>     - Lors de leur union, l'arbre de hauteur $h_1$ est attaché à celui de hauteur $h_2$;
>         - Si la hauteur **finale** est $h_2$, la propriété reste **évidemment vraie**;
>         - Si la hauteur devient $h_2 + 1$, cela signifie que $h_1 = h_2$;
> 	- Le nouvel arbre contient alors $n_1 + n_2 \geq 2^{h_1} + 2^{h_2} = 2 \cdot 2^{h_2} = 2^{h_2+1}$ éléments.
>
> 3. **Conclusion**:
>     - Pour un arbre de hauteur $h$ contenant $n$ éléments, nous avons $n \geq 2^h$
>     - Donc $h \leq \log_2 n$

> [!abstract]- Corollaire
> La complexité de chacune des opérations dans la méthode d’union rapide pondérée pour $n$ éléments est $\mathcal{O}(\log n)$.

> [!tip]+ Remarque
> Cette borne logarithmique représente une amélioration exponentielle par rapport à la méthode naïve, qui pouvait créer des arbres de hauteur linéaire.
