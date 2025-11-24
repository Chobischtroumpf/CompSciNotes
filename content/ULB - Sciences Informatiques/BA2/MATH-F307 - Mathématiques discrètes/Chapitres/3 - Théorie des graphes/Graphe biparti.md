---
title: Graphe biparti
authors: Alessandro Dorigo
tags:
  - Graphe
---


> [!info]+ Définition
> Un graphe $G$ est dit **biparti** si $\chi(G) ≤ 2$ (on peut le colorier avec au plus $2$ couleurs).
^bff5b9

> [!note]
> Un cycle à $n$ sommets $C_n$ est biparti ssi $n$ est pair.
# Propriétés
|                    ![[3cf7b112340a5e7e5f2ddf4c75fc169f.png]]                     |                      ![[13716b66738ca4b77e2e7fbae4eddb6a.png]]                       | ![[f21ce5bc39067233f354c47c0fb61e51.png]] |
| :---------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: | :---------------------------------------------: |
|                   $K_n$ = [[Graphe complet]] à $n$ sommets                    | $K_{m,n}$ graphe [[Graphe biparti#^bff5b9\|biparti]] [[Graphe complet#^673d8c\|complet]] |              Étoile à $n$ sommets               |
|                          $V(K_n) := \{1,2,\dots,\}$                           |                                                                                          |                                                 |
| $E(K_n) := \bigl\{ij \mid i,j \in \{1,2, \dots ,n\} \text{ et } i < j\bigl\}$ |                                                                                          |                                                 |
|                            $\Delta(K_n) := n - 1$                             |                           $\Delta(K_{m,n}) = \text{max } m,n$                            |                 $\Delta = n-1$                  |
|                         $\chi(K_n) := n = \Delta + 1$                         |                                  $\chi(K_{m,n}) \leq 2$                                  |                   $\chi = 2$                    |

> [!abstract]- Théorème 3.10.1
> Si le [[Degré#^3c01ed|degré]] maximum d’un graphe $G$ est $\Delta$, alors $\chi(G) ≤ \Delta + 1$.
>
> ![[5f057785a6d2c24e080c8a2b7915b69a.png]]
> ![[deee116748a5ff334305a1922d3c5833.png]]

> [!abstract]- Théorème 3.10.2
> $G$ est [[Graphe biparti#^bff5b9|biparti]] $\iff G$ ne contient pas de [[Cycle (théorie des graphes)#^4c6fe0|cycle]] impair.
>
> ![[a4349c0ea240f2248bc653c654fdf515.png]]
> ![[bfd9b9cf2e977d5a68fa047316447a58.png]]
