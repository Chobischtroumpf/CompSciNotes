## introduction 
- soient 
	- graphe dirigé $G = (V,A)$ 
		- $V$ : ensemble de sommets d'index $i=1:n$ 
		- $A$ : ensemble des arcs $(i,j): i→ j, i,j \in V$ 
	- une source $s \in V$ 
	- un puits $t \in V$ 
	- une capacité $\kappa_{ij} \gt 0$ pour tout arc $(i,j)$ 
	- → graphe pondéré $G = (V,A, \kappa)$ 

# définitions 
## flot maximum 
- le prb de flot maximal 
	- transporter la qtté maximale possible d'une origine à une destination données
		- sans dépasser les capacités $\kappa_{ij}$ des arcs $(i,j) \in A$ 
		- origine = source 
		- destination= puits 

## _st_-flot
- $f_{ij}$ : flot de l'arc (i,j)
- _st_-flot dans le graphe $G=(V,A)$
	- vecteur d'entiers $f= (f_{ij})$ associées aux arcs tq 
		- contrainte de capacité 
			- $\forall (i,j) \in A: 0 \leq f_{ij} \leq \kappa_{ij}$ 
		- contrainte de conservation 
			- $\forall i \in V\backslash \set{s,t} : \sum_{j:(i,j) \in A}f_{ij} = \sum_{j:(j,i) \in A}f_{ji}$ 
			-  $\forall i \in V\backslash \set{s,t} : \sum_{j:(i,j) \in A}f_{ij} - \sum_{j:(j,i) \in A}f_{ji} = 0$ 
	- ![[Pasted image 20251215164052.png]]
- valeur $v$ du flot $f$
	- flot entrant en le puits $t$ 
	- flot sortant en la source $f$ 
	- $v(f) = \sum_{j:(s,j) \in A}f_{sj} = \sum_{j:(j,t) \in A}f_{jt}$ 

## coupe 
- coupe $(S,T)$ dans le graphe $G=(V,A)$ 
	- déf par le sous-ensemble non vide de noeuds $S$ 
	- partition des sommets $V$ en $S$ et $V \backslash = T$ 
- ensemble des arcs sortant de $S$ 
	- dénoté par $\delta^+ (S)$ 
	- $\delta^+ (S) = \set{(i,j) \in A : i \in S, j \in T = V \backslash S}$ 
	- → donc $\delta^- (S) = \set{(j,i) \in A : i \in S, j \in V \backslash S}$ 

**capacité**
- capacité $c(S,T)$ d'une coupe $(S,T)$ 
	- somme des capacités de ses arcs 
	- $c(S,T) = \sum_{i \in S}\sum_{j \in T} \kappa_{ij}$ 

## _st_-Coupe
- _st_-coupe 
	- coupe qui sépare $s$ et $t$ 
	- coupe $(S,T)$ tq 
		- $s \in S$ 
		- $t \in V \backslash S$ 
- coupe minimale d'un réseau
	- coupe dont la capacité est minimale sur ttes les coupes du réseau
### exemples
![[Pasted image 20251215170227.png]]
### propriété
**exemple**
![[Pasted image 20251215170555.png]]
- coupe 
	- $S = \set{s,v_1,v_2}$ 
	- $T=  \set{v_3,v_4,t}$
	- capacité de la coupe 
		- $c(S,T) = 12+14=26$ 
		- $v_1→v_3$ : 12
		- $v_2 → v_4$ : 14
	- flot à travers la coupe 
		- $f(S,T) = 12 + 11 - 4 = 19$ 
		- $v_1 → v_3 : 12$ 
		- $v_2 → v_4 :  11$ 
		- $v_3 → v_2 : 4$ 
#### asymétrie 
- capacité $c(S,T)$ d'une coupe $(S,T)$ ne compte que les arcs allant du côté source $(s)$ de la coupe vers le côté puits $(t)$ de la coupe
- le flot $f(S,T)$ compte les arcs allant dans les deux sens à travers la coupe 
	- $f(S,T) = \sum_{i \in S} \sum_{j \in T} f_{ij} - \sum_{i \in S}\sum_{j \in T} f_{ji}$ 
