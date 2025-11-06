---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

On parle de récursivité lorsqu’on est confronté à une définition qui fait référence à elle-même.

Pour pouvoir parler d’une définition récursive d’un objet, celle-ci doit respecter les trois propriétés suivantes:
1. Une référence directe ou indirecte à un objet identique doit apparaître;
2. Un cas simple, sans référence directe ou indirecte à un objet identique, doit être défini explicitement;
3. La notion de "taille" doit apparaître, et ainsi les références directes ou indirectes doivent se faire vers des objets identiques mais "plus petits" de manière à se diriger vers le cas simple.

- **Récursivité directe:** Se produit lorsqu'une fonction ou méthode s'appelle elle-même directement.
- **Récursivité indirecte / croisée:** Se produit lorsqu'une fonction ou méthode appelle une autre fonction ou méthode, qui à son tour en appelle une autre, et ce processus continue jusqu'à ce que la fonction ou méthode originale soit appelée à nouveau, formant ainsi une chaîne d'appels récursifs indirects.

Une méthode ou fonction récursive doit être structurée clairement de manière à exposer le cas simple et le traitement de la partie récursive.
### Exemples de récursivité
- [[Chap 02 - slides_recursivite.pdf#Factorielle récursive]]
- [[Chap 02 - slides_recursivite.pdf#Fibonacci récursif]]
- [[Chap 02 - slides_recursivite.pdf#Changement de base récursive]]
- [[Chap 02 - slides_recursivite.pdf#Conversion d'une expression infixe en postfixe]] + [[Chap 02 - slides_recursivite.pdf#Evaluation d’une expression infixe]]

*Lors d’appels récursifs, comme pour tout appel de fonction ou méthode, quand une fonction ou méthode se termine, le contrôle retourne à la fonction ou méthode appelante. Chaque appel initialise un nouveau contexte avec de nouveaux paramètres et variables locales.*

On a donc besoin d’une pile pour gérer les sauvegardes des contextes des fonctions et méthodes successivement appelées (pas besoin en Python).

- Il faut donc veiller à minimiser le nombre de variables locales ou de paramètres dans une telle fonction ou méthode récursive.

*Si un algorithme peut souvent être écrit d’une manière récursive, ce n’est pas toujours pour autant la forme la plus naturelle, ni surtout la plus efficace pour réaliser cet algorithme.*
### Exemples de fausses récursivités
Toutes ces versions itératives n’utilisent pas de pile. Il s’agit donc de fausses récursivités.
- [[Chap 02 - slides_recursivite.pdf#Factorielle itérative]]
- [[Chap 02 - slides_recursivite.pdf#Fibonacci itératif]]
- [[Chap 02 - slides_recursivite.pdf#Changement de base itérative]]
- [[Chap 02 - slides_recursivite.pdf#Problème consistant à trouver la plus grande valeur contenue dans une liste non triée de n éléments]]
- [[Chap 02 - slides_recursivite.pdf#Recherche séquentielle dans une liste]]
- [[Chap 02 - slides_recursivite.pdf#Recherche séquentielle dans une liste triée]]
- [[Chap 02 - slides_recursivite.pdf#Recherche dichotomique itérative]]

**La "vraie" récursivité ne peut se passer d’une pile.** Ainsi, nous pouvons avancer que la récursivité implique l’usage d’une pile (et que bien sûr l’usage d’une pile dans un algorithme n’implique en rien la présence de récursivité).

Il est parfois possible de résoudre des problèmes au moyen d’algorithmes effectuant deux appels récursifs portant chacun sur plus ou moins la moitié des données. C’est ce qu’on appelle **divide and conquer.**
### Exemples de divide & conquer
- [[Chap 02 - slides_recursivite.pdf#Recherche dichotomique]]
- [[Chap 02 - slides_recursivite.pdf#Version divide and conquer]]
