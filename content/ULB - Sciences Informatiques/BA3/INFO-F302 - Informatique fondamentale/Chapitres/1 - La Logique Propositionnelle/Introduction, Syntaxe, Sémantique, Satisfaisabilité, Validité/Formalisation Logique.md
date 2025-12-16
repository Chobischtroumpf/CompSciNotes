---
title: Formalisation Logique
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **formalisation logique** est le processus de traduction d'énoncés en langage naturel vers des formules de la logique propositionnelle, permettant ainsi un raisonnement formel.

## Exemples de Formalisation

> [!example]+ Exemple du Train et du Taxi
> **Énoncés en langage naturel** :
> 1. Le train est arrivé en retard
> 2. Il y a des taxis à la gare
> 3. L'invité est en retard
>
> **Propositions** :
> - $p$ : Le train est arrivé en retard
> - $q$ : Il y a des taxis à la gare
> - $r$ : L'invité est en retard
>
> **Formalisation** :
> 1. Hypothèse : $(p \land \neg q) \rightarrow r$
> 2. Hypothèse : $p$
> 3. Hypothèse : $\neg r$
> 4. Déduction : $\neg q \rightarrow r$
> 5. Déduction : comme $\neg r$, alors $q$

> [!example]+ Exemple du Parapluie
> **Énoncés en langage naturel** :
> 6. Il pleut
> 7. L'invité a son parapluie
> 8. L'invité est mouillé
>
> **Propositions** :
> - $p$ : Il pleut
> - $q$ : L'invité a son parapluie
> - $r$ : L'invité est mouillé
>
> **Formalisation** :
> 1. Hypothèse : $(p \land \neg q) \rightarrow r$
> 2. Hypothèse : $p$
> 3. Hypothèse : $\neg r$
> 4. Déduction : $\neg q \rightarrow r$
> 5. Déduction : comme $\neg r$, alors $q$

## Correspondance

> [!abstract]+ Table de Correspondance
> | Exemple du Train | Exemple du Parapluie | Proposition |
> |:----------------:|:--------------------:|:-----------:|
> | Le train est arrivé en retard | Il pleut | $p$ |
> | Il y a des taxis à la gare | L'invité a son parapluie | $q$ |
> | L'invité est en retard | L'invité est mouillé | $r$ |

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Bachus-Naur Form]]** : Syntaxe formelle des formules
> - **[[Déduction Naturelle]]** : Système pour déduire des conclusions
> - **[[Fonction d'Interprétation]]** : Attribution de valeurs de vérité
