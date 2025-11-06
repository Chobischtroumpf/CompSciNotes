---
title: Binary search (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
  - Algo
---


![[Pasted image 20241105094830.png]]

> [!info]+ Définition
> Soit $T(n)$ le nombre de comparaisons effectuées par une recherche binaire dans un vecteur de taille $n$, pour détecter la présence (ou non) de $x$ (au pire cas).

> [!example]+ Exemple
> ![[Pasted image 20241111123851.png]]
### Observation cruciale
Pour résoudre le problème, on observe la relation de récurrence suivante:

$$\begin{cases}
T(1) = 1 \\
T(n)  = T \left( \lfloor \frac{n}{2} \rfloor \right) + 1 \quad \forall n \geq 2
\end{cases}$$

> [!abstract]- Théorème 7.3.1
> Pour tout $n \geq 2$, le nombre de comparaisons effectuées par une recherche binaire dans un vecteur de taille $n$, pour détecter la présence (ou non) de $x$ (au pire cas) est:
> $$T(n) = 1 \cdot T \left( \frac{x}{2} + \varepsilon(x) \right) + 1$$
> avec $\varepsilon = \lfloor \frac{x}{2} \rfloor - \frac{x}{2}$.
>
> **Démonstration ([[Akra-Bazzi#^e2e8a1|Akra-Bazzi]]):**
> - Paramètres: $k = 1, g(x) = 1, p = 0$
>
> $$T(x) \in \Theta \left( x^0 + x^0 \int_{1}^{x} \frac{1}{u} du \right) = \Theta(\log(x))$$

> [!tip]+ Remarque
> $T(n) =$ nombre de bits dans l’écriture de $n$ en base 2.
