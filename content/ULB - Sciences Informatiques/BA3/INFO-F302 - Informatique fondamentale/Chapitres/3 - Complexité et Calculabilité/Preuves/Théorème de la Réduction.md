---
title: Théorème de la Réduction
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Le **théorème de la réduction** formalise la composition de réductions polynomiales et établit que cette composition préserve le caractère polynomial.

## Énoncé

> [!abstract]+ Théorème
> Soient $A$, $B$, $C$ trois problèmes de décision, et soient :
> - $f$ : une réduction polynomiale de $A$ vers $B$ en temps $O(n^c)$
> - $g$ : une réduction polynomiale de $B$ vers $C$ en temps $O(n^d)$
>
> Alors $h = g \circ f$ est une réduction polynomiale de $A$ vers $C$ en temps $O(n^{cd})$.

## Démonstration

> [!abstract]+ Partie 1 : Setup (ce qu'on a)
> **Données** :
> - $A$, $B$, $C$ : trois problèmes
> - $f$ : réduction de $A$ vers $B$ en temps $O(n^c)$
> - $g$ : réduction de $B$ vers $C$ en temps $O(n^d)$

> [!abstract]+ Partie 2 : Correctness (ça marche)
> Soit $I_A$ une instance quelconque du problème $A$.
>
> Montrons que : **$I_A$ a une solution $\Leftrightarrow (g \circ f)(I_A)$ a une solution**
>
> **Chaîne d'équivalences** :
> 1. $I_A$ a une solution
> 2. $\Leftrightarrow f(I_A)$ a une solution
>    - Car $f$ est une réduction de $A$ vers $B$
> 3. $\Leftrightarrow g(f(I_A))$ a une solution
>    - Car $g$ est une réduction de $B$ vers $C$
>
> Donc $g \circ f$ est une réduction valide de $A$ vers $C$.

> [!abstract]+ Partie 3 : Polynomial (c'est assez rapide)
> Soit $n_A$ = taille de l'instance $I_A$.
>
> **Analyse de complexité** :
> - Taille de $f(I_A)$ : $O(n_A^c)$
> - Temps pour calculer $g(f(I_A))$ : $O((n_A^c)^d) = O(n_A^{cd})$
> - $cd$ est une constante
> - Donc la composition est polynomiale

## Corollaire : Propagation de la NP-Dureté

> [!abstract]+ Théorème
> **Si $A$ est NP-dur et $A$ se réduit polynomialement à $B$, alors $B$ est NP-dur.**
>
> **Preuve** :
> - **Objectif** : Montrer que tout problème $X$ de NP se réduit à $B$
>
> - **Démonstration** :
>   1. Soit $X \in NP$ quelconque
>   2. Comme $A$ est NP-dur : $X \leq_p A$ (par définition de NP-dur)
>   3. Par hypothèse : $A \leq_p B$
>   4. Par le théorème de composition : $X \leq_p B$
>   5. Comme $X$ était arbitraire : tout problème de NP se réduit à $B$
>   6. Donc $B$ est NP-dur ✓

## Template de Preuve Rapide

> [!tip]+ Modèle Standard
> "Soit $X \in NP$. Puisque $A$ est NP-dur, $X$ se réduit à $A$ en temps polynomial. Puisque $A$ se réduit à $B$ en temps polynomial, par le lemme de composition, $X$ se réduit à $B$ en temps polynomial. Comme $X$ était arbitraire, tout problème de NP se réduit à $B$, donc $B$ est NP-dur."

## Application Pratique

> [!example]+ Utilisation Courante
> **Pour montrer qu'un problème $B$ est NP-complet** :
>
> 1. **Montrer $B \in NP$** :
>    - Décrire un certificat
>    - Donner un algorithme de vérification polynomial
>
> 2. **Montrer que $B$ est NP-dur** :
>    - Choisir un problème $A$ NP-complet connu
>    - Construire une réduction $f : A \leq_p B$
>    - Utiliser le théorème pour conclure
>
> 3. **Conclusion** : $B$ est NP-complet

## Remarques Importantes

> [!warning]+ Points Clés
> **Transitivité illimitée** :
> - On peut composer autant de réductions qu'on veut
> - $A_1 \to A_2 \to ... \to A_n$ reste polynomial
> - Les exposants se multiplient : $n^{c_1 \cdot c_2 \cdot ... \cdot c_k}$
>
> **Choix du problème source** :
> - En pratique, on réduit depuis le problème le plus "proche"
> - Pas besoin de repartir de SAT à chaque fois
> - Exemples courants : 3-SAT, Vertex Cover, Clique, 3-Coloriabilité
>
> **Direction de la réduction** :
> - Attention : $A \leq_p B$ ne signifie PAS que $A$ est plus difficile que $B$
> - Au contraire : si on sait résoudre $B$, on peut résoudre $A$
> - Donc $B$ est au moins aussi difficile que $A$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Réduction Polynomiale]]** : Définition de base
> - **[[Composition de Réduction]]** : Version simplifiée
> - **[[Classe NP#NP-Dur]]** : Application principale
> - **[[Conséquence de la Complétude]]** : Implications pratiques
