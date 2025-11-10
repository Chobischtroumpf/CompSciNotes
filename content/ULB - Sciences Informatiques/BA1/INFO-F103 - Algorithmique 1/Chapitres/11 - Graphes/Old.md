---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

# 11: Graphes
## Définition
Un graphe $G=(S,A)$ est défini comme une structure composée de deux ensembles:
- Un ensemble $S$ de sommets (non vide);
- Un ensemble $A$ de paires de sommets $(i,j), \text{ où } i,j \in S$.

|         ![[Pasted image 20240424151953.png]]          | --------------------------------------------------------------------------------------------------------------------------- |
| :---------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------- |
| $S=\{a,b,c,d\} \ \ A =\{(a,b), (b,c), (c,b), (d,d)\}$ |                                                                                                                             |
|                                                       |                                                                                                                             |
### Implémentations d’un Graphe
- **Statique:** Matrice d'adjacence/incidence.
- **Dynamique:** Listes de successeurs.
## Termes Clés
- **Sommet:** Un point dans le graphe.
- **Arc:** Une connexion directionnelle entre deux sommets.
- **Arête:** Une connexion non directionnelle.
	- **Boucle:** Arête avec une seule extrémité reliant un sommet à lui-même.
### Relations entre Sommets
- **Père (Prédécesseur):** Sommet d'où vient un arc ou une arête.
- **Fils (Successeur):** Sommet vers lequel un arc ou une arête est dirigé.
- **Frère:** Deux sommets $i$ et $j$ qui sont des fils d’un même sommet $k$.

![[d17583203e5891a2f29169c1dd5509f0.png]]
## Types de Graphes
- **Orienté/Dirigé:** Les arcs ont une direction.
- **Non-orienté/Non-dirigé:** Les arêtes ne possèdent pas de direction spécifique.
- ![[Pasted image 20240424152422.png]]
- **Pondéré:** $G=(S, A, \omega)$ avec $\omega(i, j)$ étant le poids de l'arc ou de l'arête $(i, j)$.
- ![[Pasted image 20240424152841.png]]
- **Simple:** Pas de boucles ou d'arêtes multiples entre deux sommets.
- **Multiples:** Multiples arêtes entre deux sommets.
	- **$m$-graph**: Multi-graphe avec au plus $m$ arcs ou arêtes entre deux sommets.
- **Acyclique:** Ne contient aucun cycle.
	- Tout graphe acyclique a au plus $n-1$ arêtes (dont le fait que tout arbre a exactement $n-1$ arêtes).
- **Complet:** Chaque paire de sommets est connectée par une arête unique.
	- Un graphe complet est symétrique.
## Nombre Maximum d'Arêtes
- Graphes non-orientés de $n$ sommets:
$$m_{max}=\frac{n(n+1)}{2}$$
ou
$$m_{max} = \frac{n(n - 1)}{2} \text{ si G est en + simple}$$
- Graphes orientés:
$$m_{max}=n^2$$
## Ordre et Taille d'un Graphe
- **Ordre $|S|$:** Nombre de sommets.
- **Taille $|A|$:** Nombre d'arcs ou d'arêtes.

![[Pasted image 20240426105807.png]]
## Adjacence
- Deux sommets $i$ et $j$ sont adjacents si une arête ou un arc $(i, j)$ existe entre eux.
	- **Adjacence entre arcs/arêtes**: Deux arcs ou arêtes sont adjacents s'ils sont distincts et partagent au moins une extrémité commune.
## Degrés
- **Degré entrant $\deg^-(s)$:** Nombre d'arcs entrants vers le sommet $s$.
- **Degré sortant $\deg^+(s)$:** Nombre d'arcs sortants du sommet $s$.
- **Degré $\deg(s)$:** Pour les graphes non-orientés, nombre total d'arêtes incidentes à $s$.
	- **Graphe orienté:** Somme du degré entrant et du degré sortant de $s$.
