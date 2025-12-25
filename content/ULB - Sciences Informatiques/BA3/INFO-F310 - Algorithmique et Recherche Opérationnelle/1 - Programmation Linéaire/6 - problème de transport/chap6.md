# problème de transport 
- un produit doit être transporté de sources (usines) vers des destinations (dépôts, clients)
- objectif : déterminer la qtté envoyée de chq source à chq destination en minimisant des coûts de transport 
	- les coûts de transport sont prop aux qttés transportées 
- contraintes d'offre limitées aux sources et de demande à satisfaire aux destinations 
## variantes 
- modèle de tranport pas limité au transport de produits entre des sources et destinations géographiques 
### exemple pour variante : modèle de production 
- société fabrique sacs à dos 
	- demandes 
		- mars 100
		- avril 200
		- mai 180
		- juin 300
	- production 
		- mars 50
		- avril 180
		- mai 280
		- juin 270
	- demande peut-être satisfaite 
		- par prod du mois courant (40€/sac)
		- par prod d'un mois précédent (+0.5€/sac/mois pour le stockage)
		- par prod d'un mois suivant (+ 2€ / sac / mois de pénalité de retard)

#### correspondances avec le modèle de transport 

| transport                    | production - stocks                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| source $i$                   | période de prod $i$                                                                      |
| destination $j$              | période de demande $j$                                                                   |
| offre à la source $i$        | capacité de production à la période $i$                                                  |
| demande à la destination $j$ | demande pour la période $j$                                                              |
| coût de transport $i$ à $j$  | coût unitaire (prod + stock + pénalité) pour une prod en période $i$ pour la période $j$ |

## algo pour le problème de transport 
- basé sur l'algo du simplexe en tenant compte de la structure du prb 
	1. détermination d'une solution de base admissible 
	2. détermination de la variable entrant en base 
	3. détermination de la variable sortant de base 

### etape 1 : base admissible 

#### méthode : Coin Nord-Ouest
- partir du coin sup gauche du tableau 
	1. allouer le plus possible à la cellule courante et ajuster l'offre et la demande 
	2. se déplacer d'une cellule vers la droite (demande nulle) ou le bas (offre nulle)
	3. répéter jusqu'au moment où toute l'offre est allouée
	![[Pasted image 20251208175313.png]]

#### méthode : moindres coûts 
- sélectionner la cellule de coût de minimum 
	1. allouer le plus possible à la cellue courante et ajuster l'offre et la demande 
	2. sélectionner la cellule de coût minimum ayant une demande et une offre non nulles 
	3. répéter jusqu'au moment où toute l'offre est allouée
	![[Pasted image 20251208175608.png]]

## formulation 
### problème primal 
- $\min z = \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$
	- $\sum_{j=1}^n x_{ij} = a_i, i = 1:m$ 
	- $\sum_{i=1}^m x_{ij} = b_j, j=1:n$ 
	- $x_{ij} \geq 0, i = 1:m, j = 1:n$ 

### problème dual 
- $\max w = \sum_{i=1}^m a_iu_i + \sum_{j=1}^n b_jv_j$ 
	- $u_i + v_j \leq c_{ij}, i = 1:m, j = 1:n$ 

### adaptation du simplexe 
- critère d'optimalité 
	- $u_i +v_j - c_{ij} \leq 0$
- complémentarité
	- $x_{ij} \gt 0 \implies u_i + v_j - c_{ij} = 0$ 
- méthode 
	1. détermination des valeurs des variables duales (multiplicateurs)
	2. vérification du critère d'optimalité et détermination de la variable entrante 
	3. détermination de la variable sortante pour préserver l'admissibilité et pivotage 

#### étapes 
1. déterminer les "shadow prices" (coûts marginaux) pour chaque offre $u_i$ et chaque demande $v_j$ apd chq cellule utilisée (variable en base)
	- $y = c_B^T A_B^{-1} \implies y^TA_B=c_B^T \implies u_i + v_j = c_{ij}$ 
2. calculer les profits marginaux pour les cellules non-utilisées (variables hors base)
		$t_N^T = -(c^T_N - c_B^TA_B^{-1}A_N) = -(c_N^T-y^TA_B) \implies t_{ij} = (u_i + v_j) - c_{ij}$
	- si le profil marginal pour chq cellule inutilisée est négatif ou nul 
		- → STOP : solution OPTIMALE
3. Algo du cycle de réaction en chaîne 
	- selectionnez une cellule utilisée présente le profit marginal le plus élevé comme variable entrante 
	- màj les valeurs du nouvel ensemble de cellules utilisées (variable en base) en alternant ajout et retrait d'une même quantité ($\theta$)
