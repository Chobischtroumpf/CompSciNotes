---
title: Sources d’erreurs
authors: Alessandro Dorigo
tags:
  - CFN
---


L’erreur numérique est composée de quatre parties:
1) [[Erreur d’approximation#^6954a2|L’erreur d’approximation]];
2) [[Erreur d’arrondi#^ac2136|L’erreur d’arrondi]];
3) [[Erreur de propagation#^0d8961|L’erreur de propagation]] (indépendante de l’algorithme);
	- Cas spécial: [[Erreur d’annulation#^29c241|erreur d’annulation]].
4) [[Erreur de génération#^d42576|L’erreur de génération]] (liée à la forme de la méthode);
	- Cas spécial: [[Erreur d’absorption#^218d33|erreur d’absorption]].

> [!tip]+ Remarque
> Etant donné que chacune des quatres composantes de l’erreur dépend de ses propres facteurs, il est important d’identifier les sources et les caractéristiques de chaque type d’erreur.