$$\deg(s) = \deg^+(s) + \deg^-(s)$$
### Propriétés des Degrés
 - La somme des degrés sortants et entrants de tous les sommets $s \in S$ équivaut à la taille du graphe:
 $$\sum_{s \in S} \deg^+(s) + \sum_{s \in S} \deg^-(s) = m, \ m = |A|$$
 - Le nombre d’arêtes d’un graphe simple est égal à la demi-somme des degrés de ses sommets:
 $$\sum_{s \in S} \deg(s) = 2|A|$$
## Chaînes et Chemins
- **Chaîne:** Suite d'arêtes connectant une séquence de sommets.
	- La longueur correspond au nombre d'arêtes.
	- **Chaîne simple:** Ne contient pas une arête plus d'une fois.
	- **Chaîne élémentaire:** Ne contient pas un sommet plus d'une fois.
		- Toute chaîne élémentaire est simple, mais l'inverse n'est pas toujours vrai.
	- **Propriété:** Si deux sommets $s$ et $t$ sont reliés par une chaîne, alors il existe une chaîne élémentaire les reliant.

- **Chemin:** Suite d'arcs connectant une séquence de sommets.
	- La longueur est égale au nombre d'arcs.
		- Pour un chemin incluant $k$ sommets, la longueur est $k - 1$.
	- **Chemin simple**: Ne contient pas un arc plus d'une fois.
	- **Chemin élémentaire**: Ne passe pas plus d'une fois par chaque sommet.
#### Cycle et Circuit
- **Cycle:** Un chemin qui commence et termine au même sommet.
- **Circuit:** Un cycle dans un graphe orienté.
#### Types Spéciaux de Cycles et Chemins
- **Eulérien:** Visite chaque arête exactement une fois.
- **Hamiltonien:** Visite chaque sommet exactement une fois.
##
## Liste d'adjacence
### Pour un graphe orienté
- Tableau $T$ des successeurs pour chaque sommet:
	- `T[i]` pointe vers la liste chaînée des successeurs du sommet $i$;
	- Accès direct a un sommet via `T`;
	- Complexité spatiale: $O(|S| + |A|) = O(n + m)$.

| ![[6413c78e03355704cce9879012995158.png]] | ![[dd051faa24a55a7c00134687f3091301.png]] |
| :----------------------------------: | :----------------------------------: |
### Pour un graphe non-orienté
- Idem mais complexité spatiale: $O(|S| + 2|A|) = O(n + m)$
### Variante
#### Partager physiquement les sommets:
- Chaque sommet est représenté une et une seule fois;
- Chaque sommet possède une liste chaînée dont les éléments pointent vers ses successeurs.

| ![[Pasted image 20240501134317.png]] | ![[f0aa0164f2bfc222afa24d01506df2d4.png]] |
| :----------------------------------: | :----------------------------------: |
#### Matrice creuse:
![[5d30113adad7e5990a7f6e2716c8f220.png]]
- Chaque liste chaînée est remplacée par un tableau de taille $n + 1$, dont les premières cases contiennent les successeurs du sommet;
- Pour savoir combien de cases de ce tableau ”sont utiles”
	- **Utilisation d’une sentinelle:** Marquage de la fin de la liste des sommets par valeur spéciale, e.g., $−1$
	- ![[88a40ab0692af240b2eb3ea0f483e1a8.png]]
	- Stocker le **nombre de successeurs** $n_i$ dans la première case de chaque ligne $i$:
		- Chaque ligne `T[i]` contient une valeur `n_i = T[i][0]` dans sa première case
		- Les successeurs de i sont stockés dans les cases `T[i][1]`  à `T[i][n_i]`
	- ![[178a8612a06268d064edfc16bc69d38b.png]]
## ## Accessibilité
### Fermeture transitive d'un graphe
- La fermeture ou cloture transitive d'un graphe $G = (S,A)$ est le graphe $G^* = (S, A^*)$ ayant les memes sommets que $G$, et dont les arêtes ou arcs relient un sommet $i$ a un sommet $j$ s'il existe dans $G$ une chaîne ou un chemin allant de $i$ a $j$.

