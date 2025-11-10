---
title: File
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!info]+ Définition
> Une **file** est une structure de données qui suit le principe **FIFO** (_First In, First Out_), où le premier élément inséré est le premier à être retiré. Un exemple classique de file est une file d’attente dans la vie quotidienne, où la personne arrivée en premier est la première à être servie.
>
> ![[cd931f42875e15d36ac1f1756ff8dce8.png]]

- Une File est, comme l’est une Pile, une zone de sauvegarde temporaire
- La gestion des entrées et sorties dans cette zone répond au principe FIFO

The simplest example of a queue is the typical line that we all participate in from time to time.
We wait in a line for a movie, we wait in the check-out line at a grocery store, and we wait in the cafeteria line (so that we can pop the tray stack). Well-behaved lines, or queues, are very restrictive in that they have only one way in and only one way out. There is no jumping in the middle and no leaving before you have waited the necessary amount of time to get to the front.

- L’interface de base d’une file consiste en les primitives suivantes :
	- `insert`: rajout d’un élément dans la file
	- `remove`: retrait d’un élément de la file
	- `head`: indique la valeur de l’élément qui sera le prochain à sortir de la file
	- `isEmpty`: indique si la file est vide ou non
	- `size`: indique le nombre d’éléments présents dans la file
## File (tableau)
![[a0d3065503f897a071f60b066c035acb.png]]
- Au moyen d’un tableau, on maintient deux indices appelés `debut` et `fin`
- Le tableau est géré circulairement
- On insère un élément en `fin` (et on incrémente cet indice)
- Lors d’une insertion, si on atteint l’extrémité (droite) du tableau, on continue circulairement à l’indice 0 (si cette position est libre)
- On retire un élément de la file en `début` et on incrémente aussi cet indice que l’on gère aussi bien sûr circulairement
## File (pointeurs)
![[3e832139e43293eb10c42ad40383fa65.png]]
[[Chap 01 - slides_adt.pdf#File (sans Node)]] / [[Chap 01 - slides_adt.pdf#File (avec Node)]]
- Au moyen d’une liste circulaire avec élément bidon, on supprime en tête de liste et on insère en fin de liste
- L’élément bidon permet de s’assurer qu’il y a toujours un élément qui précède l’élément courant
- On gère un pointeur `fin` qui pointe vers le dernier élément de la liste (ce pointeur nous permet aisément de retrouver la tête de la liste)
