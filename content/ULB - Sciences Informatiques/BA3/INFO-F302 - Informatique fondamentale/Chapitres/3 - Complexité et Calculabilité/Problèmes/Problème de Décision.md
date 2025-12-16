---
title: Problème de Décision
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Un **problème de décision** est un problème dont la réponse est "oui" ou "non". On peut le définir formellement comme un langage de mots sur un alphabet fini $\Sigma$.

## Formalisation

> [!abstract]+ Langage et Alphabet
> **Définitions** :
> - $\Sigma$ : un alphabet fini
> - $\Sigma^*$ : l'ensemble de tous les mots sur $\Sigma$ (incluant le mot vide $\epsilon$)
> - Un **langage** sur $\Sigma$ : un sous-ensemble $L \subseteq \Sigma^*$
>
> **Exemple** : $\Sigma = \{0, 1\}$, alors $00100 \in \Sigma^*$

## Problème de Décision comme Langage

> [!abstract]+ Représentation
> Un problème de décision = un langage $P \subseteq \Sigma^*$
>
> **Fonction caractéristique** :
> $$\chi_P : \Sigma^* \to \{0, 1\}$$
> $$u \mapsto \begin{cases}
> 1 & \text{si } u \in P \\
> 0 & \text{si } u \notin P
> \end{cases}$$

> [!tip]+ Interprétation
> Chaque langage $P$ représente un problème dont la réponse est "oui" ou "non", en l'identifiant à sa fonction caractéristique $\chi_P$

## Exemples

> [!example]+ Problèmes Classiques
> **SAT (Satisfiabilité)** :
> - Entrée : Une formule propositionnelle en FNC
> - Sortie : "oui" ssi la formule est satisfaisable
>
> **Coloriage de Graphes** :
> - Entrée : Un graphe $G$ et un entier $k$
> - Sortie : "oui" ssi $G$ est coloriable avec au plus $k$ couleurs
>
> **2-Partition** :
> - Entrée : $n$ entiers $c_1, ..., c_n$ avec $S = \sum c_i$ paire
> - Sortie : "oui" ssi il existe $J \subseteq \{1, ..., n\}$ tel que $\sum_{i \in J} c_i = S/2$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème d'Optimisation]]** : Version avec maximisation/minimisation
> - **[[Algorithme de Décision]]** : Algorithme résolvant un problème de décision
> - **[[Classe P]]** : Problèmes décidables en temps polynomial
> - **[[Classe NP]]** : Problèmes vérifiables en temps polynomial
