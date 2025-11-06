---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

- **Principe général:** Résolution d'un problème par combinaison des solutions de ses sous-problèmes, similaire mais distincte du paradigme *Divide and Conquer* du fait que les sous-problèmes **peuvent se chevaucher**.
- **Utilité:** Efficace pour les problèmes avec chevauchement des sous-problèmes où stocker des solutions intermédiaires évite des recalculs inutiles, aussi appelé mémoïsation.
### Algorithmes en programmation dynamique:
- Shortest-path, Knapsack, Multiplication de chaînes matricielles, Fibonacci
## Approches de programmation dynamique:
### Approche descendante
- Décomposition du problème en sous-problèmes résolus par récursivité, avec mise en cache des résultats pour éviter des recalculs sur des entrées identiques.
### Approche ascendante (tabulation)
- Résolution itérative des sous-problèmes du plus petit au plus grand, stockage des résultats dans un tableau pour réutilisation directe.
#### Relation de récurrence
- Les relations de récurrence sont des expressions dont le n$^{\text{éme}}$ terme est défini par une combinaison de $k$ de ses termes précédents;
- Le nombre naturel $k$ détermine l’ordre de la récurrence.

|                         | Tabulation                                                              | Mémoïsation                                             |
| ----------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Méthode                 | Itérative                                                               | Récursive                                               |
| Parcours                | Bottom-up                                                               | Top-down                                                |
| Résolution              | Résolution de tous les<br>sous-problèmes                                | Résolution uniquement des<br>sous-problèmes nécessaires |
| Structure<br>de données | Table                                                                   | Dictionnaire (memo)                                     |
| Entrées                 | Toutes les entrées sont<br>insérées (une par une)                       | Les entrées sont<br>insérées à la demande               |
| Application             | Faible degré de recouvrement<br>(quantité de calculs redondants évités) | Haut degré de recouvrement                              |
## Mémoïsation
- Association d'un cache à une fonction pour stocker temporairement les résultats et éviter des recalculs sur les mêmes entrées.
- **Structure de donnée:** Souvent un dictionnaire ou une matrice.
- **Impact sur la complexité:** Réduit la complexité en temps au détriment d'une augmentation de la complexité spatiale.
	- Pour un problème $F$, le sous-problème $F_k, \ k < n$ ne sera pas recalculé si déjà calculé avant.
