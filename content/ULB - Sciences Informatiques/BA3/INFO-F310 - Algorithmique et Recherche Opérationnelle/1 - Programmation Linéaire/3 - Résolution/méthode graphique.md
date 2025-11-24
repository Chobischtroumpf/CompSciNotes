---
title: méthode graphique
authors: iamscrambledeggs
tags: []
---

# méthode graphique
## Etapes
1. reporter sur un graphique chacune des contriantes
2. déterminer sur ce grpahique l'intersection de l'ensemble de toutes ces contraintes (demi-espaces)
	1. _note : cette intersection, si elle existe, constitue l'ensemble des solutions admissibles_
3. déterminer les coordonnées des points extrêmes (ie. sommets du polyèdre défini par l'ensemble des solutions admissibles). soit par
	1. localisation directe sur le graphique
	2. calcul des coordonnées du point d'intersection des droits
		1. pour chaque pt extrême, résoudre sys d'eq des droites qui se coupent en ce points
4. substituer les coordonnées de chq point extrême dans la fonction objectif
	1. le point extrême qui optimise la fonction objectif $\equiv$ solution optimale
[[#méthode graphique avec programme linéaire|exemple]]

### courbe de niveau
- courbe de niveau
	- courbe de niveau $z$ d'une fonction $f$ est déifnie par l'ensemble des points $(x_1, x_2)$ appartenant à l'ensemble de définition de $f$ vérifiant $f(x_1,x_2) = z$
	- courbes de niveaux de l'objectif $z$ : ensemble de solutions ayant un profit (valeur de l'objectif) donné
**méthode**
- recherche de l'intersection entre une droite et le polyèdre convexe ABCDEF définissant l'ensemble des solutions admissibles
- amélioration de la solution : recherche d'une direction dans laquelle le profit $z$ augmente
- recherche de la solution optimale : la droite mobile doit garder une intersection avec l'ensemble des solutions admissibles
