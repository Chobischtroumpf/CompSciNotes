---
title: automate fini
authors: Mihai Bors
tags: []
---

# automate fini
- un automate fini, ou juste automate, $A$ sur un alphabet $\Sigma$
	- 4-uplet $(Q, q_0, F, \delta)$
		- $Q$ : ensemble fini d'éléments = états
		- $q_0 \in Q$ : état initial
		- $F \subseteq Q$: ensemble d'états dits finaux (ou acceptants)
		- $\delta : Q \times \Sigma \to Q$ : une fonction (pas nécessairement totale)
			- fonction de transition

- lorsqu'il lit une  entrée $w \in \Sigma^*$
	1. $A$ commence son exécution dans l'état $q_0$
	2. $A$ suit la fonction de transition $\delta$
		- indication en fonction de l'état où il se trouve et de la lettre qu'il lit quel est l'état suivant
		- si pas de fonction définie, alors l'automate s'arrête et le mot n'est pas accepté
	3. ...
	4. Fin de son exécution : atteint état final
		- mot accepté ou rejeté