## Suite de Fibonacci
- La suite de Fibonacci est définie par la relation de récurrence:
$$F_n = \begin{cases} 0 & \text{si } n = 0 \\ 1 & \text{si } n = 1 \\ F_{n - 1} + F_{n - 2} & \text{si } n \geq 2  \end{cases}$$
[[Chap 11 - slides_prog_dynamique_part1.pdf#Fibonacci récursif]]

![[Pasted image 20240501155709.png]]

- La complexité en temps pour Fibonacci est définie comme:
$$\begin{align*}
T(n) &\geq 2 T(n - 2) \quad \quad \quad \ \ = 2^1 T(n - 2 \cdot 1) \\
&\geq 2 \times 2 T(n - 4) \quad \ \ \ = 2^2 T(n - 2\cdot 2) \\
&\geq 2 \times 2 \times 2 T(n - 6) = 2^3 T(n - 2\cdot 3) \\
&\vdots \\
&\geq 2^k T(n - 2\cdot k) \quad \ \ \ = \Omega(2^{n / 2})
&\end{align*}
$$
où chaque terme $T(n-2k)$ correspond au temps nécessaire pour calculer le $n-2k^{ème}$ terme de la suite de Fibonacci, et $k$ est approximativement égal à $\frac{n}{2}$ lorsque $n$ est suffisamment grand.
- Cette récurrence nous montre que la complexité croît de manière exponentielle, soit $\Omega(2^{n/2})$.
### Amélioration grace à l'approche descendante:
[[Chap 11 - slides_prog_dynamique_part1.pdf#Fibonacci memo descendant]]

- Un seul parcours de l’arbre d’appels (profondeur $n$), après retour du cas de base, en récupérant du mémo toutes les valeurs précédemment calculées (en $F(2)$ et $F(3)$);
- La complexité en temps de cette fonction avec mémoïsation est, en supposant des registres de $n$−bits pour chaque entrée de la structure de donnée memo:
$$T (n) = T (n − 1) + c = O(cn)$$
ou $c$ est le est le temps nécessaire pour insérer des nombres de $n$−bits, Donc:
$$T (n) = O(n^2)$$
### Amélioration grace à l'approche ascendante:
- Utilisation d'une boucle pour calculer chaque nombre de Fibonacci en sommant les deux précédents, avec les valeurs initiales de 0 et 1, de sorte à trouver le nombre à la position $n$ dans la suite.

![[Pasted image 20240501164007.png]]

```python
def fibonacci_ascending(n):
	# Base cases
	if n in {0, 1}:
		return n
	precedent, result = 0, 1
	for _ in range(2, n + 1):
		# Calcul du nombre de Fibonacci suivant
		# Sauvegarde du nombre precedent
		precedent, result = result, precedent + result
	return result
```
- Complexité en temps: $O(n)$
- Complexité en espace: $O(1)$
## Sous-structure optimale
### Propriété
- Un problème a une sous-structure optimale si la solution optimale peut être obtenue à partir des solutions optimales de ses sous-problèmes.
## Algorithme de Bellman-Ford
L'algorithme calcule:
- Le plus court chemin depuis un sommet fixé $s$ dans un graphe $G$ pondéré;
- Détecte la présence d'un circuit absorbant;
- Permet certains arcs de poids négatif pour détecter les circuits absorbants accessibles depuis le sommet source.
### Structure de donnée
- Tableau de distance $D$ du sommet $s$ aux autres sommets du graphe $G$, indexé par les sommets du graphe $G$;
- Liste des prédécesseurs $P$ (graphe orienté) ou liste des voisins (graphe non-orienté).
### Principe de fonctionnement
- Si les plus courts chemins entre $s$ et tous les prédécesseurs de $v$ sont connus:
	- Pour trouver le plus court chemin entre $s$ et $v$, additionner la distance du plus court chemin entre $s$ et $u$ à la distance de l'arc $(u,v)$ pour chaque prédécesseur $u$ de $v$.
- La plus petite somme donne le plus court chemin entre $s$ et $v$.

L'algorithme divisé en sous-problèmes:
- Soit $D_k[v]$ la distance d'un chemin allant de $s$ à $v$ et contenant au plus $k$ arcs.
$$
\begin{cases}
D_0[s] = 0 \text{ et } D_0[v] = +\infty \text{ pour } v \neq s \\
D_{k+1}[v] = \min \Bigl\{ D_k[v], \min_{(u,v) \in A}\{D_k[u] + \omega(u,v)\} \Bigl\}
\end{cases}
$$
L'algorithme calcule les valeurs $D_k[v]$ par valeur de $k$ croissante.
```C
Bellman-Ford(G = (S,A,w), s)
	for (int i = 1 ; i <= ordre du graphe G(|S|) ; ++i)
		D_0[i] = +infty

	int k = 0

	while (k < ordre du graphe G)
		D_k[s] = 0

		for (v in S)
			D_k+1[v] = min{D_k[v],min{D_k[u] + w(u,v) | (u,v) in A}}

		if (D_k+1 == D_k)
			STOP
		else
			k += 1

	if (k == |S|)
		return -1 // Detection du circuit absorbant
	// D = tableau des distances depuis s (plus courts chemins)
return D
```
### Fonctionnement de l'algorithme
- $D_0[v] =$ valeur d'un chemin de $s$ à $v$ de distance minimum et contenant 0 arcs;
- A la $k^{eme}$ itération de la boucle principale: $D_k[v] =$ valeur d’un chemin de $s$ à $v$ de distance minimale et ne contenant pas plus de $k$ arcs;
- Si pas de circuit absorbant:
    - Un plus court chemin élémentaire de $s$ à $v$ a moins de $n-1$ arcs;
    - $D$ se stabilise en moins de $n-1$ itérations à la valeur d’un plus court chemin de $s$ à $v$.

![[Pasted image 20240508154947.png]]
### Complexité
- **Temps**: $O(n)$, chaque valeur est calculée une seule fois
- **Espace**: $O(1)$, nombre fixe de variables utilisé quel que soit $n$
## Problème du sac à dos (Knapsack problem)
- On décide quels objets mettre dans un sac à dos pour maximiser le profit total sans dépasser la capacité $W$.
- On a un ensemble de $n$ objets, ou chaque objet $n_i$ contient $x_i$ instances, a un profit $p_i$ et un poids $w_i$.
### Cas 1: un seul objet de chaque type (0/1 knapsack)
- $x_i = 1$
#### Implémentation naïve
- Utilise un schéma de récursion simple qui calcule les mêmes sous-problèmes de manière répétitive.

![[Pasted image 20240515124816.png]]
- Formule:
	- Si $w \geq w_1$ alors on prend l'objet 1 $f_1(w) = p_1$
		Sinon $f_1(w)=0$
	- Pour un objet $j$:
	$$
	f_j(w)=
	\begin{cases}
	f_{j-1}(w) & \text{pour } w = 0,...,w_{j-1}\\
	max\{f_{j-1}(w), p_j + f_{j-1}(w -w_j)\} & \text{pour } w = w_j,..., W
	\end{cases}
	$$
- Profit optimal donné par $f_n(W)$

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack]]
#### Optimisation avec mémoization
- Utilise un tableau 2D `T` pour sauvegarder les résultats intermédiaires;
- Évite de recalculer les sous-problèmes déjà résolus en vérifiant `T[n][W]`:
	- Le calcul de chaque $f_j(w)$ implique d'examiner au plus $n$ éléments;
	- Il faut calculer au plus $W$ valeurs de $f_i(w)$.

- **Différence:**
	- Stocke les résultats intermédiaires dans une matrice pour éviter la redondance.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack Memo]]
