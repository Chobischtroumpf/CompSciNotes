---
title: Algorithme de Vitter
authors: Alessandro Dorigo
tags: []
---
> [!info]+ Définition
>
> **Ordre implicite** : de bas en haut, puis de gauche à droite.
>
> **Bloc** : ensemble de tous les noeuds de même _poids_ et de même _type_ (feuille vs sommet interne).
>
> Les blocs et les noeuds d'un même bloc sont ordonnés implicitement.
>
> **Leader** : le plus grand noeud d'un bloc (le plus haut, ou le plus à droite en cas d'égalité).
>
> **Invariant de Vitter à conserver** : une feuille précède ($<$) toujours un noeud de même poids.
>
> **Feuille symbole inconnu** $\emptyset$ : symbole pas encore rencontré.

> [!tip]+ Fonctionnement
>
> **Émission du code :**
>
> - L'arbre est initialisé avec le symbole inconnu $\emptyset$ en racine
> - Le symbole à coder $X$ est cherché dans l'arbre
> - S'il y est, on émet le mot de code associé à $X$ ($\sim$ chemin de l'arbre menant à $X$)
> - Sinon, on émet le mot de code associé à $\emptyset$ suivi de $X$, et on remplace le noeud $\emptyset$ par un noeud interne ayant deux fils : $\emptyset$ (à gauche) et $X$ (à droite)
>
> **Mise à jour de l'arbre :**
>
> On remonte du sommet codé vers la racine :
>
> - On incrémente le sommet en cours
> - On le place au bout (ordre minimal, en bas à gauche) de son nouveau bloc (poids $+1$, même type)
> - Ceci nécessite de permuter des sommets du même bloc entre eux (ainsi que leurs sous-arbres)

> [!tip]+ Exemple
> ![[b061c195c778d9faaaa9fc80fc6e6faf.png]]
> ![[432852f353ad0d1e868eb472172ffa84.png]]
> ![[0e85655f628351ce14c4d8b59954280f.png]]
> ![[89a36f1e69fef9a6b3aa499207e3eac0.png]]
> ![[d6299f49138c9ee8a920fadf7ab1a0fa.png]]
