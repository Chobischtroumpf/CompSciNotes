---
title: problème dual
authors: iamscrambledeggs
tags: []
---

## propriétés du dual
- problème dual du problème dual = prb primal
	- prb d'origine
- dual d'un prb primal ss-frm canonique = prb ss-frm canonique
	- forme symétrique de la relation de dualité
- dual d'un prb primal ss-frm standard = prb ss-frm canonique avec variables duales non-restreintes
	- frm asymétrique

## construction
- apd problème primal
![[Pasted image 20251117164835.png]]

**vérification**
- → le problème dual du problème dual = problème primal
![[Pasted image 20251117164946.png]]

### construction sous forme matriciel
1. vecteurs
	1. vecteur de coeff de la fonction objectif du primal → vecteur de  droite des contraintes duales
	2. vecteur de droites des contraintes primales → vecteur de coeff de la  fonction objectif du dual
2. transposée de la matrice des contraintes du primal → matrice des contraintes du  dual
3. à chq var primale = contrainte dans le dual
	1. son signe décide du sens de la contrainte duale
4. à toute contrainte primale = var dans le dual
	1. sens décide du signe de la var duale

![[Pasted image 20251205163337.png]]
### construction en tableau indiciel
![[Pasted image 20251117172151.png]]
