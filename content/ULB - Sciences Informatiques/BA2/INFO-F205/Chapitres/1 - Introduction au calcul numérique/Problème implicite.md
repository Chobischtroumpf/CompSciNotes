---
title: Problème implicite
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Definition
> Un problème est dit **implicite** lorsque la solution est définie par une équation ou un système d’équations à résoudre, plutôt qu’une expression explicite. Il faut donc recourir à des méthodes algorithmiques ou numériques pour obtenir une solution.
>
> **Forme générale:**
> $$F(\vec{x}, \vec{d}) = 0$$
> où $F$ est une fonction définissant une relation entre les inconnues $\vec{x}$ et les données $\vec{d}$,

^8f6eed

> [!example]+ Exemples
> - Trouver la plus grande racine $x$ de l’équation du second degré $ax^2 + bx + c = 0$ où les données sont représentées par le vecteur $\vec{d} = [a, b, c]$.
> - Trouver la solution du système linéaire $A\vec{x} = \vec{b}$ où les données sont représentées par la matrice étendue $\vec{d} = [A \mid \vec{b}]$.
