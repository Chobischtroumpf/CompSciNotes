#InfoFond 
# classe $P$ 
- classe $P$ = classe des problèmes pouvant être décidés en tmeps polynomial 
	- un prb $P \subseteq \Sigma^*$ est dans $P$ 
		- s'il existe un algo $A$ et une constante $k$ tq 
		- pour tout mot $u$ de longueur $n$ 
			- $A$ retourne 1 en temps $O(n^k) : u \in P$ 
			- $A$ retourne 0 en temps $O(n^k) : u \not \in P$ 
**exemples**
- décider si tableau est trié
- décider si un entier codé en unaire est premier (facile)
- décider si un entier codé en binaire est premier (difficile, prb resté ouvert pendant longtemps)