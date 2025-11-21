# GRAPHCOLOR est $NP$-complet 
- démontrer que prb de coloriage de graphe avec $k$ couleurs est $NP$-complet
	- prb dans $NP$ en prenant solution candidate un coloriage → facile de vérifier en tps polynomial que cette solution est vaide 
	- montrer que GRAPHCOLOR est $NP$-dur : réduire problème 3SAT en tps polynomial dans GRAPHCOLOR
	- prouver existence d'un aglo, àpd $S$ de clauses avec 3 littéraux, crée en tps poly un graph $G$ et un entier $k$ tq $S$ satisfaisable $\Leftrightarrow G$ coloriable avec $k$ couleurs 
		- on prend $k =  0$ : couleurs = { 0,1, #}

## réduction de 3SATvers GRAPHCOLOR 
![[Pasted image 20251031130507.png]]
- coloriages
	- équivalents modulo permutation 
	- littéral et sa négation ne peuvent pas être colorié de la même couleur 
- → on supposera que le noeud central est toujours colorié par # 

**on le fait pour les n propositions**
![[Pasted image 20251031130717.png]]
**encodage d'une clause**
![[Pasted image 20251031130828.png]]
- "l'ilôt" $\neg x_1 \lor x_2 \lor x_n$ était séparé puis on l'a rattaché au graphe principale par le noeud coloré avec la couleur 1 
	- attaches avec tous les $x_i$ de l'ilot car relation entre eux trois (de ce que j'ai compris)

**on attache avec les $x_i$ des propositions et de là, on propose un coloriage**

![[Pasted image 20251031151524.png]]
→ il faut le faire pour toutes les clauses 
![[Pasted image 20251031151628.png]]
**démontrer la correction de la réduction**
- démontrer que 
	- toute interprétation qui satisfait $S$ donne un coloriage du graphe avec 3 couleurs
	- tout coloriage valide du graphe donne une interprétation qui satisfait $S$ 