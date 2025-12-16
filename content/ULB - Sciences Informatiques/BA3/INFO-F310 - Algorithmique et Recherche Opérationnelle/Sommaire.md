---
title: INFO-F310 - Algorithmique et Recherche Opérationnelle
authors: Alessandro Dorigo
tags:
  - BA3
  - ULB
  - Algo
  - Maths
---
## 1 - Introduction
En partant d'un énoncé/problème donné, on va:
1) Modéliser ce problème (spécifier les alternatives, restrictions, fonction a optimiser (min/max))
2) Formuler ce modèle en un programme mathématique (définir formellement les variables, contraintes et la fonction objectif)
3) A partir de la formulation, chercher (utiliser une méthode de résolution)

- [[Problème d'achat de billets d'avion]]
- [[Modèle de recherche opérationnelle]]
	- [[Solution admissible]]
	- [[Solution optimale]]
	- [[Variable]]
	- [[Fonction objectif]]
	- [[Contrainte]]
	- [[Paramètre]]
- [[Ensemble convexe]]
- [[Fonction convexe]]
- [[Problème de maximisation de la surface d'un rectangle]]
- [[Méthodes de résolution]]
- [[Localisation d’émetteurs de télévision]]
## 2 - Programmes Linéaires
- rappel mathématique
	- [[théorie des ensembles convexes]]
		- [[théorie des ensembles convexes#combinaison convexe|combinaison convexe]]
		- [[théorie des ensembles convexes#ensemble convexe|ensemble convexe]]
		- [[théorie des ensembles convexes#enveloppe convexe|enveloppe convexe]]
		- [[théorie des ensembles convexes#point extrême|point extreme]]
- définitions
	- [[Programme linéaire]]
	- [[forme standard]]
	- [[forme canonique]]
	- [[solution de base]]
		- [[solution de base#^503980|solution de base réalisable]]
		- [[solution de base#^2d600c|solution de base dégénérée]]
		- [[solution de base#^199e43|solution de base réalisable dégénérée]]
		-  [[solution de base#^50a468|solution réalisable optimale]]
		-  [[solution de base#^af92a8|solution réalisable]]
- théorèmes
	-  [[théorème d'équivalence]]
	-  [[théorème fondamental de programmation linéaire]]
	-  [[théorème de Minkowski]]
	- [[théorème d'équivalence V2]]
	- [[corollaires]]
- exemples
	- [[Problème de production de peinture]]
	- [[problème diététique]]
	- théorème d'équivalence
		-  [[exemple théorème d'équivalence|jsp frr, il le sort de son cul]]
		- [[fast food]]

# 3 - Résolution
- résolution
	- [[méthode graphique]]
		- [[production de peinture#méthode graphique avec programme linéaire|exemple]]
	- [[méthode du simplexe]]
		- [[production de peinture#méthode du simplexe|exemple]]
	- [[méthode des deux phases]]
- à savoir
	- [[règles de standardization]]
		- [[exemples règles de standardization]]
	- cas particuliers
		- [[base dégénérée]]
			- [[exemple base dégénérée]]
		- [[solutions optimales multiples]]
			- [[exemple solutions optimales multiples]]
		- [[problèmes non-bornés]]
			- [[exemples problème de non-borné]]
		- [[problèmes impossibles]]
- ahahahahahah c'est trop marrant
	- [[interprétation économique]]

# 4 - jsp frr
- problèmes
	- [[problème de maximisation]]
	- [[problème de minimisation]]
- [[dualité]]
	- [[problème dual]]
		- [[problème dual#propriétés du dual|propriétés]]
		- [[problème dual#construction|construction]]
			- [[problème dual#construction sous forme matriciel|sous forme matricielle]]
			- [[problème dual#construction en tableau indiciel|en tableau indiciel]]
	- relation primal dual
		- [[dualité faible]]
			- [[dualité faible#preuve|preuve]]
			- [[dualité faible#conséquence du théorème|conséquence]]
		- [[dualité forte]]
			-  [[dualité forte#interprétation|interprétation]]
			-  [[dualité forte#démonstration|preuve 1]]
			- [[dualité forte#autre démonstration (plus courte car why not)|preuve 2]]
		- [[corollaire de la dualité forte]]
		- [[synthèse relation primal-dual]]
- complémentarité
	-  [[1er théorème des écarts complémentaires]]
	- [[2e théorème des écarts complémentaires]]
		- [[2e théorème des écarts complémentaires#exemple|exemple]]
- interprétation économique
	-  [[interprétation économique dualité faible et forte]]
		- [[interprétation économique dualité faible et forte#exemple|exemple]]
	- [[corollaire du théorème de la dualité forte]]
		- [[corollaire du théorème de la dualité forte#interprétation économique| interprétation eco]]
	-  [[méthode simplexe duale]]
		-  [[méthode simplexe duale#théorème 1|théorème 1]]
		-  [[méthode simplexe duale#motivation|motivation]]
		- [[méthode simplexe duale#relations|relation]]
		- [[méthode simplexe duale#théorème 2|théorème 2]]
		-  [[méthode simplexe duale#principe|principe]]
- exemples
	- [[exemple primal dual 1]]
	- [[exemple primal-dual 2]]
