---
title: exemple langage 2
authors: Mihai Bors
tags: []
---

# exemple
 - prenons l'alphabet $\Sigma = \set{a,b}$
- un automate qui accepte
	- $L_3 = \set{u \in \Sigma^* | |u| \geq 3 \land u[|u| - 3] = a}$
	- ie. l'ensemble des mots de longueur au moins 3  dont la 3e lettre en partant de la fin est $a$
![[Pasted image 20251125152928.png]]
- → généralement, si on veut vérifier que la $n$-ième lettre en partant de la fin est $a$
	- → il faut $O(2^n)$ états (lecture de gauche à droite )
