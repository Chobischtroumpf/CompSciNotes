---
title: Contrainte
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Définition
> Une condition ou restriction que la solution doit respecter. Elle limite l'ensemble des [[Solution admissible#^12896e|solutions admissibles]].

^77d260

**Types de contraintes**:
- Linéaire/non-linéaire
- Convexe/non-convexe
- Égalités/inégalités

> [!example] Exemples
> - **Contraintes linéaires d’égalité**: $Ax = b, A \in \mathbb{R}^{m \times n}, x \in \mathbb{R}^n, b \in \mathbb{R}^m$
> - **Contraintes linéaires d’inégalité**: $Ax \leq b, A \in \mathbb{R}^{m \times n}, x \in \mathbb{R}^n, b \in \mathbb{R}^m$
> - **Contraintes non-linéaires d’égalité**: $h(x) = 0, h: \mathbb{R}^n \to \mathbb{R}^m$
> - **Contraintes non-linéaires d’inégalité**: $g(x) \leq 0, g: \mathbb{R}^n \to \mathbb{R}^p$

> [!note]
> Un modèle peut combiner différents types de contraintes (par exemple, des contraintes linéaires d’égalité et d’inégalité)