4. retour étape 1	
[pour mieux comprendre](https://www.youtube.com/watch?v=tZ0cfYuSIuk)

#### étape 1 : détermination variables duales (multiplicateurs)
- système de $m+n-1$ équations à $m+n$ inconnues 
	- fixer $u_1 = 0$ 
- résoudre récursivement le système 
	- $\forall x_{ij} \gt 0 : u_i + v_j - c_{ij} = 0$ 
**exemple**
![[Pasted image 20251211141917.png]]

#### étape 2 
- vérification du critère d'optimalité ($u_i + v_j - c_{ij} \leq 0$) et détermination de la variable entrante 

**exemple**
![[Pasted image 20251211142129.png]]
#### étape 3 
- détermination de la variable sortante pour préserver admissibilité et pivotage 
	- objectifs 
		- ofre et demande doivent continuer à être satisfaites
		- qttés transportées doivent rester positives 
	- méthode
		1. construction d'un cycle parcourant des variables en base en partant de ET revenant à la variable entrante 
		2. déplacement le long de lignes et colonnes en alternant ajout et retrait d'une même quantité 
**exemple**
![[Pasted image 20251211142520.png]]

#### étapes 1 et 2
- mise à jour des valeurs $u_i,v_j$ 
- vérification du critère d'optimalité 
![[Pasted image 20251215161910.png]]

#### étape 3 
- oh la flemme 

### problème de transbordement 
- extension du modèle de transport
	- parfois nécessaire (ou moins cher) d'utiliser des noeuds intermédiaires pour le transport 
- 3 types de noeuds 
	- noeuds d'offre purs : arcs sortants uniquement 
		- → offre = offre originale 
	- noeuds de demande purs : arcs entrants uniquement
		- → demande = demande originale 
	- noeuds de transbordement : arcs entrants et sortants 
		- → offre / demande = offre/ demande originale + buffer
		- sources et destinations pour le problème de transport
- buffer : qtté nécessaire pour transporter toute la demande à travers le noeud de transbordement 
# exemples
## exemple d'intro 
- firme automobile 
	- 3 usines : LA(1000), Detroit(1500), New Orleans(1200)
		- capacités dans les parenthèses
	- 2 centres de distributions : Denver(2300), Miami (1400)
		- demandes  dans les parenthèses
	- coûts de transport : 

| usines / centres | Denver | Miami |
| ---------------- | ------ | ----- |
| LA               | 80     | 215   |
| Detroit          | 100    | 108   |
| New Orleans      | 102    | 68    |
- $\min z = 80x_{11} + 215x_{12} + 100x_{21} + 108x_{22} + 102x_{31} + 68x_{32}$
	- $x_{11} + x_{12} = 1000$
		- LA
	- $x_{21} + x_{22} = 1500$ 
		- Detroit
	- $x_{31} + x_{32} = 1200$ 
		- New Orleans 
	- $x_{11} + x_{21} + x_{31} = 2300$ 
		- Denver
	- $x_{12} + x_{22} + x_{32} = 1400$ 
		- Miami
	- $x_{11}, x_{12}, x_{21}, x_{22}, x_{31}, x_{32} \geq 0$ 
- interprétation 
	- $x_{ij}$ qtté déplacée de l'usine $i$ vers centre $j$ 
- propriétés
	- somme des offres = somme des demandes 
		- 1000 + 1500 + 1200 = 2300 + 1400
		- → modèle balancé (sinon non-balancé)

### représentation tableau : modèle non balancé 

| usine/centre | Denver | Miami | Offre |
| ------------ | ------ | ----- | ----- |
| LA           | 80     | 215   | 1000  |
|              | 1000   |       |       |
| Detroit      | 100    | 108   | 1300  |
|              | 1300   |       |       |
| New Orleans  | 102    | 68    | 1200  |
|              |        | 1200  |       |
| Artificial   | 0      | 0     | 200   |
|              |        | 200   |       |
| Demande      | 2300   | 1400  |       |
## exemple : problème de transport 
![[Pasted image 20251208181526.png]]
### étape 1 : base admissible
→ utilisation de la méthode moindre coûts
![[Pasted image 20251208181637.png]]
- sélection de celui qui a le moindre coût
- on soustrait l'offre de la ligne associée à la demande associée
![[Pasted image 20251208181701.png]]
- sélection du 2e moindre coût
- même chose + surplus de 5
![[Pasted image 20251208181743.png]]
- même chose + surplus de 10 par rapport à l'offre
![[Pasted image 20251208181755.png]]
- sélection pour la dernière colonne de la demande 
- → manque de 10 pour la demande
![[Pasted image 20251208181825.png]]
- ajout du dernier coût qui permet de réunifier les 10 manquant de la demande (en prenant le surplus de l'offre de la ligne associée)

## exemple : simplex transport 
![[Pasted image 20251215162131.png]]

### méthode du coin nord-ouest
- trouver une solution de base initiale admissible 
![[Pasted image 20251215162211.png]]

j'en ai marre frère 
