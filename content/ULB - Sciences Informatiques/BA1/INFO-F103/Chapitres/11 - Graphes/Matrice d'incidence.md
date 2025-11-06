---
title: Matrice d'incidence
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> - La matrice d'incidence $I$ est une Matrice de taille $n \times m$, pour ($|S| = n, |A| = m$) nous donnant une information sur la relation entre un sommet et un arc ou arête.
> - L'information se trouvant en $I_{i,j}$ indique si l'arc ou arête $j$ provient ou pointe vers le sommet $i$.

^3bcff9

> [!abstract]- À savoir
>Elle peut être représentée de plusieurs façons différentes:
>- Pour un graphe orienté on peut utiliser plusieurs méthodes;
>- Dans le cas d'un graphe dirigé avec boucles, on peut définir $I_{i,j}$ tel que:
> $$I_{i,j} = \begin{cases} (V,F) & \text{si l'arc part du sommet } i \\ (F,V) & \text{si l'arc arrive au sommet } j \\ (F,F) & \text{si l'arc n'est pas lié au sommet} \\ (V,V) & \text{si l'arc fait une boucle}\end{cases}$$
> ![[Pasted image 20240501133012.png]]
>- Ou alors, dans le cas d'un graph sans boucle, on peut définir $I_{i,j}$ tel que :
> $$I_{i,j} = \begin{cases} 1 & \text{si l'arc } (i,j) \text{ part du sommet } i \\ -1 & \text{si l'arc } (i,j) \text{ arrive au sommet } j \\ 0 & \text{ si l'arc n'est pas lié au sommet} \end{cases}$$
>![[Pasted image 20240501134040.png]]
>- Pour un graphe non-orienté, on peut définir $I_{i,j}$ tel que :
> $$I_{i,j} = \begin{cases} 1 & \text{si l'arête } (i,j) \text{ relie le sommet } i \text{ et le sommet } j \\ 0 & \text{si aucune arête ne relie les deux sommets} \end{cases}$$
> ![[Pasted image 20240501133213.png]]
