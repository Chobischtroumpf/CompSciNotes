---
title: Matrice Laplacienne
authors: Alessandro Dorigo
tags:
  - MathDis
  - Complements
---


> [!info]+ Définition
> La **matrice Laplacienne** d’un [[Graphe (théorie des graphes)#^ca541f|graphe]] $G$ est la matrice $L = (L_{i,j})$ avec
>
> $$L_{i,j} := \begin{cases} d_i & \text{si } i = j \\ -1 & \text{si } i \neq j, \, ij \in E(G) \\ 0 & \text{sinon} \end{cases}$$

> [!example]+ Exemple
> ![[Pasted image 20241212142444.png]]
>
> **Remarque:** $L = D - A$ où
> ![[Pasted image 20241212142538.png]]
>
> $L$ est une matrice symétrique réelle $n \times n \Rightarrow n$ valeurs propres dans $\mathbb{R} : \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$.

**Fait:** $\lambda_i \geq 0 \quad \forall i$, car
$$x^TLx = \sum_{ij \in E(G)} (x_i - x_j)^2 \geq 0$$
De plus, $\lambda_1 = 0$ car $L \cdot \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} \implies \det(L) = \lambda_1 \lambda_2 \cdots \lambda_n = 0$.

![[Pasted image 20241212143356.png]]
![[Pasted image 20241212143407.png]]

> [!abstract]- Théorème de Kirchhoff 10.5.1
> Tous les cofacteurs de $L = L(G)$ sont égaux au nombre d'[[Arbre (théorie des graphes)#^d6e627|arbres couvrants]] de $G$.
> - De plus, ce nombre est
>   $$\frac{1}{n} \lambda_2 \cdots \lambda_n$$
