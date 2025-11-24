---
title: Algorithme numérique
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Étant donné un problème bien posé $F(\vec{x}, \vec{d}) = 0$, nous définissons **l'algorithme numérique** pour la résolution du problème $F$ par la suite de problèmes approchés:
> $$F_1(\vec{x}^{(1)}, \vec{d}^{(1)}), F_2(\vec{x}^{(2)}, \vec{d}^{(2)}), ..., F_n(\vec{x}^{(n)}, \vec{d}^{(n)})$$
> dépendant d'un paramètre $n$.

> [!info]+ Propriétés des algorithmes numériques
> - **[[Consistance]]** : La solution du problème original appartient à celles des sous-problèmes.
> - **[[Stabilité]]** : Sensibilité aux perturbations des données.
> - **[[Convergence]]** : Assure que la solution numérique approche la solution exacte.

> [!abstract]- Théorème de Lax-Richtmyer
> Un algorithme numérique est **convergent** si et seulement s'il est [[Consistance#^77e44d|consistant]] et [[Stabilité#^f6ba30|stable]].

> [!tip]+ Types d'algorithmes
> - Un algorithme est dit **déterministe** si à chaque moment de l'exécution, la prochaine étape est déterminée de façon unique
> - Si plusieurs alternatives existent, l'algorithme est dit non-déterministe.
> - Un algorithme non-déterministe est dit **stochastique** si la probabilité des différentes alternatives est décrite par une distribution de probabilité.
