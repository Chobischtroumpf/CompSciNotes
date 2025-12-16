---
title: Composition de Réduction
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **composition de réductions** est la propriété selon laquelle si $A$ se réduit à $B$ et $B$ se réduit à $C$, alors $A$ se réduit à $C$. Cette propriété est fondamentale pour prouver la NP-dureté de nouveaux problèmes.

## Lemme de Composition

> [!abstract]+ Énoncé
> Soient $A$, $B$, $C$ trois problèmes, et soient :
> - $f$ : une réduction de $A$ vers $B$ en temps $O(n^c)$
> - $g$ : une réduction de $B$ vers $C$ en temps $O(n^d)$
>
> Alors $g \circ f$ est une réduction de $A$ vers $C$ en temps $O(n^{cd})$.

## Preuve

> [!abstract]+ Démonstration
> **Partie 1 : Correction (ça marche)**
>
> Soit $I_A$ une instance quelconque de $A$. Montrons que :
> $$I_A \text{ a une solution} \Leftrightarrow (g \circ f)(I_A) \text{ a une solution}$$
>
> Chaîne d'équivalences :
> 1. $I_A$ a une solution
> 2. $\Leftrightarrow f(I_A)$ a une solution (car $f$ est une réduction de $A$ vers $B$)
> 3. $\Leftrightarrow g(f(I_A))$ a une solution (car $g$ est une réduction de $B$ vers $C$)
>
> Donc $(g \circ f)$ est une réduction valide de $A$ vers $C$.
>
> **Partie 2 : Temps polynomial (c'est assez rapide)**
>
> Soit $n_A$ la taille de $I_A$ :
> - Taille de $f(I_A)$ : $O(n_A^c)$
> - Temps pour calculer $g(f(I_A))$ : $O((n_A^c)^d) = O(n_A^{cd})$
> - $cd$ est une constante, donc c'est polynomial

## Astuce Mnémotechnique

> [!tip]+ Mémorisation
> **"SCP"** = Setup, Correctness, Polynomial
>
> 1. **S**etup : Définir $f$ et $g$ avec leurs complexités temporelles
> 2. **C**orrectness : Chaîner les "si et seulement si" ($\Leftrightarrow$) à travers $A \to B \to C$
> 3. **P**olynomial : Composer les exposants ($c \times d$)

## Template de Preuve

> [!tip]+ Modèle de Réponse
> "Soient $f$ une réduction de $A$ vers $B$ en $O(n^c)$ et $g$ une réduction de $B$ vers $C$ en $O(n^d)$. Alors $g \circ f$ réduit $A$ vers $C$ car :
>
> (1) $I_A$ résout $A$ ssi $f(I_A)$ résout $B$ ssi $g(f(I_A))$ résout $C$
>
> (2) Le temps est $O((n^c)^d) = O(n^{cd})$ qui est polynomial."

## Application : Propagation de la NP-Dureté

> [!abstract]+ Théorème
> **Si $A$ est NP-dur et $A \leq_p B$, alors $B$ est NP-dur.**
>
> **Preuve** :
> - Soit $X \in NP$ quelconque
> - Comme $A$ est NP-dur : $X \leq_p A$ (par définition)
> - Par hypothèse : $A \leq_p B$
> - Par le lemme de composition : $X \leq_p B$
> - Comme $X$ était arbitraire : tout problème de NP se réduit à $B$
> - Donc $B$ est NP-dur

## Exemple Pratique

> [!example]+ Chaîne de Réductions
> Pour montrer qu'un nouveau problème $D$ est NP-dur :
>
> **Chaîne** : 3-SAT $\to$ Graphe 3-Coloriable $\to$ $D$
>
> **Étapes** :
> 1. 3-SAT est NP-complet (Cook-Levin)
> 2. 3-SAT $\leq_p$ Graphe 3-Coloriable (réduction connue)
> 3. Construire Graphe 3-Coloriable $\leq_p D$
> 4. Par composition : 3-SAT $\leq_p D$
> 5. Donc $D$ est NP-dur
>
> **Avantage** : On peut réduire depuis le problème le plus pratique, pas forcément depuis 3-SAT directement.

## Remarques

> [!tip]+ Observations
> **Choix du problème source** :
> - On choisit généralement le problème NP-complet le "plus proche"
> - Plus la réduction est simple, plus la preuve est claire
> - Problèmes sources courants : 3-SAT, 3-Coloriabilité, Clique, Vertex Cover
>
> **Composition multiple** :
> - On peut composer plus de deux réductions
> - $A \to B \to C \to D \to E$ est valide
> - La complexité reste polynomiale

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Réduction Polynomiale]]** : Définition de base
> - **[[Théorème de la Réduction]]** : Formalisation complète
> - **[[Classe NP#NP-Dur]]** : Utilise les réductions
> - **[[Conséquence de la Complétude]]** : Applications pratiques
