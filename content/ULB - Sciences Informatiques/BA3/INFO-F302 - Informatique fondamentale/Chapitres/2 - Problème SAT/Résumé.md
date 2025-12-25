---
title: Résumé
authors: Mihai Bors
tags:
  - InfoFond
---
## Problème SAT

Le chapitre introduit ce qu'est SAT. On commence par expliquer les littéraux et clauses, qui nous permettent d'introduire SAT, qui utilise ces concepts. SAT est un problème qui consiste à satisfaire toutes les clauses avec une seule valuation (ou interprétation).

Pour résoudre un problème via SAT, on doit trouver un moyen de convertir (réduire) ce problème vers SAT, en traduisant le français en une formule booléenne (qui est ensuite convertie en FNC).

On voit ensuite des moyens d'optimisation pour pouvoir rendre SAT plus rapide. On commence avec [[Algo DPLL|DPLL]], qui est un algorithme qui recherche des clauses unitaires avec un seul littéral et des variables qui ont une polarité unique (toujours positives ou toujours négatives) à travers toute la formule. Cela nous permet de ne pas avoir à tout explorer et d'élaguer l'arbre de recherche pour résoudre une formule.

Finalement, on parle de la transformation de Tseitin, qui consiste à introduire des variables intermédiaires pour réduire le nombre de clauses dans la formule et donc rendre la résolution linéaire au lieu d'exponentielle, c'est surtout utile quand on a des formules en FND (forme normale disjonctive) à convertir en FNC, par exemple $(x_1 \land q_1) \lor (x_2 \land q_2) \lor \dots$ qui donnerait $2^n$ clauses par distribution naïve.
