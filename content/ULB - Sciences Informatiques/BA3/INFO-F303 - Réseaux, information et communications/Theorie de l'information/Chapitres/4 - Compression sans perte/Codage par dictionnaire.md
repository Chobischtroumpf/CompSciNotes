---
title: Codage par dictionnaire
authors: Alessandro Dorigo
tags: []
---

> [!note]+ Idée
> Le but est de stocker les sous-chaines de caracteres du message dans un dictionnaire (couples indice-chaîne de caractères)
> Si des longues sous-chaînes sont fréquentes, les substituer par leurs indices comprime le message.
>
> Challenge:
> - Éviter la transmission du dictionnaire
> - Permettre la construction à la volée pendant le codage et décodage

> [!abstract]+ Algorithme de Lempel-Ziv
> L'algorithme de Lempel-Ziv effectue un **codage et décodage à la volée**.
>
> Le dictionnaire contient toutes les sous-chaînes de caractères (de longueur ≤b\leq b ≤b) apparues récemment (commençant au plus ww w caractères plus tôt).
>
> Le codage est une **suite de chaînes de caractères**, chacune représentée par un tuple (ℓ,d,s)(\ell, d, s) (ℓ,d,s) où :
>
> - ℓ≥0\ell \geq 0 ℓ≥0 : longueur de la chaîne apparue récemment
> - d≥0d \geq 0 d≥0 : position de cette chaîne (distance au caractère courant)
> - ss s : caractère suivant dans le message
> - ℓ=0\ell = 0 ℓ=0 et d=−1d = -1 d=−1 si nouveau caractère

> [!tip]+ Propriétés
>
> Le codage correspond à une **référence du dictionnaire + symbole suivant**.
>
> Il n'y a **pas besoin de transmettre le dictionnaire** (il est reconstruit à la volée).
>
> **Taux de compression** :
>
> - Négatif pour l'exemple (trop court) ci-dessus
> - Meilleur si longues chaînes proches répétées souvent
>
> Pour une fenêtre et un tampon suffisamment longs, la longueur du message compressé tend vers celle obtenue avec un code de Huffman.
>
> ### **Décodage**
>
> En procédant de la même manière, on peut **reconstruire le message et le dictionnaire à partir du code**.
