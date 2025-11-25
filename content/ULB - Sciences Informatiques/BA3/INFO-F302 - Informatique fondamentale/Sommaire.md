---
title: INFO-F302 - Informatique fondamentale
authors: Alessandro Dorigo
tags:
  - ULB
  - BA3
  - InfoFond
  - Maths
---
# Chapitre 0: Introduction
- [[Théorème d’incomplétude de Gödel]]
- [[Informatique fondamentale]]
	- [[Automate]]
		- [[Machine de Turing]]
	- [[Chaîne de Markov]]
	- [[Système de déduction]]
- [[Théorie de la complexité]]
	- [[Problème complet]]
- [[Réductions entre problèmes]]
- [[Problème 2-partition]]
- [[Problème Bin Packing]]
# Chapitre 1: La Logique Propositionnelle
### Introduction, syntaxe, sémantique, satisfaisabilité, validité
- [[Formalisation logique]]
- [[BNF - Bachus-Naur Form]]
- [[Règles de précédence]]
- [[Fonction d’interprétation]]
- [[Validité]]
- [[Satisfaisabilité]]
### Tableaux Sémantiques
- [[Sémantique]]
	- [[Tableau sémantique]]
	- [[Règles de simplification]]
### Déduction Naturelle
- [[Déduction naturelle]]
- [[Conjonction]]
- [[Double négation]]
- [[Modus Tollens (Contraposition)]]
- [[Les règles de déduction naturelle]]
- [[Équivalence]]

# Chap 2 : problème SAT

## littéraux et clauses
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - problème SAT/littéraux et clauses/définitions|définitions]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - problème SAT/littéraux et clauses/définitions#clause|clause]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - problème SAT/littéraux et clauses/définitions#satisfaction d'ensemble de clauses|satisfaction d'ensemble de clauses]]
- [[formes normales]]
	- [[formes normales#forme normale conjonctive (FNC)|forme normale conjonctive]]
	- [[formes normales#forme normale conjonctive (FND)|forme normale conjonctive]]
	- [[formes normales#mise sous FNC et FND|mise sous FNC et FND]]
- [[lien avec SAT]]
## problème SAT
- [[Problème SAT#définition prb SAT|définition problème SAT]]
	- [[Problème SAT#complexité du prb SAT|complexité du prb SAT]]
- [[Notations]]
	- [[Notations#disjonction|grande disjonction]]
	- [[Notations#conjonction|grande conjonction]]

## modélisation
- [[Coloriage des cartes]]
- [[Problème des 8 reines]]
- [[jeu Sudoku]]
- [[Problème de pavage]]

## algo DPLL
- definitions
	- [[interprétation partielle]]
		- [[interprétation partielle#simplification sous une interprétation partielle|simplification sous interprétation partielle]]
- [[Algo DPLL]]
	- [[Algo DPLL#proposition pivot|proposition pivot]]
		- [[Algo DPLL#premier critère de choix clauses unitaires|clauses unitaires]]
		- [[Algo DPLL#deuxième critère de choix proposition à polarité unique|proposition à la polarité unique]]
	- [[Algo DPLL#pseudo code|pseudocode]]

## transformation de tseitin
-  [[transformation de Tseitin]]
- [[variantes SAT]]
	- [[variantes SAT#2SAT|2-SAT]]
	- [[variantes SAT#QSAT|QSAT]]
	- [[variantes SAT#WEIGHTED-MAX-SAT|WEIGHTED-MAX-SAT]]
		- [[variantes SAT#MAX-SAT|MAX-SAT]]

# Chap 3 : classes P et NP 
- [[introduction]]
- problème 
	- [[problème de décision]]
	-  [[problème d'optimisation]]
	- [[problème indécidable]]
		-  [[problème indécidable#exemple problème de l'arrêt|problème de l'arrêt]]
			-  [[problème indécidable#problème de la correspondance de Post|problème de la correspondance de Post]]
		- [[problème indécidable#autres problèmes indécidables|autres exemples]]
- algorithmes
	-  [[algorithme de décision]]
	-  [[algorithme de vérification]]
- classes
	- [[classe P]]
	-  [[classe NP]]
		-  [[classe NP#$NP subseteq$ ExpTime|$NP \subseteq Exptime$]]
		-  [[classe NP#$NP$- dur ou $NP$-difficiles|NP-dur]]
	- [[autres classes]]
- preuves
	- [[conjecture]]
	- démontrer qu'un prb est NP-complet 
		-  [[composition de réduction]]
		-  [[théorème de la réduction]]
		-  [[conséquence de la complétude]]
- exercices
	- [[bin packing est np-complet]]
	-  [[graphcolor est np-complet]]
		- [[graphcolor est np-complet#réduction de 3SATvers GRAPHCOLOR|réduction 3SAT vers GRAPHCOLOR]]
	-  [[démonstration problème indécidable]]

# Chap4 : automates finis 
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - automates finis/introduction|introduction]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - automates finis/introduction#exemples|exemples]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - automates finis/introduction#applications possibles|applications possibles]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/4 - automates finis/introduction#avantages/inconvénients des automates|avantages / inconvénients]]
- définitions 
	-  [[language]]
		- [[language#langage accepté ou reconnu|language accepté ou reconnu]]
	- [[facteur]]
	-  [[automate fini]]
	-  [[exécution]]
	- [[état atteignable]]
- résultats 
	- [[complétion d'un automate]]
		- [[complétion d'un automate#lemme|lemme]]
	-  [[problème du VIDE]]
	- [[état atteignable#théorème|théorème des états atteignables]]
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