---
title: Coloriage des cartes
authors: Alessandro Dorigo
tags:
  -
---

- colorier chq région de telle sorte que deux régions ayant une frontière commune n'aient jamais la même couleur
	- but : minimiser le nb de couleurs
**exemple**
![[Pasted image 20251007163656.png]]
- pour cette carte, il faut minimum 3 couleurs

**remarque**
- lorsque régions pas discontinues (ie. région nécessairement en un seul morceau) → 4 couleurs suffisent toujours (_Théorème de 4 couleurs_)

## modélisation
- fixons un nb de couleurs et exprimons l'existence d'un coloriage avec 3 couleurs en logique propositionnelle
	- l'ensemble des régions : {1,2,3,4,5,6}
	- ensemble des couleurs: {R,V,B}
	- pour chq région $r$ et chq couleur $c$, nous introduisons la proposition $x_{r,c}$
	- → $X = \set{x_{r_c} | r \in \set{1,...,6}, c \in \set{R,V,B}}$
		- si interprétation $V$ trouvée par solveur SAT est telle que $V(x_{r,c} = 1)$
		- → chq région $r$ est coloriée avec la couleur $c$
### contraintes
-  expression contraintes : Voisines = {(1,2),(1,3),(2,4),(3,4),(4,5),(3,5),(5,6),(3,6)}
- exprimer que 1 et 2 ont deux couleurs différentes ?
	- $\neg\left((x_{1,V} \land x_{2,V}) \lor (x_{1,B} \land x_{2,B}) \lor (x_{1,R} \land x_{2,R})\right)$
	- $\equiv (\neg x_{1,V} \lor \neg x_{2,V}) \land (\neg x_{1,B} \lor \neg x_{2,B}) \land (\neg x_{1,R} \lor \neg x_{2,R})$
	- $\equiv \bigwedge_{c \in \{R, V, B\}} \neg x_{1,c} \lor \neg x_{2,c}$
- faire la même chose pour les autres voisins
- à la fin
	- $\phi = \bigwedge_{(i,j) \in \text{ Voisines }} \bigwedge_{c \in \set{R,V,B}} \neg x_{i,c} \vee \neg x_{j,c}$
