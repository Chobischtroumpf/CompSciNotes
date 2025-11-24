---
title: Mergesort (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
  - Algo
---


Formellement appris en `MATH-F307`. Pour mergesort vu de manière algorithmique, voir *[[Mergesort]]*.

Mergesort est un algorithme de tri efficace qui utilise la technique de division et conquête pour trier un vecteur de taille $n = 2^p$.
### Principe de Mergesort
1. **Division**: L'algorithme divise le vecteur $v$ de taille $n$ en deux moitiés:
   - La moitié gauche: $v[1, \dots, n/2]$
   - La moitié droite: $v[n/2 + 1, \dots, n]$
2. **Tri récursif**: Mergesort trie récursivement chaque moitié.
3. **Fusion**: Les deux moitiés triées sont ensuite fusionnées pour obtenir un vecteur trié.

![[bedab3aded09203f69d6928def38ef1c.png]]

> [!info]+ Définition
> Soit $T(n)$ le nombre de comparaisons effectuées par mergesort pour trier un vecteur de taille $n$ dans le pire des cas.

> [!example]+ Exemples
> - **$T(2) = 2 \cdot T(1) + 2 - 1 = 1$**
> - **$T(4) = 2 \cdot T(2) + 3 = 5$**
> - **$T(8) = 2 \cdot T(4) + 7 = 17$**
### Observation cruciale
Pour résoudre le problème, on observe la relation de récurrence suivante:

$$\begin{cases}
T(1) = 0 \\
T(n)  = 2 \cdot T \left( \frac{n}{2} \right) + (n-1) \quad \forall n = 2^p \geq 2
\end{cases}$$

> [!abstract]- Théorème 7.1.1
> Pour $n = 2^p$, le nombre de comparaisons effectuées par mergesort est donné par:
> $$T(n) = n \log_2 (n) - n + 1$$
>
> ![[1f960a84bb8df91965ae907a70bd53c2.png]]
