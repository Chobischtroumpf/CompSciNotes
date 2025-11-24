---
title: Codage de Prüfer
authors: Alessandro Dorigo
tags:
  - MathDis
  - Complements
---


> [!info]+ Définition
> Le **codage de Prüfer** est une méthode pour décrire un [[Arbre (théorie des graphes)#^dcd789|arbre]] de $n$ sommets dont les sommets sont numérotés (arbre étiqueté) avec une suite $P = (x_1, x_2, x_3, \dots, x_{n-2})$ de $n - 2$ termes.
>
> Une suite $P$ donnée correspond à un et un seul arbre numéroté de $1$ à $n$.

> [!abstract]- Algo
> Pour $i = 1, \dots, n - 2$, trouver la plus petite feuille $v$ de l’arbre $T$ et écrire le numéro du voisin de cette feuille, ensuite effacer $v$ de $T$.
>
> ![[f89c3ebcb5f455e4d404ffc86db06936.png]]

> [!abstract]- Théorème 10.4.1
> Le nombre d’arbres $T$ ayant pour ensemble de sommets $[n] := \{1, 2, \dots, n\}$ est $n^{n-2}$.
>
> **Démonstration:**
> Le **codage de Prüfer** donne une bijection $C : \mathcal{A}_n \to [n]^{n-2}$ entre
>
> $$\mathcal{A}_n = \{T \mid T \ \text{arbre avec} \ V(T) = [n] \}$$
>
> et $[n]^{n-2}$, car il existe une fonction $D : [n]^{n-2} \to \mathcal{A}_n$ de decodage telle que
>
> $$D(C(T)) = T \quad \forall T \in \mathcal{A}_n \quad \text{et} \quad C(D(X)) = X \quad \forall X \in [n]^{n-2}$$

> [!abstract]- Théorème 10.4.2
> Soit $d = (d_1, d_2, \dots, d_n) \in \mathbb{N}_0^n$ un vecteur tel que $\sum d_i = 2n-2$. Le nombre d'arbres $T$ avec $V(T) = [n]$ et t.q. le $i$-ème sommet a degré $d_i$ est:
>
> $$\binom{n-2}{d_1-1, d_2-1, \dots, d_n-1}$$

> [!tip]+ Remarque
> Le coefficient multinomial est bien défini car
> $$\sum^n_{i=1} (d_i-1) = \sum^n_{i=1} d_i - n = 2n-2-n = n-2$$

> [!example]+ Exemple
> ![[84cb2820f9e21940137aac307ce138f1.png]]
>
> Le nombre d'arbres est
> $$\binom{6}{0,0,0,0,0,2,2,2} = \frac{6!}{2! \cdot 2! \cdot 2!} = \frac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2}{2 \cdot 2 \cdot 2} = 90$$
### Prüfer en Python
```python
def tree_to_prufer(Tree):
	prufer = []
	deg = {}
	# obtenir les degres de Tree
	for v in Tree: deg[v] = len(Tree[v])

	n = len(Tree)
	for i in range(0, n-2):
	# trouver la plus petite feuille dans Tree,
	# ecrire le numero du voisin, puis" effacer" la feuille
	for v in Tree:
		if deg[v] == 1:
			neighbor = [w for w in Tree[v] if deg[w] > 0]
			w = neighbor[0]
			deg[v] -= 1
			deg[w] -= 1
			prufer.append(w)
			break

	return prufer
```

```python
Tree = {1:[2], 2:[1,3,4,5], 3:[2], 4:[2,6], 5:[2], 6:[4]}
print(tree_to_prufer(Tree))
```

![[6eab75d6b677634ad1385ebe41232807.png]]
