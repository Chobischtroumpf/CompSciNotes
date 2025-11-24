---
title: Réductions entre problèmes
authors: Alessandro Dorigo
tags:
  - InfoFond
---


> [!abstract]- Principe des réductions
> Si on peut résoudre un [[Problème complet#^670910|problème complet]] pour une classe, on peut résoudre tous les autres problèmes de la classe avec la même complexité asymptotique.

> [!info]+ Définition
> Une **réduction** d'un problème $A$ vers un problème $B$ est une méthode permettant d'encoder toute entrée du problème $A$ comme une entrée du problème $B$, de sorte qu'une solution existe pour l'entrée de $A$ si et seulement si une solution existe pour l'entrée correspondante de $B$.

^0954bf

 > [!abstract]- Réduction pour problèmes de décision
 > Réduire un problème $A$ vers un problème $B$, c’est trouver une méthode permettant d’encoder toute entrée $I_A$ du problème $A$ comme une entrée $I_B$ du problème $B$, telle que $I_A$ a une solution (la réponse est oui) si et seulement si $I_B$ a une solution.
 >
 > Cela signifie trouver une fonction $f$ telle que:
 > - $f$ transforme toute entrée $I_A$ du problème $A$ en une entrée $I_B = f(I_A)$ du problème $B$
 > - $I_A$ a une solution $\Leftrightarrow I_B$ a une solution
 > - **Notation**: $A \leqslant B$ ("$A$ se réduit à $B$")

> [!abstract]- Réduction pour problèmes généraux
> Pour les problèmes qui ne sont pas de décision (exemple : trier un tableau):
> - Toute solution de $I_A$ s'encode en une solution de $I_B$
> - Réciproquement, toute solution de $I_B$ se décode en une solution de $I_A$

> [!abstract]- Propriétés des réductions
> Si $A \leqslant B$, alors:
> 1. **Résolution**: Un algorithme pour $B$ donne un algorithme pour $A$
> 2. **Complexité**: Si $B$ est "facile", alors $A$ est "facile"
> 3. **Indécidabilité**: Si $A$ est indécidable, alors $B$ est indécidable
> 4. **Transitivité**: Si $A \leqslant B$ et $B \leqslant C$, alors $A \leqslant C$

> [!example]+ Exemple
> **[[Problème 2-partition#^264e40|Problème 2-partition]]** $\leqslant$ **[[Problème Bin Packing#^a7a3c5|Problème Bin Packing]]**
> - **2-partition**: Partitionner un ensemble d'entiers en deux sous-ensembles de sommes égales
> - **Réduction**: Prendre $C = S/2$ (où $S$ est la somme totale), $k = 2$ sacs
> - **Équivalence**: Il existe une 2-partition $\Leftrightarrow$ on peut ranger tous les objets dans 2 sacs
