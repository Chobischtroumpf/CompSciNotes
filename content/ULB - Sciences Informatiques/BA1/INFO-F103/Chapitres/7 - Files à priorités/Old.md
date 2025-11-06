---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

Les tas (heaps) sont des structures de données de type arbre binaire qui respectent la propriété de tas: chaque nœud est plus grand (dans un max-tas) ou plus petit (dans un min-tas) que ses enfants. Cette propriété permet d'accéder rapidement au plus grand ou au plus petit élément, ce qui rend les tas utiles pour des applications comme les files à priorités.

Les files à priorités sont des structures de données qui permettent de stocker des éléments avec une certaine priorité. Les éléments de plus haute priorité sont servis avant ceux de moindre priorité. Les tas sont souvent utilisés pour implémenter les files d'attente à priorité car ils permettent des insertions et des suppressions efficaces tout en maintenant l'ordre de priorité.
## Méthodes sur un tas
[[Chap 07 - slides_heap.pdf#Heap]]
### Insertion
1. **Ajouter à la fin du tableau**: L'élément à insérer est ajouté à la fin du tableau qui représente le tas.
2. **Réordonner**: L'élément ajouté est comparé avec sa racine (le parent), puis avec la racine de la racine (le grand-parent), etc., jusqu'à ce qu'il soit placé dans une position qui respecte la propriété du tas.
### Suppression
1. **Enlever l'élément le plus grand / le plus petit (la racine)**: La racine du tas, qui est l'élément le plus grand dans un tas max ou le plus petit dans un tas min, est supprimée.
2. **Réordonner**: Le dernier élément du tableau est déplacé au premier pour remplacer la racine supprimée. Ensuite, cet élément est comparé avec ses enfants pour trouver le plus grand (dans un max-tas) ou le plus petit (dans un min-tas) et est échangé avec lui si nécessaire. Ce processus est répété jusqu'à ce que la propriété du tas soit restaurée.
### Tri par tas (Heap Sort)
1. **Transformer un tableau en tas**: Cela peut être fait en utilisant la méthode de tasification sur l'ensemble du tableau ou en insérant chaque élément un par un dans un nouvel tas.
2. **Supprimer depuis le tas**: Les éléments sont supprimés un par un du tas (toujours la racine) jusqu'à ce que le tas soit vide. Les éléments supprimés sont placés dans l'ordre dans le tableau, ce qui résulte en une séquence triée.
### Tasification (Heapify)
1. **Commencer par la fin**: Le processus commence au dernier parent du tableau.
2. **Vérifier les enfants**: Pour chaque nœud examiné, vérifier s'il a des enfants.
3. **Comparer et échanger**: Si un nœud a des enfants, comparer leurs valeurs et, si nécessaire, échanger le parent avec le plus grand (dans un tas max) ou le plus petit (dans un tas min) des enfants pour respecter la propriété du tas.
4. **Répéter**: Ce processus est répété pour chaque parent dans le tableau, en remontant jusqu'à la racine.