#### lemme 
- soient 
	- $f$ un _st_-flot traversant le graphe $G$ depuis la source $s$ vers le puits  $t$ 
	- $(S,T)$ une coupe qlcq du graphe $G$ 
- → alors le flot $f(S,T)$ a travers la coupe $(S,T)$ vérifie
	-  $f(S,T) = \sum_{i \in S} \sum_{j \in T} f_{ij} - \sum_{i \in S}\sum_{j \in T} f_{ji} = v$ 

## dualité 
### dualité faible 
- capacité d'une _st_-coupe $c(S,T)$ (séparant $s$ de $t$)
	- supérieur ou égale à la valeur $v$ d'un _st_-flot $f$ admissible sur $G$ 
	- $v \leq c(S,T)$ 
	- → le flot entrant en $t$ ne peut être plus grand que le flot entrant en $T = V \backslash S$ 

### dualité forte 
- valeur $v$ d'un _st_-flot maximal
	- égale à la capacité $c(S,T)$ d'une _st_-coupe minimale
	- $v = c(S,T)$ 

## théorème de Ford-Fulkerson 
### théorème flot-max/coupe-min 
- pour 
	- tout graphe $G$ (orienté)
	- toute paire de sommets $(s,t) \in V \times V$ 
	- tout vecteur de capacités positives
- la valeur maximale du flot de $s$ à $t$
	- égale à la capacité d'une coupe minimale séparant $s$ de $t$ 

**conséquence**
- prb de flot maximal et de coupe minimale peuvent être formulés comme étant les versions primale et duale d'un même PL
	- flot maximal → primale 
	- coupe minimale → duale 

### théorème de Menger 
- source d'origine du théorème flot-max/coupe-min 
- soient 
	- G, une grpahe fini non-orienté 
	- $s,t$ deux sommets distincts 
- → le nb minimum d'arêtes à supprimer pour déconnecter $s$ et $t$
	- égal au nb max de chemins arête-disjoints de $G$ reliant $s$ et $t$ 
## formulation 

### problème de flot maximal 
**formulation**
- $\max v$ 
	-  $\forall i \in V\backslash \set{s,t} : \sum_{j:(i,j) \in A}f_{ij} - \sum_{j:(j,i) \in A}f_{ji} = \begin{cases} v, i = s \\ -v , i = t \\ 0 \end{cases}$
	- $(i,j) \in A : 0 \leq f_{ij} \leq \kappa_{ij}$ 

- data 
	- graphe pondéré $G = (V,A,\kappa)$ 
	- paire $(s,t) \in V \times V$ 
- solution réalisable 
	- _st_-flot admissible $f$ sur $G$ 
		- vérifiant les contraintes de capacités et de conservation
- solution optimale 
	- _st_-flot admissible $f$ 
		- dont $v$ est maximum 

## formulation du PL dual 
- flot sortant en $s$ 
	- pas plus grand que le flot sortant de S = V \ T
- flot entrant en $t$ 
	- pas plus grand que le flot entrant en T = V \ S

- $\max \sum_{j:(s,j) \in A}f_{sj}$ 
	- $\forall k \in V \backslash \set{s,t} : \sum_{j:(k,j) \in A}f_{kj} - \sum_{i:(i,k) \in A}f_{ik} = 0$
	- $\forall (i,j) \in A : f_{ij} \leq \kappa_{ij}$ 
	- $\forall (i,j) \in A: f_{ij} \geq 0$ 
#### variables duales 
$\forall (i,j) \in A : y_{ij} = \begin{cases} 1, i \in S \land j \in T \leftrightarrow (i,j) \in cut (S,T) \\ 0, sinon \end{cases}$ 
$\forall i \in V \backslash \set{s,t} : c_i = \begin{cases} 1, i \in S \\ 0, sinon \end{cases}$ 

