---
title: INFO-F302 - Informatique fondamentale
authors: Alessandro Dorigo
tags:
  - ULB
  - BA3
  - InfoFond
  - Maths
---
[[Définitions à mémoriser]]

# Chapitre 0: Introduction
- [[Théorème d'Incomplétude de Gödel]]
- [[Informatique Fondamentale]]
	- [[Automate]]
		- [[Machine de Turing]]
	- [[Chaîne de Markov]]
	- [[Système de Déduction]]
- [[Théorie de la Complexité]]
	- [[Problème Complet]]
- [[Réductions entre Problèmes]]
- [[Problème 2-partition]]
- [[Problème Bin Packing]]

# Chapitre 1: La Logique Propositionnelle

### Introduction, syntaxe, sémantique, satisfaisabilité, validité
- [[Formalisation Logique]]
- [[Bachus-Naur Form]]
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/1 - La Logique Propositionnelle/Introduction, Syntaxe, Sémantique, Satisfaisabilité, Validité/Règles de Précédence]]
- [[Fonction d'Interprétation]]
- [[Validité]]
- [[Satisfaisabilité]]

### Tableaux Sémantiques
- [[Sémantique]]
	- [[Tableau Sémantique]]
	- [[Règles de Simplification]]

### Déduction Naturelle
- [[Déduction Naturelle]]
- [[Conjonction]]
- [[Double Négation]]
- [[Modus Tollens (Contraposition)]]
- [[Les Règles de Déduction Naturelle]]
- [[Équivalence]]

# Chapitre 2: Problème SAT

### Littéraux et Clauses
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problème SAT/littéraux et clauses/définitions|définitions]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problème SAT/littéraux et clauses/définitions#clause|clause]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problème SAT/littéraux et clauses/définitions#satisfaction d'ensemble de clauses|satisfaction d'ensemble de clauses]]
- [[formes normales]]
	- [[formes normales#forme normale conjonctive (FNC)|forme normale conjonctive]]
	- [[formes normales#forme normale conjonctive (FND)|forme normale conjonctive]]
	- [[formes normales#mise sous FNC et FND|mise sous FNC et FND]]
- [[lien avec SAT]]

### Problème SAT
- [[Problème SAT#définition prb SAT|définition problème SAT]]
	- [[Problème SAT#complexité du prb SAT|complexité du prb SAT]]
- [[Notations]]
	- [[Notations#disjonction|grande disjonction]]
	- [[Notations#conjonction|grande conjonction]]

### Modélisation
- [[Coloriage des cartes]]
- [[Problème des 8 reines]]
- [[jeu Sudoku]]
- [[Problème de pavage]]

### Algo DPLL
- definitions
	- [[interprétation partielle]]
		- [[interprétation partielle#simplification sous une interprétation partielle|simplification sous interprétation partielle]]
- [[Algo DPLL]]
	- [[Algo DPLL#proposition pivot|proposition pivot]]
		- [[Algo DPLL#premier critère de choix clauses unitaires|clauses unitaires]]
		- [[Algo DPLL#deuxième critère de choix proposition à polarité unique|proposition à la polarité unique]]
	- [[Algo DPLL#pseudo code|pseudocode]]

### Transformation de Tseitin
-  [[transformation de Tseitin]]
- [[variantes SAT]]
	- [[variantes SAT#2SAT|2-SAT]]
	- [[variantes SAT#QSAT|QSAT]]
	- [[variantes SAT#WEIGHTED-MAX-SAT|WEIGHTED-MAX-SAT]]
		- [[variantes SAT#MAX-SAT|MAX-SAT]]

# Chapitre 3: Classes P et NP
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/3 - Complexité et Calculabilité/Introduction|Introduction]]
- problème
	- [[Problème de Décision]]
	-  [[Problème d'Optimisation]]
	- [[Problème Indécidable]]
		-  [[Problème Indécidable#exemple problème de l'arrêt|problème de l'arrêt]]
			-  [[Problème Indécidable#problème de la correspondance de Post|problème de la correspondance de Post]]
		- [[Problème Indécidable#autres problèmes indécidables|autres exemples]]
- algorithmes
	-  [[Algorithme de Décision]]
	-  [[Algorithme de Vérification]]
- classes
	- [[Classe P]]
	-  [[Classe NP]]
		-  [[Classe NP#$NP subseteq$ ExpTime|$NP \subseteq Exptime$]]
		-  [[Classe NP#$NP$- dur ou $NP$-difficiles|NP-dur]]
	- [[Autres Classes]]
- preuves
	- [[Conjecture P ≠ NP]]
	- démontrer qu'un prb est NP-complet
		-  [[Composition de Réduction]]
		-  [[Théorème de la Réduction]]
		-  [[Conséquence de la Complétude]]
- exercices
	- [[Bin Packing est NP-Complet]]
	-  [[GraphColor est NP-Complet]]
		- [[GraphColor est NP-Complet#réduction de 3SATvers GRAPHCOLOR|réduction 3SAT vers GRAPHCOLOR]]
	-  [[Démonstration Problème Indécidable]]

# Chapitre 4: Automates Finis
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - Automates Finis/introduction|introduction]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - Automates Finis/introduction#exemples|exemples]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - Automates Finis/introduction#applications possibles|applications possibles]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - Automates Finis/introduction#avantages/inconvénients des automates|avantages / inconvénients]]
- définitions
	-  [[language]]
		- [[language#langage accepté ou reconnu|language accepté ou reconnu]]
			- [[language#langage accepté pour AFN|pour un automate non déterministe]]
	- [[facteur]]
	-  [[automate fini]]
		-  [[exécution]]
		- [[état atteignable]]
	- [[automate non-déterministe]]
		- [[exécution#exécution pour AFN|exécution]]
		-  [[automate non-déterministe#AF vs AFN|AF vs AFN]]
	- [[expression rationnelle]]
		- [[expression rationnelle#exemple|exemple]]
- résultats
	- [[complétion d'un automate]]
		- [[complétion d'un automate#lemme|lemme]]
	-  [[problème du VIDE]]
	- [[état atteignable#théorème|théorème des états atteignables]]
	- [[arbre des exécutions]]
		- [[arbre des exécutions#test d'appartenance au langage|test d'appartenance au langage]]
		- [[arbre des exécutions#algorithme|algorithme]]
		- [[arbre des exécutions#lemme|lemme]]
		- [[arbre des exécutions#théorème|théorème 1]]
			- [[arbre des exécutions#exemple|exemple]]
		- [[arbre des exécutions#théorème|théorème 2]]
	- [[théorème - lien entre AF et AFN]]
		- [[théorème - lien entre AF et AFN#preuve|preuve]]
		- [[théorème - lien entre AF et AFN#complexité|complexité]]
	-  [[théorème de Kleene|théorème de Kleene : lien entre AF et expression rationnelle]]
		- [[théorème de Kleene#preuve|preuve ]]
			- [[théorème de Kleene#dans le cas $E = F+G$|cas 1]]
			- [[théorème de Kleene#dans le cas $E = F cdot G$|cas 2]]
				-  [[théorème de Kleene#cas problématique|cas problématique]]
			- [[théorème de Kleene#cas $E = G *$|cas3]]
	- [[théorème construction d'un langage|théorème sur la construction d'une union d'un langage tricky]]
- opérations booléennes sur les langages
	- [[complément]]
	- [[union, intersection]]
		-  [[union, intersection#théorème|théorème]]
	- [[produit d'automates]]
		-  [[produit d'automates#cloture par union et intersection|clotûre par union et intersection]]
	-  [[inclusion et équivalence]]
		-  [[inclusion et équivalence#théorème|théorème]]
		- algorithmes
			- [[inclusion et équivalence#algorithme|méthode 1]]
			- [[inclusion et équivalence#autre méthode|méthode 2]]
	- [[autres opérations]]
	- [[sémantique des expressions rationnelles]]
		-  [[sémantique des expressions rationnelles#exemples|exemples]]
- exemples
	- [[exemple langage 1]]
	- [[exemple langage 2]]
	-  [[exemple AFN]]
	- [[exemple construction AFN apd expression rationnelle]]

# Chapitre 5: Logique des Prédicats
-  [[langage du premier ordre]]
	- [[alphabet]]
	-  [[construction des termes]]
	-  [[construction de formules]]
	-  [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/5 - Logique des Prédicats/règles de précédence|règles de précédence]]
	- [[variable libre, liée]]
	- [[formule close]]
	- [[Libres(phi)]]
	- [[exemples formules]]
- sémantique
	-  [[structure]]
		-  [[structure#exemples|exemples]]
		- [[interprétation des termes dans une structure]]
	- [[interprétation des formules]]
	- [[structures et satisfaction des formules]]
		-  [[structures et satisfaction des formules#exemples|exemples]]
	- [[formule satisfaisable]]
	- [[formule valide]]
	-  [[formule équivalente]]
		- [[formule équivalente#exemples de formules équivalentes|exemples]]
		- [[formule équivalente#à ne pas faire !!!!!|à ne pas faire !!]]
	- exemples
		-  [[exemple 1]]
		- [[exemple 2]]
- indécidabilité du problème de validité
	- [[Problème Indécidable#théorème| théorème problème de la correspondance de Post]]
	- [[théorème de la validité en logique du premier ordre]]
		-  [[théorème de la validité en logique du premier ordre#preuve (pas à l'examen askip)|preuve]]
			-  [[théorème de la validité en logique du premier ordre#considérations|considérations]]
			- [[théorème de la validité en logique du premier ordre#étape 1|étape 1]]
			- [[théorème de la validité en logique du premier ordre#étape 2|étape 2]]
			- [[théorème de la validité en logique du premier ordre#étape 3|étape 3]]
