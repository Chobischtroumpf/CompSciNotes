---
title: Réduction Polynomiale
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Une **réduction polynomiale** d'un problème $A$ vers un problème $B$ est une fonction calculable en temps polynomial qui transforme toute instance de $A$ en une instance de $B$, préservant la réponse.

## Définition Formelle

> [!abstract]+ Caractérisation
> Une fonction $f : \Sigma^* \to \Sigma^*$ est une **réduction de $A$ vers $B$** (notée $A \leq_p B$) si :
>
> 1. **Calculabilité polynomiale** : $f$ est calculable en temps polynomial
> 2. **Préservation de la réponse** : Pour tout $x \in \Sigma^*$ :
>    $$x \in A \Leftrightarrow f(x) \in B$$
>
> **Notation** : $A \leq_p B$ ("$A$ se réduit polynomialement à $B$")

## Propriétés

> [!abstract]+ Propriétés Fondamentales
> **Transitivité** :
> - Si $A \leq_p B$ et $B \leq_p C$, alors $A \leq_p C$
> - Preuve : Composition de fonctions polynomiales
>
> **Préservation de P** :
> - Si $A \leq_p B$ et $B \in P$, alors $A \in P$
> - Algorithme pour $A$ : calculer $f(x)$ puis résoudre $f(x)$ dans $B$
>
> **Préservation de NP** :
> - Si $A \leq_p B$ et $B \in NP$, alors $A \in NP$

## Utilisation pour la NP-Dureté

> [!abstract]+ Montrer la NP-Dureté
> Pour montrer qu'un problème $B$ est NP-dur :
>
> 1. Choisir un problème $A$ connu NP-complet
> 2. Construire une réduction $f : A \leq_p B$
> 3. Prouver que $f$ est correcte (préserve la réponse)
> 4. Prouver que $f$ est calculable en temps polynomial
> 5. Conclure : $B$ est NP-dur

## Exemple : 2-Partition vers Bin Packing

> [!example]+ Réduction Concrète
> **Problème source** : [[Problème de Décision#2-Partition|2-Partition]]
> - Entrée : $n$ entiers $c_1, ..., c_n$ avec $S = \sum c_i$ paire
> - Question : Peut-on partitionner en deux sous-ensembles de somme $S/2$ ?
>
> **Problème cible** : Bin Packing
> - Entrée : $n$ objets, $k$ sacs de capacité $C$
> - Question : Peut-on ranger tous les objets ?
>
> **Construction de la réduction** :
> ```
> f(c_1, ..., c_n):
>     S = somme(c_1, ..., c_n)
>     return (objets = c_1,...,c_n, k = 2, C = S/2)
> ```
>
> **Correction** :
> - 2-Partition a une solution $\Leftrightarrow$ Bin Packing a une solution
> - Si partition $J$ : ranger $J$ dans sac 1, reste dans sac 2
> - Si rangement valide : objets du sac 1 forment une partition
>
> **Complexité** : $O(n)$ (calcul de $S$ et construction de l'instance)

## Composition de Réductions

> [!abstract]+ Lemme de Composition
> **Énoncé** : Si $A \leq_p B$ via $f$ en temps $O(n^c)$ et $B \leq_p C$ via $g$ en temps $O(n^d)$, alors $A \leq_p C$ via $g \circ f$ en temps $O(n^{cd})$.
>
> **Preuve** :
> 1. **Correction** :
>    - $x \in A \Leftrightarrow f(x) \in B$ (car $f$ est une réduction)
>    - $f(x) \in B \Leftrightarrow g(f(x)) \in C$ (car $g$ est une réduction)
>    - Donc $x \in A \Leftrightarrow (g \circ f)(x) \in C$
>
> 2. **Complexité** :
>    - Taille de $f(x)$ : $O(n^c)$
>    - Temps pour calculer $g(f(x))$ : $O((n^c)^d) = O(n^{cd})$
>    - Polynomial car $cd$ est une constante

## Propagation de la Dureté

> [!abstract]+ Théorème
> **Si $A$ est NP-dur et $A \leq_p B$, alors $B$ est NP-dur.**
>
> **Preuve** :
> - Soit $X \in NP$ quelconque
> - $X \leq_p A$ (car $A$ est NP-dur, par définition)
> - $A \leq_p B$ (hypothèse)
> - Par transitivité : $X \leq_p B$
> - Comme $X$ était arbitraire : tout problème de NP se réduit à $B$
> - Donc $B$ est NP-dur

## Template de Preuve

> [!tip]+ Modèle de Démonstration
> Pour montrer qu'un problème $B$ est NP-complet :
>
> **Étape 1** : Montrer que $B \in NP$
> - Décrire un certificat
> - Donner un algorithme de vérification polynomial
>
> **Étape 2** : Montrer que $B$ est NP-dur
> - Choisir $A$ NP-complet (souvent 3-SAT)
> - Construire $f : A \leq_p B$
> - Prouver : $x \in A \Leftrightarrow f(x) \in B$
> - Prouver : $f$ calculable en temps polynomial
>
> **Conclusion** : $B$ est NP-complet

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Classe NP#NP-Dur]]** : Utilise les réductions pour sa définition
> - **[[Composition de Réduction]]** : Transitivité des réductions
> - **[[Théorème de la Réduction]]** : Formalisation du lemme de composition
> - **[[Conséquence de la Complétude]]** : Implications pratiques
