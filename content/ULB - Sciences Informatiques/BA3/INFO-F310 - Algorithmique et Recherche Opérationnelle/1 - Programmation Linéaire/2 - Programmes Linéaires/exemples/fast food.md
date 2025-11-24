---
title: fast food
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---

## énoncé
- fast food vend des hamburgers et des cheeseburgeurs
	- hamburger = 125g de viande
	- cheeseburger = 100g de viande
- fast-food démarre chq journée avec 10kg de viande mais peut commander 2€/kg de viande supp pour la livraison
- profit
	- 0.02€ / hamburger
	- 0.015€ / cheeseburger
- demande ne dépasse pas 900 sandwiches/jours - surplus donnés

## prb
combien le fast-food doit-il produire de sandwiches de chq type/jour ?

## var
- x1 = nb hamburgers vendus / jour
- x2 = nb cheeseburgers vendus / jour

## contraintes
- borne sup sur les ventes de sandwichs par jour : $x_1 + x_2 \leq 900$
- commande de viande supp : intro d'un var non restreinte x3 tq : $0.125x_1 + 0.1x_2 + x_3 = 10$
	- coût pour la viande supp (déficit) apparaît ssi $x_3 \lt 0$
	- → substitution de la var x3 par 2 var non-neg $x_3^+, x_3^-$
		- $x_3 = x_3^+ - x_3^-, x_3^+, x_3^- \geq 0$
		- → $0.125,x_3 + 0.1x_2 + x_3^+ - x_3^- = 10$

## modèle complet
- $\max z = 0.02x_1 + 0.015x_2 - 2x_3^-$
- contraintes
	- $x_1 + x_2 \leq 900$
	- $0.125x_1 + 0.1x_2 + x_3^ - x_3^- = 10$
	- $x_1,x_2, x_3^+, x_3^-  \geq 0$
