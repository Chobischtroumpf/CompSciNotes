# bin packing 

| objets | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| Poids  | 3   | 4   | 4   | 3   | 3   | 2   | 1   |
- sacs de 10kg
	- 3 sacs : {{1, 2},{3, 4, 5}, {6, 7}}
	- 2 sacs : {{1, 2, 4}, {3, 5, 6, 7}}

## Bin Packing est $NP$-complet
- Sup qu'on ait $k$ sacs de capacité $C$ 
	- BinPacking est dans $NP$ 
		- vérification en tps polynomial si une solution candidate
		- ie. assignation de chaque objet à un numéro de sac entre 1 et $k$, satisfait bien la contrainte de capacité
	- BinPacking $NP$-dur : démonstration avec réduction en tps polynomial du prb 2-partition (prb $NP$-complet)
		- instance de $2$-partition 
			- $n$ entiers $c_1,...,c_n$ 
			- $S \subseteq \set{1,...,n}$ tq $\sum_{i \in S}c_i = \sum_{i \not \in S}c_i$ ?
				- $S$ paire car sinon pas de solution 
		- réduction vers BinPacking 
			- si $C = S/2$, les obj $1,..,n$ de poids $c_1,...,C_n$ et $k = 2$ 
			- il y a une solution à $2$-partition $\Leftrightarrow$ il y en a une à l'instance de BinPacking ainsi construite
			- + on peut construire cette instance de BinPacking en tps polynomial (dans la taille de l'instance de $2$-partitions)
		- → BinPacking est donc $NP$-dur
