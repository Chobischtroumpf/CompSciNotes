---
title: Démonstration Problème Indécidable
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Objectif
> Montrer qu'un problème donné est **indécidable** par réduction depuis le problème de l'arrêt.

## Problème à Démontrer

> [!abstract]+ Énoncé
> **Problème de l'Équivalence de Programmes**
>
> **Entrée** : Deux programmes $P$ et $Q$ qui retournent tous les deux une valeur booléenne
>
> **Question** : Les deux programmes sont-ils équivalents ?
> $$\forall x, P(x) = Q(x) \text{ ?}$$

## Stratégie de Preuve

> [!abstract]+ Méthode
> **Réduction depuis le problème de l'arrêt** (connu indécidable)
>
> - Si on pouvait décider l'équivalence de programmes
> - Alors on pourrait décider le problème de l'arrêt
> - Or le problème de l'arrêt est indécidable
> - Donc l'équivalence de programmes est indécidable

## Rappel : Problème de l'Arrêt

> [!warning]+ Indécidable
> **Entrée** : Un programme $R$ et une entrée particulière $x_0$
>
> **Question** : Le programme $R$ s'arrête-t-il sur l'entrée $x_0$ ?
>
> **Théorème de Turing (1936)** : Ce problème est indécidable.

## Construction de la Réduction

> [!abstract]+ Transformation
> Étant donné :
> - Un programme $R$
> - Une entrée particulière $x_0$ de $R$
>
> **On construit deux programmes** :

### Programme AUX

> [!example]+ Définition
> ```
> procedure AUX(x):
>     r := R(x0)
>     return 1
> ```
>
> **Comportement** :
> - Exécute $R$ sur l'entrée fixe $x_0$
> - Ignore complètement son paramètre $x$
> - Retourne 1 si $R(x_0)$ termine
> - **Ne retourne rien** si $R(x_0)$ ne s'arrête pas (boucle infinie)

### Programme CONST

> [!example]+ Définition
> ```
> procedure CONST(x):
>     return 1
> ```
>
> **Comportement** :
> - Ignore son paramètre $x$
> - S'arrête toujours
> - Retourne toujours 1

## Analyse de la Différence

> [!abstract]+ Observation Clé
> **Différence fondamentale** :
> - `CONST(x)` s'arrête **toujours** et retourne 1
> - `AUX(x)` retourne 1 **seulement si** $R(x_0)$ s'arrête
>
> **Comportements possibles** :
>
> | Cas | $R(x_0)$ | `AUX(x)` | `CONST(x)` | Équivalents ? |
> |-----|----------|----------|------------|---------------|
> | 1 | S'arrête | Retourne 1 | Retourne 1 | **OUI** |
> | 2 | Ne s'arrête pas | Boucle ∞ | Retourne 1 | **NON** |

## Preuve de Correction

> [!abstract]+ Équivalence
> **Théorème** : `AUX` et `CONST` sont équivalents si et seulement si $R$ s'arrête sur $x_0$.
>
> **Preuve ($\Rightarrow$)** :
> - Supposons que `AUX` et `CONST` sont équivalents
> - C'est-à-dire : $\forall x, \text{AUX}(x) = \text{CONST}(x)$
> - En particulier : pour toute entrée $x$, `AUX(x)` retourne 1
> - Donc `AUX(x)` termine toujours
> - Donc $R(x_0)$ termine (car c'est ce qu'exécute `AUX`)
> - Donc $R$ s'arrête sur $x_0$ ✓
>
> **Preuve ($\Leftarrow$)** :
> - Supposons que $R$ s'arrête sur $x_0$
> - Alors pour toute entrée $x$ :
>   - `AUX(x)` exécute $R(x_0)$ qui termine
>   - `AUX(x)` retourne 1
>   - `CONST(x)` retourne 1
> - Donc $\forall x, \text{AUX}(x) = \text{CONST}(x) = 1$
> - Donc `AUX` et `CONST` sont équivalents ✓

## Conclusion de la Réduction

> [!success]+ Résultat
> **On a construit une réduction du problème de l'arrêt vers le problème d'équivalence** :
>
> $$R \text{ s'arrête sur } x_0 \Leftrightarrow \text{AUX et CONST sont équivalents}$$
>
> **Conséquence** :
> - Si le problème d'équivalence était décidable
> - On pourrait décider le problème de l'arrêt
> - Or le problème de l'arrêt est indécidable (Turing, 1936)
> - **Donc le problème d'équivalence est indécidable**

## Généralisation de la Méthode

> [!tip]+ Technique Standard
> **Pour montrer qu'un problème $B$ est indécidable** :
>
> 1. Choisir un problème $A$ connu indécidable (souvent : problème de l'arrêt)
> 2. Construire une transformation qui, pour toute instance de $A$ :
>    - Crée une instance de $B$
>    - Préserve la réponse : $A$ a solution $\Leftrightarrow B$ a solution
> 3. Conclure : si $B$ était décidable, $A$ le serait aussi
> 4. Donc $B$ est indécidable
>
> **Note** : Contrairement aux réductions pour NP-dureté, pas besoin que la transformation soit en temps polynomial (le problème est indécidable de toute façon).

## Autres Exemples

> [!example]+ Problèmes Indécidables Similaires
> **Par la même technique, on peut montrer indécidable** :
>
> - **Terminaison** : Un programme $P$ s'arrête-t-il sur toute entrée ?
> - **Correction** : Un programme $P$ satisfait-il sa spécification ?
> - **Atteignabilité** : Une ligne de code est-elle atteignable ?
> - **Comportement** : Un programme imprime-t-il jamais "Hello" ?

## Remarques

> [!warning]+ Observations Importantes
> **Différence avec NP-complétude** :
> - Problème NP-complet : difficile, mais décidable
> - Problème indécidable : impossible à décider (même avec temps infini)
>
> **Approximation impossible** :
> - Pour les problèmes NP-complets, on peut faire de l'approximation
> - Pour les problèmes indécidables, même l'approximation est impossible
>
> **Implications pratiques** :
> - Pas d'analyseur statique parfait
> - Pas de vérificateur automatique complet
> - Nécessité de techniques partielles (tests, vérification partielle, etc.)

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème Indécidable#Problème de l'Arrêt]]** : Problème source standard
> - **[[Réduction Polynomiale]]** : Technique similaire mais pour NP-dureté
> - **[[Algorithme de Décision]]** : Ce qui n'existe pas pour ces problèmes
> - **[[Problème Indécidable#Autres Problèmes Indécidables]]** : Plus d'exemples