#### problème dual 
- minimiser capacité totale des arcs compris dans coupe c(S,T)
- $\min \sum_{(i,j) \in} \kappa_{ij} y_{ik}$ 
	- $\forall (i,j) \in A, i \neq s, j \neq t: y_{ij} - c_i + c_j \geq 0$
		- pours les sommets $i,j$, si $i \in S$ et $j \in T$, alors l'arc $(i,j)$ est pris en compte dans la coupe $c(S,T)$ 
	- $\forall (s,j) \in A, j \neq t : y_{sj} + c_j \geq 1$
		- si $j\in T$ → l'arc (s,j) est pris en compte dans la coupe c(S,T)
	- $\forall (i,t) \in A, i \neq s : y_{it} - c_i \geq 0$ 
		- si $i \in S$ → l'arc (i,t) est pris en compte dans la coupe c(S,T)
	- $\forall (i,j) \in A : y_{ij} \geq 0$ 
	- $\forall i \in V \backslash \set{s,t} : c_i \in \mathbb{R}$ 

### formulation indicielle → matricielle (standard)
- soient 
	- un graphe orienté pondéré $G = (V,A, \kappa)$ 
	- un sommet source $s \in v$ 
	- un sommet destination $t \in V$ 
- la formulation du PL primal permettant de trouver un flot de $s$ à $t$ de valeur maximale est 
 - $\max v$ 
	-  $\forall i \in V\backslash \set{s,t} : \sum_{j:(i,j) \in A}f_{ij} - \sum_{j:(j,i) \in A}f_{ji} = \begin{cases} v, i = s \\ -v , i = t \\ 0 \end{cases}$
	- $(i,j) \in A : 0 \leq f_{ij} \leq \kappa_{ij}$ 
#### formulation matricielle
- $\max c^Tx$ 
	- $Ax \leq b$ 
	- $l \leq x \leq u$ 
- $x \in \mathbb{R}^n$: vecteur des variables de flot $x_k$ 
	- chaque arc $k$ est rep sous forme paire ordonnée de sommets 
	- $k = (i,j) \in V \times V$ 
- $c \in \mathbb{R}^n$ : vecteur du coût $c_k$ par unité de flot pour chaque arc $k = (i,j) \in A$ 
- $A$ : matrice d'incidence noeud-arc du graphe
	- node arc incidence matrix 
	- dimension $m \times n$ 
	- $A_{ik} = \begin{cases} 1, k = (i,k) \text{ starts at node} i → \text{ arc sortant +} \\  -1 , k=(j,i) \text{ ends at node }i → \text{ arc entrant -} \\0, sinon \end{cases}$ 
- $b \in \mathbb{R}^m$ : vecteur offre (+) / demande  (-)
	- condition d'équilibre : $1^Tb = 0$ 
- $l,u$ : respectivements bornes inf et sup de capacité pour chaque arc 

**exemple**
![[Pasted image 20251215182233.png]]
![[Pasted image 20251215182305.png]]
- m lignes (sommets)
- n colonnes (arcs)

- soit $x$ 
	- flot total entrant au sommet $i$ 
		- $\sum_{j:(j,i) \in A} A_{i,(j,i)}x_{(j,i)}$ 
	- flot total sortant du sommet $i$
		-  $\sum_{j:(i,j) \in A} A_{i,(i,j)}x_{(j,i)}$ 
	- ![[Pasted image 20251215182801.png]]
- pour sommet $3$ 
	- ![[Pasted image 20251215182857.png]]
	- flot total entrant 
		- $A_{32}x_2  + A_{33}x_3 + A_{34}x_4$ 
			- $=A_{32}x_{(1,3)} + A_{33}x_{(2,3)} + A_{34}x_{(4,3)}$ 
			- $=-x_{(1,3)}-x_{(2,3)}-x_{(4,3)}$ 
			- $\equiv -f_{13} - f_{23} - f_{43}$ 
	- flot total sortant 
		- $A_{35}x_5 + A_{36}x_6$ 
			- ...
			- $\equiv f_{35} + f_{36}$ 

