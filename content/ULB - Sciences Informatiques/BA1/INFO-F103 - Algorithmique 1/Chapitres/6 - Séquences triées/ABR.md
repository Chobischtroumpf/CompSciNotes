---
title: ABR
authors: Alessandro Dorigo
tags:
  - Algo
---


| ![[549bffc8939997b9729ced49f8586b60.png]] | Chaque nœud est défini comme ceci:<br>![[10b9ae83699f89440c4aa48bfedf92f6.png]] |
| :----------------------------------: | :------------------------------------------------------------------------: |

### Recherche d'un élément dans un ABR
1. **Comparer `x` à la valeur `y` dans la racine**: Si `x` est égal à `y`, la recherche est terminée.
2. **Direction vers le sous-arbre gauche**: Si `x` est strictement inférieur à `y`, continuer la recherche dans le sous-arbre gauche.
3. **Direction vers le sous-arbre droit**: Si `x` est strictement supérieur à `y`, poursuivre la recherche dans le sous-arbre droit.
4. **Répétition récursive**: Répéter le processus de manière récursive sur le sous-arbre approprié jusqu'à ce que `x` soit trouvé ou qu'une feuille soit atteinte sans trouver `x`.
### Premier élément d'un ABR
Le premier élément (le plus petit) d'un ABR se trouve en suivant continuellement le sous-arbre gauche à partir de la racine jusqu'à atteindre la feuille la plus à gauche.
### Dernier élément d'un ABR
Le dernier élément (le plus grand) d'un ABR se trouve en parcourant continuellement le sous-arbre droit à partir de la racine jusqu'à atteindre la feuille la plus à droite.
### Élément suivant dans un ABR
1. **Si le nœud a un sous-arbre droit**: Le suivant est le premier élément (le plus à gauche) de ce sous-arbre droit.
2. **Si le nœud n'a pas de sous-arbre droit**: Remonter l'arbre jusqu'à trouver un nœud qui est un fils gauche. Le parent de ce nœud est le suivant.
### Élément précédent dans un ABR
1. **Si le nœud a un sous-arbre gauche**: Le précédent est le dernier élément (le plus à droite) de ce sous-arbre gauche.
2. **Si le nœud n'a pas de sous-arbre gauche**: Remonter l'arbre jusqu'à trouver un nœud qui est un fils droit. Le parent de ce nœud est le précédent.
### Suppression d'un élément dans un ABR
1. **Localiser `x`**: Utiliser la recherche pour trouver le nœud contenant `x`.
2. **Si `x` n'a pas de fils**: Il suffit de le supprimer et de relier son parent à `null`.
3. **Si `x` a qu'un fils gauche**: Supprimer `x` et relier son parent directement au fils unique de `x`.
4. **Si `x` a un fils droit**:
	a. Trouver le successeur de `x` (l'élément le plus à gauche du sous-arbre droit de `x`).
    b. Remplacer la valeur de `x` par celle de son successeur.
    c. Supprimer le successeur (qui se trouve maintenant dans une position où il a au plus un fils).

La suppression d'un élément dans un ABR nécessite de maintenir les propriétés de l'ABR, assurant ainsi que chaque nœud soit plus grand que tous les éléments dans son sous-arbre gauche et plus petit que ceux dans son sous-arbre droit. Cette opération peut nécessiter un rééquilibrage de l'arbre, selon l'implémentation spécifique de l'ABR (comme dans le cas d'un AVL ou d'un arbre rouge-noir).
