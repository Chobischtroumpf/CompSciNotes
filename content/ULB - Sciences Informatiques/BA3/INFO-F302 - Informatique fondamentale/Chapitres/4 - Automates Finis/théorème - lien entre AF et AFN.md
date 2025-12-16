---
title: théorème - lien entre AF et AFN
authors: Mihai Bors
tags: []
---

# théorème
- Soit $L$ un langage sur un alphabet $\Sigma$
	- $L$ est accepté par un automate fini
	- $\Leftrightarrow$ s'il est accepté par un AFN

## preuve
- sens AFN → AF
	- étant donné un ANF $A$, construire un AF  $B$ équivalent
		- qui acccepte le même langage
### construction des sous-ensembles
- ~tester l'appartenance au language
	- AF $B$ qui simule AFN $A$ calcule le sous-ensemble d'états atteints
	- états de $B$ seront donc des sous-ensembles d'états de $A$
		- $etats_B \subseteq  etats_A$
	- apd d'un sous-ensemble $P \subseteq Q$, en lisant une lettre $\sigma$
		- → $B$ va vers l'état $Post_A(P,\sigma)$
	- états acceptants de $B$ sont les sous-ensembles qui contiennent un état acceptant de $A$
- formellement
	- $A= (Q, q_0, F, \Delta)$ sur un alphabet $\Sigma$
		- → $B = (2^Q, \set{q_0}, F':= \set{P \subseteq Q | P \cap F \neq \emptyset}, \delta := Post_A)$
**exemple**
![[Pasted image 20251125162341.png]]

## complexité
- l'automate $B$ (AFN) construit, a exponentiellement plus détats que $A$
	- → inévitable en général
- on peut mq $\forall n \geq 0$,
	- le plus petit AF acceptant le langage $L_n$ des mots de longueur au moins $n$
		- dont la $n$-ème lettre en artant de la fin est $a$
	- sur l'alphabet $\set{a,b}$, a $2^{O(n)}$ états
- le plus petit AFN pour $L_n$ a $O(n)$ états
	- → AFN sont exponentiellements plus succincts que les AF