- soit $b \in \mathbb{R}^m$ 
	- $b_i$ rep l'offre externe au noeud $i$ 
	- $b_i$ négatif rep la demande externe au noeud $i$ 
	- doit satisfaire $1^Tb = 0$ 
		- offre totale = demande totale 
	- ![[Pasted image 20251215183515.png]]

## algorithme de Ford-Fulkerson 
### arcs en avant / en arrière 
- soient 
	- $f$ un _st_-flot
	- $P$ un chemin non-dirigé/ non-orienté dans le graphe $G$ obtenu par remplacement de chq arc de $A$ par une arête 
- arc en avant de $P$ 
	- arc traversé dans $P$ dans son orientation originale
- arc en arrière de $P$ 
	- arc traversé dans $P$ dans l'autre sens 
### chemin augmentant 
- si
	- pour tout arc $a = (i,j)$ en avant de P : $f_{ij} \lt \kappa_{ij}$ 
		- orienté de s vers t 
	- pour tout arc $a = (i,j)$ en arrière de P : $f_{ji} \gt 0$ 
- alors 
	- P = chemin $f$-augmentant
### théorème : critère d'optimalité 
- un _st_-flot $f$ est maximal 
	- $\Leftrightarrow$ il n'existe pas de chemin $f$-augmentant
- → dans un graphe pondéré $G=(V,A,\kappa)$ muni d'un flot $g$ 
	- → il n'y a aucun chemin augmentant 
		- $\Leftrightarrow$ le flot est maximum
### graphe résiduel 
- soient 
	- graphe $G = (V,A,\kappa)$ 
		- avec fonction de pondération := capacité $\kappa : A \to \mathbb{N}$ 
	- une paire $(s,t) \in V \times V$ 
	- un flot $f$ réalisable
- graphe résiduel $H=(V,B,\kappa^f)$ 
	- avec fonction de pondération := capacité résiduelle 
		- $\kappa^f : B \to \mathbb{N}$ 
		- défini tq pour tout arc $(i,j) \in A(G)$ 
	- si $\kappa_{ij} - f_{ij} \gt 0$ 
		- → on ajoute dans $B(H)$ un arc $b=(i,j)$ de capacité résiduelle $\kappa^f_{ij} = \kappa_{ij}-f_{ij}$ 
	- si $f_{ij} \gt 0$ 
		- → on ajoute dans $B(H)$ un arc $b=(j,i)$ de capacité résiduelle $\kappa^f_{ji} = f_{ij}$

**exemple**
![[Pasted image 20251215184644.png]]
### méthode 
#### idée
- il existe un chemin augmentant $P$ de $s$ vers $t$ dans le graphe $G$ 
	- $\Leftrightarrow$ s'il existe un chemin de $s$ vers $t$ dans le graphe résiduel $h$ 
- lorsqu'un chemin augmentant $P$ est sélectionné dans le graphe résiduel $H$ 
	- chq arc dans $P$ qui correspond à un **arc en avant** dans $G$ 
		- augmente le flot en utilisant un arc ayant de la capacité dispo
	- chq arc dans $P$ qui correspond à un **arc en arrière** dans $G$ 
		- annule le flot qui a été écoulé vers l'avant
	- ![[Pasted image 20251215184644.png]]
	- ![[Pasted image 20251216153241.png]]

- méthode 
	- ne s'arrête que lorsqu'il n'y a plus de chemins dans le graphe résiduel $H$ 
		- pas dans graphe original $G$ 
	- est correcte car le graphe résiduel $H$ permet d'établir le critère d'optimalité 
		- càd calcule toujours un flot maximum

**Critère d'optimalité**
- étant donné 
	- un graphe $G = (V,A,\kappa)$ 
	- une paire $(s,t) \in V \times V$ 
- un flot $f$ est maximum dans $G$ 
	- s'il n'y a pas de chemin $s-t$ dans le graphe résiduel $H$

**idée algo**
- trouver un chemin augmentant et augmenter le flot sur ce chemin 
1. initialisation : $f=0$ 
	- flot nul sur tous les arcs est toujours admissible
