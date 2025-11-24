---
title: Arbre de code
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!info]+ Définition
> Un **arbre de code** est une représentation arborescente d'un [[Code sans préfixe#^392e5f|code sans préfixe]] où chaque chemin de la racine vers une feuille correspond à un mot du code.

^4606d7

> [!abstract]- Structure de l'arbre
> - **Racine**: correspond au mot vide
> - **Sommets internes**: correspondent à des préfixes des mots du code (mot de $C^*$)
> - **Feuilles**: correspondent aux **mots du code**
> - **Arêtes**: étiquetées par les symboles de l'alphabet $C$

> [!abstract]- Propriétés
> - **Degré** de l'arbre $\leq r$ (taille de l'alphabet $\vert C \vert$)
> - **Hauteur** de l'arbre $= \ell_{\max}$ (longueur maximale des mots du code)
> - **Correspondance bijective**: arbre de code $\Leftrightarrow$ code sans préfixe

> [!example]+ Exemple
> ![[a13ca9da19b06130fa06103f3757359a.png]]

> [!abstract]- Algorithme de décodage
> 1. Commencer à la racine
> 2. Pour chaque bit/symbole lu, suivre l'arête correspondante
> 3. Si on atteint une feuille: symbole décodé, retourner à la racine
> 4. Répéter jusqu'à la fin de la séquence
