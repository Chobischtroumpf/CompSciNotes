---
title: Algorithme de Lempel-Ziv-Welch
authors: Alessandro Dorigo
tags: []
---

> [!note] Encodage
> On initialise d'abord un dictionnaire avec les symboles individuels
> On va ensuite repeter les étapes suivantes:
> - Trouver la plus longue chaîne w de symboles successifs présente dans le dictionnaire
> - Ecrire l’indice de cette chaîne dans le dictionnaire
> - Ajouter la chaîne wc dans le dictionnaire, où c est le symbole suivant en entrée

> [!note] Décodage
> - Initialiser le dictionnaire
> - décoder le premier indice
> - ajouter celui-ci au dictionnaire
> - Répéter:
> 	- Décoder le premier symbole s de la chaîne correspondant à l’indice suivant
> 	- Remplacer ? par s dans la chaîne précédemment ajoutée au dictionnaire
> 	- Décoder le reste de la chaîne w correspondant à l’indice courant
> 	- Ajouter w ? au dictionnaire