2. alternance de deux phases 
	1. phase de marquage : recherche d'un chemin augmentant 
	2. phase d'augmentation : augmenter le flot sur le chemin trouvé en phase de marquage
3. répétition des deux phases jusqu'il n'y a plus de chemin augmentant 
#### phase de marquage 
- input 
	- graphe $G=(V,A,\kappa)$ 
	- paire $(s,t) \in V \times V$ 
	- ensemble $L = \emptyset$ 
1. marquer $s$ par $[0,\infty]$ 
	1. + ajouter $s$ dans $L$ : $L =\set{s}$ 
2. tant que $L \neq \emptyset$ et $t$ non marqué 
	1. sélectionner un sommet $i$ dans $L$ et le retirer de $L$ 
		1. $L = L \backslash \set{i}$ 
	2. pour tout sommet $j$ non marqué tq $(i,j) \in A$ et $f_{ij} \lt \kappa_{ij}$ 
		1. marquer $j$ par $[i,\alpha_j]$ 
			1. $\alpha_j = \min (\alpha_j, \kappa_{ij} - f_{ij})$ 
		2. ajouter $j$ dans $L$ 
			1. $L = L \cup \set{j}$ 
	3. Pour tout sommet $j$ non marqué tq $(j,i) \in A$ et $f_{ji} \gt 0$ 
		1. marquer $j$ par $[i,\alpha_j]$ 
			1. $\alpha_j = \min(\alpha_i,f_{ji})$ 
		2. ajouter $j$ dans $L$ 
			1. $L = L \cup \set{j}$
3. si $t$ est marqué, STOP
	1. plus de chemin augmentant
#### phase d'augmentation
1. commencer avec $j=t$ 
2. tant que $j \neq s$ 
	1. Soit $[i,\alpha_j]$ la marque de $j$ 
		1. si arc $(i,j)$ est en avant (_de s vers t_) dans $G$ 
			1. → $f_{ij} = f_{ij} + \alpha_t$ 
		2. si arc $(i,j)$ est en arrière (_de t vers s_) dans $G$ 
			1. → $f_{ji} = f_{ji} - \alpha_t$ 
	2. $j=i$ 

### complexité 
- phase de marquage : $O(|V|+ |A|)$ 
	- suppression des marques : $O(|V|)$ 
	- examen de tous les successeurs et tous les prédécesseurs :$O(|A|)$
- phase d'augmentation :$O(|V|)$ 
- A chq itération, on augmente le flot d'une unité au moins 
- si la valeur de ce flot max = $F$ 
	- complexité maximale totale est 
		- $O(F(|V|+|V|+|A|)) = O(F(|V| + |A|))$
		- → complexité pseudo-polynomiale

### exemple 
![[Pasted image 20251216154651.png]]

#### phase de marquage 1/initialisation
![[Pasted image 20251216154737.png]]
- $L = \set{1,2,3,4,5}$ 
	- $2 : \alpha_2= min(\infty,20)$ 
	- $3 : \alpha_3 =\min(\infty,30)$ 
	- $4 : \alpha_4= \min(\infty, 10)$ 
	- $5 : \alpha_5=\min(10, 20)$ 

#### phase d'augmentation 1
![[Pasted image 20251216155036.png]]
- on choisit le chemin $1 → 4 → 5$ 
	- $f_{45} = 0 + \alpha_5$ 
	- $f_{14} = 0 + \alpha_5$ 
#### phase de marquage 2 
![[Pasted image 20251216155057.png]]
- $L = \set{1,2,3,5}$ 
	- $4 : \alpha_4 = \min(10, 10)$ 
	- $5 : \alpha_5 = \min(10, 30 - 10) = 20$ 

#### phase d'augmentation 2
![[Pasted image 20251216155122.png]]
- chemin $1 → 2 → 5$ 
	- $f_{12} = 0 +\alpha_5$ 
	- $f_{25} = 0 + \alpha_5$ 

