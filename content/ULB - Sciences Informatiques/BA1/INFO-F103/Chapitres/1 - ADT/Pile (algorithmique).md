---
title: Pile (algorithmique)
authors: Alessandro Dorigo
tags:
  - Algo
---


Formellement appris en `INFO-F103`. Pour les piles internes vues en `INFO-F201`, voir *link*.

> [!info]+ Définition
> Une **pile** est une [[Structure de données (algorithmique)#^d1977b|structure de données]] qui suit le principe **LIFO** (_Last In, First Out_), où le dernier élément inséré est le premier à être retiré.
>
> ![[Pasted image 20241015154837.png]]
>
> [[Chap 01 - slides_adt.pdf#Pile (sans Node)]] / [[Chap 01 - slides_adt.pdf#Pile (avec Node)]]

> [!tip]+ Pour visualiser:
> On peut imaginer une pile de livres, où le dernier livre posé sur la pile est le premier à être retiré.

> [!abstract]- Interface d'une pile
> - `push`: rajout d’un élément en haut de la pile
> - `pop`: retrait d’un élément du haut de la pile
> - `top`: indique la valeur de l’élément se trouvant "au sommet" de la pile
> - `isEmpty`: indique si la pile est vide ou non
> - `size`: indique le nombre d’éléments présents dans la pile
## Pile (vecteur)
![[Pasted image 20241015155127.png]]
## Pile (pointeurs)
![[Pasted image 20240206164613.png]]
