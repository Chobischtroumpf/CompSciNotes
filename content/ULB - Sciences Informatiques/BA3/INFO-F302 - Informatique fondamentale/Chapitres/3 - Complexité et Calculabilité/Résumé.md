---
title: Résumé
authors: Mihai Bors
tags:
  - InfoFond
---
## Complexité et Calculabilité



## Problèmes Indécidables

Ce chapitre nous introduit aux problèmes indécidables. Un [[problème indécidable]] est un [[problème de décision]] pour lequel il n'existe aucun algorithme qui le résout (même si l'algorithme termine en temps fini).

On a ensuite des exemples de problèmes indécidables, notamment le problème de l'arrêt où étant donné un programme qui reçoit en entrée une chaîne de caractères et le code source du programme, on veut décider si le programme va s'arrêter ou pas. On prouve que ce problème est indécidable en montrant que supposer qu'une solution existe implique une contradiction logique et donc cette solution n'existe pas.

On parle ensuite de plusieurs autres exemples, notamment le PCP, le 10ème problème de Hilbert, la complexité de Kolmogorov et le castor affairé.

Finalement, on nous montre la manière de montrer qu'un problème est indécidable, qui fonctionne de la même sorte que la preuve de NP-dureté, sauf qu'ici on n'a pas les contraintes de temps : on prend un problème qu'on réduit à un problème indécidable et donc il est également indécidable.
