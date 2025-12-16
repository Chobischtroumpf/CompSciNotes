---
title: language
authors: Mihai Bors
tags: []
---

# language
- un alphabet est un ensemble fini, $\Sigma$
	- ses éléments = lettres ou symboles
	- → mot = suite finie de lettres ou symboles
		- $\epsilon$ : mot vide
	- ensemble des mots sur $\Sigma$ est noté $\Sigma^*$
- → langage $L$ est un sous ensemble de $\Sigma^*$
	- $L \subseteq \Sigma^*$

**exemple**
- avec $\Sigma = \set{a,b}$
	- $\set{a^n | n \text{ est un entier pair}}$ : un langage
## langage accepté ou reconnu
- langage accepté (ou reconnu) par l'automate $A$, noté $L(A)$
	- l'ensemble des mots qui contiennent un nombre pair de lettres $a$
	- ensemble des mots pour lesquels il existe une exécution qui les accepte (qui atteint un état acceptant)
		- un automate accepte un langage $L$ s'il accepte tous les mots de $L$ et n'accepte aucun mot qui n'est pas dans $L$
$$
L(A) = \set{w \in \Sigma^* | \text{ il existe une exécution acceptante de A sur w}}
$$

### langage accepté pour AFN
même chose qu'avec automate déterministe mais sur un AFN
