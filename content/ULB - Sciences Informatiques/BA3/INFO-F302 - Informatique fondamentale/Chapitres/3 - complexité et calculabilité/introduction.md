- théorie de la complexité
	- intérêt à la classification des problèmes selon leur complexité algorithmique 
	- de nombreuses classes de complexité ont été introduite 
		- dans une classe, on s'intéresse particulièrement aux prb les _plus difficiles_ (~complets pour la classe)
		- un prb complet pour une classe si ts les autres prb de la classe peuvent s'y réduire en temps polynomial 
		- → _borne inférieure_ sur leur complexité : pour résoudre un problème complet pour une classe $C$, on ne peut pas faire mieux que n'importe quel algo résolvant n'importe quel prb de $C$ (moins un polynôme pour la réduction)

##  notion de codage 
- _ex. comment représenter le problème suivant comme un langage
	- Entrée : graphe $G$ non dirigé et un entier $k \in \mathbb{N}$ 
	- Sortie : 1 ssi on peut colorier $G$ avec au plus $k$ couleurs 
	- → on voudrait rep ensemble $\set{(G_1,k_1), (G_2,k_2),...}$ de toutes les paires de graphes $G_i$ coloriables avec au plus $k_i$ couleurs
		- "coder" chaque paire comme un mot 
		- _ex. alphabet $\Sigma$ = {0,1,#,$} avec graphe $G$ 
			- chaque sommet = un entier
			- chaque arête $(i,j)$ avec le mot $\overline{i}$#$\overline{j}$ 
				- $\overline{i,j}$ : codages binaires des sommets $i,j$ 
- def prb = langage de mots : abstraite, utile en théorie de la calculabilité et complexité 
- → "oublier" codage et travail direct avec rep plus "concrètes"
	- _ex. matrice d'ajacence pour un grpahe ou liste de voisins_
- **! codage peut influencer la complexité**
```
- entrée : n naturel 
for i in range (2, floor(sqrt(n))) : 
	if n % i == 0 : 
		return 0
return 1 
``` 
→dépend du codage de n 