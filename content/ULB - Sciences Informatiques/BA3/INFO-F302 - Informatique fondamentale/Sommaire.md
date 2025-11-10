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
- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problèmes SAT/Littéraux et Clauses/Définitions|Définitions]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problèmes SAT/Littéraux et Clauses/Définitions#clause|clause]]
	- [[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/2 - Problèmes SAT/Littéraux et Clauses/Définitions#satisfaction d'ensemble de clauses|satisfaction d'ensemble de clauses]]
- [[Formes normales]]
	- [[Formes normales#forme normale conjonctive (FNC)|forme normale conjonctive]]
	- [[Formes normales#forme normale conjonctive (FND)|forme normale conjonctive]]
	- [[Formes normales#mise sous FNC et FND|mise sous FNC et FND]]
- [[Lien avec SAT]]
## problème SAT
- [[Problème SAT#définition prb SAT|définition problème SAT]]
	- [[Problème SAT#complexité du prb SAT|complexité du prb SAT]]
- [[Notations]]
	- [[Notations#disjonction|grande disjonction]]
	- [[Notations#conjonction|grande conjonction]]

## modélisation
- [[Coloriage des cartes]]
- [[Problème des 8 reines]]
- [[Jeu Sudoku]]
- [[Problème de pavage]]

## algo DPLL
- definitions
	- [[interprétation partielle]]
		- [[interprétation partielle#simplification sous une interprétation partielle|simplification sous interprétation partielle]]
- [[Algorithme DPLL]]
	- [[Algorithme DPLL#proposition pivot|proposition pivot]]
		- [[Algorithme DPLL#premier critère de choix clauses unitaires|clauses unitaires]]
		- [[Algorithme DPLL#deuxième critère de choix proposition à polarité unique|proposition à la polarité unique]]
	- [[Algorithme DPLL#pseudo code|pseudocode]]

## transformation de tseitin
-  [[Transformation de Tseitin]]
- [[Variantes SAT]]
	- [[Variantes SAT#2SAT|2-SAT]]
	- [[Variantes SAT#QSAT|QSAT]]
	- [[Variantes SAT#WEIGHTED-MAX-SAT|WEIGHTED-MAX-SAT]]
		- [[Variantes SAT#MAX-SAT|MAX-SAT]]
