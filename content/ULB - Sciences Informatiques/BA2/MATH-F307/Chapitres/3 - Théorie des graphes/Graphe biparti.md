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
|                    ![[Pasted image 20241002093358 1.png]]                     |                      ![[D49FABA6-5654-496D-8925-5719B036035D.png]]                       | ![[1934A5B5-C2DC-47A7-8552-6F1A58E34C7E.png]] |
| :---------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: | :---------------------------------------------: |
|                   $K_n$ = [[Graphe complet]] à $n$ sommets                    | $K_{m,n}$ graphe [[Graphe biparti#^bff5b9\|biparti]] [[Graphe complet#^673d8c\|complet]] |              Étoile à $n$ sommets               |
|                          $V(K_n) := \{1,2,\dots,\}$                           |                                                                                          |                                                 |
| $E(K_n) := \bigl\{ij \mid i,j \in \{1,2, \dots ,n\} \text{ et } i < j\bigl\}$ |                                                                                          |                                                 |
|                            $\Delta(K_n) := n - 1$                             |                           $\Delta(K_{m,n}) = \text{max } m,n$                            |                 $\Delta = n-1$                  |
|                         $\chi(K_n) := n = \Delta + 1$                         |                                  $\chi(K_{m,n}) \leq 2$                                  |                   $\chi = 2$                    |

> [!abstract]- Théorème 3.10.1
> Si le [[Degré#^3c01ed|degré]] maximum d’un graphe $G$ est $\Delta$, alors $\chi(G) ≤ \Delta + 1$.
>
> ![[Pasted image 20241001120951.png]]
> ![[Pasted image 20241001121001.png]]

> [!abstract]- Théorème 3.10.2
> $G$ est [[Graphe biparti#^bff5b9|biparti]] $\iff G$ ne contient pas de [[Cycle (théorie des graphes)#^4c6fe0|cycle]] impair.
>
> ![[Pasted image 20241001121157.png]]
> ![[Pasted image 20241001121203.png]]