![[bfd51c96ab0a83e2814c749a92510e50.png]]

- Soit $M^*$ la matrice d'adjacence de $G^*$, alors on peut determiner si il existe un chemin entre deux sommets $i$ et $j$ si:
$$M^r_{ij} = \bigvee_{k=1}^n (M_{ik} \land M^{r-1}_{kj})$$
est vraie.
### Matrice d'accessibilité
- Une matrice $C$, booléenne, de taille $n \times n$ telle que $C_{i,j}$ indique si le sommet $j$ est accessible à partir du sommet $i$, donc, si il existe une chaîne ou un chemin reliant $i$ a $j$.

- La matrice d'accessibilité $C$ du graphe $G$ correspond à la matrice d'adjacence $M^*$ du graphe $G^*$ tel que:
$$C = M^* = M^0\ \lor\ M^1\ \lor\ M^2\ \lor\ ... = \bigvee_{r = 0}^{n - 1}M^r$$
*Note: si les chaines/chemins de longueur 0 sont aussi considérés, le résultat est la fermeture transitive et reflexive* $G^*$
![[c1f0ced085be4ffc77d30cd76a85f01a.png]]
## Algorithme de Roy-Warshall
- L'algorithme de Roy-Warshall nous permet, a partir de la matrice d'adjacence $M$ du graphe $G$, de trouver $C$.
- En partant de $C_0$, l'algorithme calcule une suite de matrices $C_k$ telles que
$$ \begin{cases} C_k[i][j] =1 & \text{s'il existe un chemin/chaîne (c/c) de } i \text{ à } j \text{ passant uniquement} \\ & \text{par des sommets inférieurs ou égaux à k} \\ C_k[i][j]=0 & \text{sinon} \end{cases}$$
### Construction de $C_k$
 - Il existe un chemin/chaîne de $i$ à $j$ passant seulement par des sommets inférieurs ou égaux à $k$ **si et seulement si:**
	 - Il existe un $c/c$ de $i$ à $j$ ne passant que par des sommets inférieurs ou égaux à $k − 1$.
		 - ou;
	 - Il existe un $c/c$ de $i$ à $k$ passant par des sommets inférieurs ou égaux à $k − 1$ et un $c/c$ de $k$ à $j$ passant par des sommets inférieurs ou égaux à $k − 1$

[[Chap 10 - slides_graphes_part1.pdf#Roy-Warshall]]
- La construction de la fermeture transitive par l’algorithme de Roy-Warshall a une complexité en $\Theta(n^3)$.
## Parcours d'un graphe
- **Parcours en profondeur:** *Depth-First Search (DFS)*
- **Parcours en largeur:** *Breadth-First Search (BFS)*

| ![[2a26cde91a1153aec73568569ce0143e.png]] |
| :----------------------------------: |
|     En rouge: DFS; En bleu: BFS      |
### Parcours en profondeur
- Le parcours en profondeur découvre les sommets du graphe en essayant toujours de descendre, en suivant les arcs ou les arêtes, le plus profondément dans le graphe.
	- À chaque fois, retour au dernier sommet pour lequel il reste encore des successeurs à visiter.
### Parcours en largeur
- Le parcours en largeur explore les sommets du graphe par niveau en découvrant:
	- D’abord les sommets à une distance $1$, en terme du nombre d’arcs ou d’arêtes, depuis le sommet de départ;
	- puis les sommets à distance $2$;
	- puis les sommets à distance $3$;
	- etc.

|  ![[ca8d76107d475902fa0abb9b7e3636ff.png]]   | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| :-------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
| Ordre DFS: 1, 2, 4, 5, 9, 6, 7, 8, 0, 3 |                                                                                                                                                    |
| Ordre BFS: 1, 2, 3, 4, 7, 5, 6, 8, 0, 9 |                                                                                                                                                    |

   - L'ordre d'exploration dépend aussi de l'ordre dans lequel on considère les fils d'un sommet (dépendant de l'implémentation)
   - À tout moment, classification des sommets en trois ensembles:
     1. L'ensemble des sommets déjà traités;
     2. L'ensemble des sommets frontaliers appelés aussi la frange (également appelé la frontière ou la bordure);
     3. L'ensemble des sommets encore inconnus.

| ![[40977ad0e12bb732c90c4a4ff134d85a.png]] | ------------------------------------------------------------------------ |
| :----------------------------------: | :----------------------------------------------------------------------: |

   - À chaque itération, nous sélectionnons un élément de la frange pour être traité et un certain nombre, $n$, d'éléments inconnus entrent dans la frange.
   - La manière de choisir les éléments de la frange qui seront traités détermine l'algorithme:
     - **DFS:** Sommet frontalier que l'on a rencontré en dernier.
     - **BFS:** Sommets frontaliers dans l'ordre dans lequel on les a rencontrés.
## Frange et parcours

|                              DFS                               |                             BFS                             |
| :------------------------------------------------------------: | :---------------------------------------------------------: |
|              ![[7c468f4020a2a68bf6112c32665549d1.png]]              |            ![[23e09c2575b7b723e1dbc9a98f9cd10d.png]]             |
| ![[b739e60636bea7c0309100d3acd0d1df.png]]<br>Frange = $\{5, 6, 3\}$ | ![[3cbbb7a44fb5e8d1045919a44344faaf.png]]<br>Frange = $\{4, 7\}$ |
## Structures de données pour les parcours de graphe
- **Parcours en profondeur (DFS): pile (stack)**
	- Les sommets parcourus sont insérés dans la pile (push)
	- Ensuite s'il n'y a pas de sommets, les sommets parcourus sont extraits de la pile (pop)
	- Discipline LIFO: Last In First Out

- **Parcours en largeur (BFS): file ou queue**
	- Parcourir tous les voisins d’un sommet en cours avant de visiter le sommet suivant qui sera le premier voisin à avoir été visité auparavant
	- Pour conserver les voisins d’un sommet en cours de visite que l’on visitera ultérieurement, on utilise une queue (= frange)
	- Discipline FIFO: First In First Out
## Codage
### DFS (récursif) - pseudo-code
```c
void DF(sommet s) {
	traiter s // traiter sommet s
	marque[s] = true // marquer s
	a = s -> 1er_arc

	while (a existe) { // si l’arc a existe
		traiter a // traiter arc a
		// si a -> extremite n est pas marquee
		if (marque[a -> extremite] == false)
			DF(a -> extremite)

		a = a -> arc_suivant
	}
}
```
- L’exploration progresse à partir d’un sommet $s$ en s’appelant récursivement pour chaque sommet voisin de $s$ (via liste d’adjacence)
### DFS (récursif + numérotation) - pseudo-code
```c
void DF(sommet s) {
	traiter s // traiter sommet s
	marque[s] = true // marquer s
	num += 1
	ordre[s] = num // numéroter sommet s
	a = s -> 1er_arc

	while (a existe) { // si l’arc a existe
		traiter a // traiter arc a

		if (marque[a -> extremite] == false)
			DF(a -> extremite)

		a = a->arc_suivant
	}
}
```
- Pour numéroter les sommets dans l’ordre de visite:
- On initialise une variable `num = 0`
	- On met à jour la variable `ordre[s]` d’un tableau indexé par les sommets de $G$ à chaque nouveau sommet visité $s$
### DFS (generalisé) - pseudo-code
```c
void DepthFirst(graphe G) {
	n = ordre de G
	// initialiser le tableau de booléens "marque"
	// (indexé par les sommets de G) a false
	for (s = 1; s <= n; ++s)
		marque[s] = false
		// Ensuite, pour tout sommet s de G
		for (s = 1; s <= n; ++s)
		// si le sommet s n’est pas marque
		if (marque[s] == false)
			DF(s)
}
```
### Complexité DFS
Soit le graphe $G$, d’ordre $n$ et de taille $m$, représenté par listes d’adjacence:
- Chaque sommet est paramètre de la procédure une et une seule fois donc il y a $n$ appels récursifs;
- À chaque sommet s visité, tous les sommets adjacents à $s$ sont testés pour le tableau marque en un temps proportionnel à $m$;
- L’algorithme demande donc un temps $Θ(n)$ pour les appels et un temps $Θ(m)$ pour les marques. Donc, $Θ(n + m)$.
### BFS (pseudo-code)
```c
void BF(sommet s) {
	Q = NULL
	traiter s
	marque[s] = true // marquer s
	enqueue(s, Q)

	while (Q != empty) { // Tant que la queue Q n'est pas vide
		s = dequeue(Q)
		a = s -> 1er_arc

		while (a existe) {
			traiter a
			s = a -> extremite

			if (marque[s] == false) {
				traiter s
				marque[s] = true // marquer s
				enqueue(s, Q)
			}

			a = a -> arc_suivant
		}
	}
}
```
### BFS (vecteur) - pseudo-code
```c
void BF() {
	num = 0
	val = (0, ..., 0)
	enqueue(1, Q)

	while (Q != empty) { // Tant que la queue Q n'est pas vide
		num += 1
		k = dequeue(Q)
		val[k] = num
		t = 1er successeur du sommet k

		while (t existe) {
			if (val[t] == 0) {
				enqueue(t, Q)
				val[t] -= 1
			}

			t = successeur suivant de t
		}
	}
}
```
### BFS (généralisé) - pseudo-code
```c
void BreadthFirst(graphe G) {
	n = ordre de G
	// initialiser le tableau de booléens "marque"
	// (indexé par les sommets de G) a false
	for (s = 1; s <= n; ++s)
		marque[s] = false
	// Ensuite, pour tout sommet s de G
	for (s = 1; s <= n; ++s)
	// si le sommet s n’est pas marque
		if (marque[s] == false)
			BF(s)
}
```
### Complexité BFS
- Chaque sommet voisin est inséré dans la file d'attente s'il n'est pas visité;
- Chaque sommet est inséré au plus une fois;
- Chaque sommet visité est marqué. Tous les sommets adjacents sont testés pour le tableau marque ce qui se fait globalement en un temps proportionnel à $m$;
- L'algorithme demande donc un temps $O(n)$ pour la boucle tant que et un temps $O(m)$ pour les marques;
- Donc, la complexité en temps est de l'ordre de $O(n + m)$.
## Algorithme de chemin de longueur minimale
- Soit $G = (S, A)$ graphe non-orienté, et une paire de sommets $(s, t) \in S \times S$:
	- On associe initialement au sommet $s$ l'index 0 et à tous les autres sommets l'index $∞$;
	- Tous les voisins de $s$ sont indexés par $1$, ce qui correspond à la distance de $s$ à chacun des sommets adjacents;
	- Puis à chaque sommet d'index $∞$ adjacent à un sommet d'index $1$ on associe l'index $2$;
	- Répéter jusqu'à ce que $t$ ait un index fini ou bien jusqu'à ce que tous les sommets d'index fini soient adjacents seulement à des sommets d'index fini.

```c
Moore(G, s, t) // s, t : sommets du graphe G
	index[s] = 0

	for (i = 1; i <= ordre du graphe; ++i)
	    if (i != s)
		    index[i] = infty

	enqueue(s, Q)

	while (Q != empty)
	    u = first(Q)
	    a = u -> 1er_arc

	    while (a existe)
	        i = a -> extremite // i adjacent au sommet u

	        if (index[i] = infty)
	            enqueue(i,Q)
	            index[i] = index[u] + 1, parent[i] = u

	        a = a -> arc_suivant

	    dequeue(Q)

	if (index[t] != infty)
		k = index[t], shortest[k] = t

	while (k != 0)
	    shortest[k - 1] = parent[shortest[k]]
	    k -= 1

	return [shortest[0], shortest[1], ..., shortest[k]]
```
### Algorithmes de chemins de poids minimal
#### Poids d'un chemin
- Le poids $\omega(P)$ d'un chemin $P := [(s_0,s_1), (s_1,s_2), ..., (s_{k-1},s_k))]$ est la somme des poids des arcs qui le constitue:
$$ \omega(P) = \sum_{i=1}^k\omega(s_{i-1},s_i)$$
#### Poids du chemin de poids minimal
- Le poids $d(s,t)$ du chemin du sommet $s$ a $t$ de poids minimal est défini par:
$$d(s,t) = \begin{cases} min\{\omega(P): P(s,t)\} & \text{s'il existe un chemin de s vers t} \\ \infty & \text{sinon} \end{cases}$$
- Le plus court chemin du sommet $s$ a $t$ est alors défini comme le chemin $P$ tel que $\omega(P) = d(s,t)$.
#### Lemme fondamental
Soit un graphe $G = (S,A)$ orienté et:
- Pondéré par une fonction $\omega : A \to \mathbb{R} : (i,) \to \omega(i,j)$;
- Un plus court chemin $P = [s_0,s_1,...,s_k]$ du sommet $s_0$ à $s_k$.

- **Si** pour tout $i,j$ tels que $0 \leq i \leq  j \leq  k$, $p_{ij}=[s_i, s_{i+1},..., s_j]$ définit le sous-chemin de $P$ allant du sommet $s_i$ à $s_j$.
	- Alors, $p_{ij}$ est un plus court chemin de $s_i$ a $s_j$
## Algorithme de Floyd-Warshall
- Calcule les distances des plus courts chemins/poids entre toutes les paires de sommets dans un graphe pondéré (sans cycles négatifs/absorbants).
- Ne renvoie pas les détails des chemins eux-mêmes.
	- Il faut donc reconstruire les plus courts chemins en utilisant une matrice $P$ de taille $n \times n$ dans laquelle $P_{i,j}$ sera le prédécesseur de $j$ dans un plus court chemin depuis $i$.

```C
Floyd-Warshall(M)
	for (i = 1; i <= ordre du graphe; ++i)
		for (j = 1; j <= ordre du graphe; ++j)
			if (i == j)
				D[i][j] = 0
			else if (M[i][j] == 0)
				D[i][j] = +infty
			else
				D[i][j] = M[i][j]
				P[i][j] = i // matrice des predecesseurs

	for (k = 1; k <= ordre du graphe; ++k)
		for (i = 1; i <= ordre du graphe; ++i)
			if (D[i][k] != +infty)
				if (D[i][k] + D[k][i] < 0) // cycle absorbant
					return
				else
					for (j = 1; j <= ordre du graphe; ++j)
						D[i][j] = min(D[i][j], D[i][k] + D[k][j])
						P[i][j] = P[k][j]

	return D
```

- L'algorithme de Floyd-Warshall fonctionne pour toute fonction de pondération $\omega$ en l'absence de **circuit absorbant**.

- Si l’ordre du graphe $\text{card}|S| = n$, la complexité en temps de cet algorithme est $\Theta(n^3)$ et sa complexité en espace $O(n^2)$.
	- Donc, complexité indépendante de la taille du graphe!
- **Interprétation:** $n^3 \gg n$ (ordre du graphe) mais $n^3 \ll n!$ (nombre de chemins possibles).
	- Exemple: si $n = 10$: $n^3 = 1000$, $n! = 3628800$.

- Lorsque le graphe contient un cycle ou **circuit absorbant**: un circuit pour lequel la somme des valeurs de ses arcs est strictement négative.
	- **Problème:** on peut arbitrairement diminuer le poids d’un chemin (no lower bound).

![[d64d1ef3c960d927b25af1d5ec532140.png]]
