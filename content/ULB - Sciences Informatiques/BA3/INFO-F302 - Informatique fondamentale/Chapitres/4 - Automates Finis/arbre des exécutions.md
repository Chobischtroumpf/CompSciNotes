---
title: arbre des exécutions
authors: Mihai Bors
tags: []
---

# arbre des exécutions
**introduction**
- combien d'exécution sur un mot de taille $m$
	- automate fini déterministe à $n$ états : $n^m$
	- automate non déterministe : complexité polynomiale
- → toutes les exécutions peuvent être représentées par un arbre
![[Pasted image 20251125154603.png]]
![[Pasted image 20251125154619.png]]
- à un même niveau dans l'arbre, ts les sous-arbes enracinés aux mêmes états sont identiques
	- → ce qui est important, c'est l'ensemble des états atteints

## test d'appartenance au langage
- soit
	- $P \subseteq Q$
	- $\sigma \in \Sigma$
	- → $Post_A(P,\sigma) = \set{p | \exists p' \in P \cdot (p', \sigma, p) \in \Delta}$
		- ensemble des états qu'on peut atteindre apd états de $P$ en lisant $\sigma$
### algorithme
- TEST(A,P,u)
	- case $u = \epsilon$
		- return $P \cap F \neq \emptyset$
	- case $u = \sigma v (\sigma \in \Sigma)$
		- return TEST($A, Post_A(P,\sigma),v)$

### lemme
- $u \in L(A) \Leftrightarrow TEST(A, \set{q_0}, u)$

## théorème
- Etant donné un AFN $A$ avec $n$ transitions et un mot $u$ de longueur $m$
	- tester si $u \in L(A)$ peut se faire en temps $O(|u|\cdot m)$
- → preuve
	- prendre algorithme précédent
		- calculer $Post_A(P,\sigma)$ sen fait en temps $O(m)$
### exemple
![[Pasted image 20251125161220.png]]
→ l'ensemble final $\set{q_0,q_2,q_3}$ contient un état acceptant donc le mot est accepté

## théorème
- étant donné un AFN $A$ avec $n$ états et $m$ transitions
	- on peut déccider en temps $O(n+m)$ si $L(A) = \emptyset$
- → même agorithme pour les automates finis déterministes
