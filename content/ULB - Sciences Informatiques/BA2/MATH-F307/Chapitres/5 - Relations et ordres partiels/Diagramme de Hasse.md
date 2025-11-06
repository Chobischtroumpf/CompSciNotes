---
title: Diagramme de Hasse
authors: Alessandro Dorigo
tags:
  - MathDis
  - Relations
  - Graphe
---


> [!info]+ Définition
> Un **diagramme de Hasse** est un type de graphe qui représente visuellement un [[Ensemble ordonné#^f247ff|ensemble partiellement ordonné]]. Il est souvent utilisé pour montrer la relation d'ordre entre les éléments d'un ensemble sans inclure les relations redondantes.

Dans un diagramme de Hasse:
- Chaque **élément** de l'ensemble est représenté par un point.
- Une **ligne montante** (ou un arc) relie deux points $a$ et $b$ si $a$ est **immédiatement inférieur** à $b$ selon la relation d'ordre.
- Les points sont disposés de manière à ce que si $a \leq b$, alors $a$ apparaît **en dessous** de $b$ dans le diagramme.
- Aucune ligne n'est dessinée entre deux éléments si la relation entre eux peut être dérivée par transitivité (par exemple, si $a \leq b$ et $b \leq c$, on ne dessine pas de lien direct entre $a$ et $c$).

> [!example]+ Exemple
> ![[Pasted image 20241104084642.png]]