#### phase de marquage 3
![[Pasted image 20251216155137.png]]
- $L = \set{1,3,5}$ 
	- $5 : \alpha_5 = \min(30, 20-0)$ 
 
#### phase d'augmentation 3
![[Pasted image 20251216155157.png]]
- chemin $1 → 3 → 5$ 
	- $f_{35} = 0 + \alpha_5$ 
	- $f_{13} = 0 + \alpha_5$  

#### phase de marquage 4
![[Pasted image 20251216155214.png]]
- $L = \set{1,3,4,5}$ car il y a encore de la capacité
	- $3 : \alpha_3 = \min(30, 30 - 20)$ 
	- $5 : \alpha_5 = \min(20, 20 - 10)$ 

#### phase d'augmentation 4
![[Pasted image 20251216155234.png]]
- chemin $1 → 3 → 4 → 5$ 
	- $f_{45} = 10 + \alpha_5$
	- $f_{34} = 0 + \alpha_5$
	- $f_{13} = 20 + \alpha_5$ 

#### phase de marquage 5
![[Pasted image 20251216155309.png]]
- STOP 
	- plus de capacité sur les arcs sortant de $s$ µ

#### final
![[Pasted image 20251216163259.png]]
- les noeuds marqués à la dernière itération définissent la coupe minimale 

## algorithme d'Edmonds Karp 
- algo similaire à l'algo de Ford-Fulkerson
	- !!! ordre de recherche utilisé pour déterminer un chemin augmentant 
- chemin trouvé dans le graphe résiduel $H$ 
	- plus court chemin (en nb d'arcs) 
	- possède la capacité de saturation la plus grande 
		- → posisble d'éliminer les arcs saturés à l'itération suivante 
- → algo Edmonds-Karp ~ "shortest augmenting (fatest) path"

- Attention 
	- BFS avec prédécesseurs → obtenir le chemin spatial de $s → t$ 
	- + appliquer la règle 
		- $f(s,t) = \min \set{\kappa_f(s,i), \kappa_f(i,j), \kappa_f(j,t)}$ 

### lemme 
- si l'algo d'Edmonds-Karp est exécuté avec
	- graphe pondéré $G = (V,A,\kappa)$ 
	- $(s,t) \in V \times V$ 
- → alors pour tout sommet $i \in V \backslash \set{s,t}$ 
	- la distance la plus courte dans le grpahe résiduel $H = G_f$ croit de manière monotone avec l'augmentation de la valeur du flot $f$ 

**méthode**
- un tel chemin peut être trouvé par un BFS dans le grpahe résiduel $H$ 
	- supp que les arcs ont tous une longueur unitaire 

### propriétés
- complexité : $O(|V||A|^2)$ 
	- chq chemin augmentant peut être trouvé en temps $O(|A|)$ 
		- avec BFS dans le graohe résiduel $H$ 
	- à chq itération : au moins un arc de $A$ arrive à une saturation 
		- capacité résiduelle nulle 
	- la distance de la source à un arc saturé par le chemin augmentant croît à chq fois que l'arc est saturé 
		- et que cette longueur est au plus $|V|$ 
	- → complexité indépendante de la valeur du flot max $F$ 
- complexité n'impose pas de fonction de pondération entière pour la capacité $\kappa$ des arcs du graphe $G = (V,A,\kappa)$ 
- longueur du plus court chemin augmentant est croissante 
### exemple 
![[Pasted image 20251216164129.png]]
![[Pasted image 20251216164144.png]]![[Pasted image 20251216164207.png]]

## théorème du flot entier 
- idée 
	- si chq capacité des arcs du grpahe est un entier 
		- → taille du flot maximal est un entier 
		- → il existe un flot max tq le flot ) chq arête soit également un entier 
	- → méthode de Ford-Fulkerson permet de trouver un tel flot 

- Si ttes les capacités d'un graphe sont des entiers 
	- → le graphe a un flot maximal entier 
- càd qu'il existe un flot maximal $f$ tq pour tout arc $(i,j)$, le flot $f_{ij}$ est un entier