---
title: Conjecture P ≠ NP
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **conjecture P ≠ NP** est l'une des questions les plus importantes et ouvertes en informatique théorique. Elle affirme que :
>
> $$P \neq NP$$
>
> C'est-à-dire que vérifier une solution en temps polynomial est strictement plus puissant que trouver une solution en temps polynomial.

## Signification

> [!abstract]+ Interprétation
> **Si P ≠ NP** :
> - Il existe des problèmes dans NP qui ne sont pas dans P
> - Les problèmes NP-complets n'ont pas d'algorithme polynomial
> - Vérifier est fondamentalement plus facile que résoudre
>
> **Si P = NP** :
> - Tout problème dans NP est dans P
> - Les problèmes NP-complets ont des algorithmes polynomiaux
> - Vérifier et résoudre ont la même difficulté
> - Conséquences révolutionnaires pour la cryptographie, l'optimisation, etc.

## État de la Question

> [!warning]+ Statut Actuel
> **Non démontré** :
> - Aucune preuve de P ≠ NP
> - Aucune preuve de P = NP
>
> **Consensus** :
> - La grande majorité des chercheurs croient que P ≠ NP
> - Basé sur des décennies de recherches infructueuses d'algorithmes polynomiaux
>
> **Prix du Millénaire** :
> - Un des sept problèmes du Clay Mathematics Institute
> - Récompense de 1 million de dollars pour une solution

## Arguments Heuristiques

> [!tip]+ Pourquoi P ≠ NP est Probable
> **Effort de recherche** :
> - Des milliers de chercheurs pendant 50+ ans
> - Aucun algorithme polynomial trouvé pour SAT
> - Aucun algorithme polynomial pour les autres problèmes NP-complets
>
> **Diversité des problèmes** :
> - Les problèmes NP-complets proviennent de domaines très variés
> - Si P = NP, ils auraient tous des algorithmes polynomiaux similaires
> - Cela semble peu plausible
>
> **Barrières de preuve** :
> - Plusieurs techniques de preuve connues ne peuvent pas résoudre P vs NP
> - Résultats de "relativisation" et "natural proofs"

## Conséquences si P = NP

> [!example]+ Implications
> **Cryptographie** :
> - La plupart des systèmes cryptographiques deviendraient inutiles
> - Factorisation en temps polynomial → RSA cassé
>
> **Optimisation** :
> - Tous les problèmes NP-complets résolubles efficacement
> - Révolution dans la logistique, la planification, etc.
>
> **Mathématiques** :
> - Prouver des théorèmes deviendrait automatisable
> - Si on peut vérifier une preuve, on peut la trouver
>
> **Intelligence Artificielle** :
> - Apprentissage automatique facilité
> - Résolution de problèmes complexes

## Conséquences si P ≠ NP

> [!example]+ Implications
> **Limites fondamentales** :
> - Certains problèmes sont intrinsèquement difficiles
> - Pas d'algorithme général efficace pour l'optimisation
>
> **Cryptographie** :
> - Base solide pour la sécurité
> - Les systèmes actuels restent sûrs (sous certaines hypothèses)
>
> **Approches alternatives** :
> - Développement d'algorithmes d'approximation
> - Heuristiques et algorithmes randomisés
> - Résolution de cas particuliers

## Variantes de la Question

> [!abstract]+ Questions Connexes
> **Autres séparations ouvertes** :
> - NP vs co-NP
> - NP vs PSPACE
> - P vs PSPACE
>
> **Questions plus faibles** :
> - Existe-t-il un algorithme sous-exponentiel pour SAT ?
> - Existe-t-il un algorithme $O(n^{100})$ pour 3-SAT ?

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Classe P]]** : Problèmes "faciles"
> - **[[Classe NP]]** : Problèmes vérifiables efficacement
> - **[[Classe NP#NP-Complet]]** : Problèmes les plus difficiles de NP
> - **[[Conséquence de la Complétude]]** : Implications de la NP-complétude