#### Optimisation avec tabulation
- Construit un tableau `T[][]` de bas en haut;
- Utilise une approche itérative pour remplir le tableau `T`.

- **Différences:**
	- Remplit le tableau de manière ascendante (itérative) au lieu de récursive;
	- Évite complètement la récursion.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack Tab]]
#### Optimisation
- Utilise un tableau 1D `T` au lieu d'un tableau 2D;
- Remplit le tableau `T` en ordre décroissant pour éviter l'utilisation de deux tableaux.

- **Différences:**
	- Utilise un espace réduit (tableau 1D) pour stocker les résultats intermédiaires;
	- Traverse le tableau dans l'ordre inverse pour éviter les chevauchements.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack Tab v2]]
### Cas 2: une quantité illimitée de chaque type d’objet (unbounded knapsack)
- $x_i \in \mathbb{N}$
#### Implementation naïve
- Considère tous les sous-ensembles d'éléments dont le poids total est inférieur à $W$;
- Calcule le profit maximal en incluant ou non chaque élément de manière répétitive.

[[Chap 11 - slides_prog_dynamique_part1.pdf#UKP]]
#### Optimisation avec tabulation
- Utilise un tableau 1D `T` pour stocker les résultats intermédiaires;
- Remplit le tableau en considérant chaque élément plusieurs fois.

- **Différences:**
	- Utilise une approche itérative pour remplir un tableau 1D;
	- Évite la récursion en utilisant des boucles imbriquées.

[[Chap 11 - slides_prog_dynamique_part1.pdf#UKP v2]]

### Autres implémentations
#### Knapsack Récursif
- Utilise une classe pour encapsuler la logique;
- Détermine récursivement la valeur maximale en essayant d'ajouter chaque objet;
- Interagit avec l'utilisateur pour obtenir les volumes des objets.

- **Différences:**
	- Encapsulation de la logique dans une classe;
	- Interaction utilisateur pour obtenir les données d'entrée;
	- Ne stocke pas les résultats intermédiaires.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack Récursif]]
#### Knapsack Temp Saves
- Utilise une classe similaire à `Knapsack Récursif`;
- Stocke les résultats intermédiaires dans un dictionnaire `maxConnu`.

- **Différences:**
	- Utilise un dictionnaire pour mémoizer les résultats des sous-problèmes;
	- Réduit les recalculs en vérifiant `maxConnu` avant de poursuivre la récursion.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Knapsack Temp Saves]]

