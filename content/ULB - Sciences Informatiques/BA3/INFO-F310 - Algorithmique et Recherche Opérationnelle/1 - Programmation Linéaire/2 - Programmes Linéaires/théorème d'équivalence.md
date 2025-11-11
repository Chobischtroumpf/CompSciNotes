---
title: théorème d'équivalence
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
# Théorème d'équivalence

> [!abstract]- Théorème "Théorème d'équivalence"
>
> Tout programme linéaire peut s'écrire sous forme standard **et** canonique.

> [!tip]+ Remarque
>
> Les opérations suivantes permettent de passer d'une forme à une autre :
>
> **Transformation de l'objectif :**
>
> $$ \min_x c^T x = - \max_x (-c^T x) $$
>
> **Transformation des contraintes d'égalité :**
>
> $$ a^T x = b \leftrightarrow \begin{cases} a^T x \leq b \ a^T x \geq b \leftrightarrow -a^T x \leq -b \end{cases} $$
>
> **Transformation des contraintes d'inégalité :**
>
> $$ \begin{align} a^T x \leq b &\leftrightarrow a^T x + s = b, \quad s \text{ (slack)} \geq 0 \ a^T x \geq b &\leftrightarrow a^T x - e = b, \quad e \text{ (excess)} \geq 0 \end{align} $$
>
> **Variables non restreintes :**
>
> Pour une variable $x$ non restreinte en signe, on définit de nouvelles variables :
>
> $$ \begin{align} x^+ &= \max[0, x] \geq 0 \ x^- &= \max[0, -x] \geq 0 \ x &= x^+ - x^- \end{align} $$
>
> En pratique, ces opérations permettent simplement de convertir un programme linéaire d'une forme à une autre.
