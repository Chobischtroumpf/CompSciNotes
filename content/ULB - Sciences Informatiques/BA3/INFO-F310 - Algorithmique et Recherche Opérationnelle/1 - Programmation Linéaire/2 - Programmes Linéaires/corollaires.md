## Corollaire 1
 - Si l'ensemble convexe $P$ correspondant à l'ensemble de contraintes $\set{Ax = b, | x \geq 0}$ est non vide
	 - → alors cet ensemble possède au moins un point extrème
- preuve
	- déduction de [[théorème fondamental de programmation linéaire]] et [[théorème d'équivalence]]

# Corollaire 2 (théorème)
- S'il existe une solution optimale finie à un problème de programmation linéaire
	- → alors il existe une solution optimale finie qui est un point extrême du polyèdre $P$ caractérisant l'ensemble de contraintes

- considérons $\max \set{c^T x : x \in P}$
	- $P = \set{x \in \mathbb{R}^n | a_i^T x \leq b_i, i = 1,...,m}$
	- Face $F$ (de $P) := \set{x \in P | a'^T x = b'}$
		- si $F$ une face de $P$
			- → $\dim (F) \leq \dim (P) - 1$
			- une face de dimension responsable 0, 1,..., k, dim(P) - 1 = responsable sommet, arête, k-face, facette
- _note : un point $x^*$ = point extrême de P $\leftrightarrow x^*$ est une face de dimension 0_

## analyse
- Sup que le problème $\max \set{c^Tx : x \in P}$ admet une solution optimale finie
- l'ensemble des solutions optimales $x^* = \max \set{c^T x : x \in P}$ définit une face non vide $F = \set{x \in P | a'^T x^* = b'}$ de $P$
- si le rang de  la matrice $A = n$
	- → alors $F$ contient une face de dimension 0
	- découle du théorème : si rang de $A$ est $n-k$ (ici $k = 0$), alors $P$ possède une face de dimension $k$ et ne contient aucune face de dimension inférieure
- Puisque un point $x^*$ est un point extrême de $P \leftrightarrow x^*$  est une face de dimension 0, il en résulte que $F$ contient un point extrême de $P$

# corollaire (finitude)
- l'ensemble de contraintes défini par $P = \set{x \in \mathbb{R}^n | Ax = b, x \geq 0}$ possède au moins au plus un nb fini de points extrêmes et chacun d'eux est fini

- preuve
	- il n'existe qu'un nb fini de solutions de base obtenues en sélectionnant $m$ vecteurs de base parmi les $n$ colonnes de la matrice $A$
	- les points extrêmes de $P$ définissent un sous-ensemble de ces solutions de base et doivent être finis