| Cas                | Implémentation         | Temps          | Espace                |
| ------------------ | ---------------------- | -------------- | --------------------- |
| 0/1 Knapsack       | Naïve                  | $O(2^n)$       | $O(n)$                |
|                    | Mémoization            | $O(n \cdot W)$ | $O(n \cdot W) + O(n)$ |
|                    | Tabulation             | $O(n \cdot W)$ | $O(n \cdot W)$        |
|                    | Tabulation (version 2) | $O(n \cdot W)$ | $O(W)$                |
| Unbounded Knapsack | Naïve                  | $O(2^n)$       | $O(W \cdot n)$        |
|                    | Tabulation             | $O(n \cdot W)$ | $O(W)$                |
## Longest Common Subsequence
- **Objectif:** Trouver la longueur de la sous-séquence commune la plus longue entre deux chaînes $C1$ et $C2$.
### Définition
- **LCS:** La sous-séquence la plus longue commune à toutes les séquences d’entrée données.
### Schéma de récursion pour LCS
- Générer toutes les sous-séquences possibles et trouver la plus longue présente dans les deux chaînes via la récursivité.
- En fonction de la relation entre les caractères non traités, appeler la fonction récursive.
### Implémentation naïve du schéma de récursion
- Utilise la récursivité pour explorer toutes les sous-séquences possibles;
- Compare les caractères des deux chaînes $C1$ et $C2$ en partant de la fin:
	- Si les caractères correspondent, augmente la longueur de la LCS;
	- Sinon, considère les sous-séquences en ignorant soit le dernier caractère de $C1$, soit le dernier caractère de $C2$.

[[Chap 11 - slides_prog_dynamique_part1.pdf#Implémentation naı̈ve du schéma de récursion]]
### Implémentation avec mémoization
- Utilise un tableau 2D `T` pour sauvegarder les résultats intermédiaires et éviter les recalculs;
- Initialisé à `-1`, indiquant que les valeurs n'ont pas encore été calculées.
- Lors d'un appel récursif, vérifie si le résultat est déjà calculé (`T[m][n] != -1`):
	- Si oui, retourne la valeur mémorisée;
	- Sinon, calcule la valeur et la stocke dans `T[m][n]`.

[[Chap 11 - slides_prog_dynamique_part1.pdf#LCS Memo]]
### Implémentation avec tabulation
- Initialise un tableau 2D `T` de dimensions $m+1$ par $n+1$;
- Le tableau est rempli de manière itérative en ordre ascendant;
- Après remplissage, traverse le tableau en ordre inverse pour reconstruire la LCS;
- La LCS est imprimée à partir des valeurs stockées dans le tableau.

[[Chap 11 - slides_prog_dynamique_part1.pdf#LCS Tab]]

| Implémentation         | Temps          | Espace         |
| ---------------------- | -------------- | -------------- |
| Naïve                  | $O(2^{m+n})$   | $O(1)$         |
| Mémoization            | $O(m \cdot n)$ | $O(m \cdot n)$ |
| Tabulation             | $O(m \cdot n)$ | $O(m \cdot n)$ |

## [[INFO-F103 - Algorithmique 1#Quicksort|Quicksort]]
- Un problems doit posséder deux attributs pour que la programmation dynamique soit avantageuse:
	- Une sous-structure optimale;
	- Des sous-problèmes qui se chevauchent.

- Si un problème peut être résolu en combinant des solutions optimales à des sous-problèmes qui ne se chevauchent pas, la stratégie est appelée ***Divide to conquer***.
- **Par conséquent:** le tri rapide *quicksort* (et le tri par fusion *mergesort*) ne sont (généralement) pas classés comme des problèmes de programmation dynamique.
