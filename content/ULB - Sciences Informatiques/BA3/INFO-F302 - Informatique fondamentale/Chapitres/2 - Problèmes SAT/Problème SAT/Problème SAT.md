---
title: Problème SAT
authors: Alessandro Dorigo
tags:
  - InfoFond
---

# définition prb SAT
- entrée : un ensemble de clauses $S$
- sortie : est-ce que $S$ est satisfaisable ?
	- si oui, quelle valuation $V$ satisfait $S$

## solveurs SAT
- solveur SAT
	- programme qui décide le prb SAT
	- si formule satisfaisable, une interprétation qui la satisfait est retournée
		- pas de connaissance d'algo (SAT NP-complet)
		- essai de se comporter efficacement dans la plupart des cas mais au pire des cas, complexité exponentielle

- motivations
	- bcp prb peuvent s'exprimer naturellement par des formules en F?C
	- les prb de classe NP se réduisent tous au prb SAT en tps poly
	- → plutôt qu'avoir un algo pour chaque prb, écrire bon algo SAT et transformer automatiquement cq instance du prb de départ en une instance de SAT équivalente
		- si transformation (= réduction) en temps raisonnable alors utilisation d'un solveur SAT donne parfois d'aussi bons résultats qu'un algo dédié au prb de départ
		- difficulté de trouver cette réduction = modéliser le prb de départ comme une instance de SAT sous FNC


## complexité du prb SAT
- prb de satisfaisabilité d'une formule propositionnelle dans la classe SAT
- on ne sait pas s'il existe algo pour ce prb en temps polynomiale
	- plupart pensent que ce n'est pas le cas- pas de démonstrastion
- → question $P \neq NP$
	- existence d'un prb résoluble en temps non-déterministe polynomial pas résoluble en temps polynomial
	- _Millenium Prize Problems du Clay Mathematics Institute_
- → beaucoup d'applications
	- ts prb de la classe $NP$ se réduisent au prb SAT en temps poly
	- ~ résoudre une instance $I$ du prb SAT : construire, en tps poly, une formule de la logique propo $\phi_I$ tq $\phi_I$ est satisfaisable ssi $I$ a une solution
	- → "bons" algo pour SAT
