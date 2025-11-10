---
title: Solutions d'une equation de récurrence linéaire homogène
authors: Alessandro Dorigo
tags:
  - MathDis
---

> [!abstract]- Théorème 8.0.1
> L'ensemble $S$ des solutions d'une équation de récurrence linéaire homogène d'ordre $d$ est un espace vectoriel de dimension $d$.
> **Démonstration:**
> (1) $S$ est un sous-espace vectoriel de $\mathbb{C}^\mathbb{N}$ :
> - La suite nulle $(0,0,0,...) \in S$ car l'équation est homogène
> - Si $f_1(n)$ et $f_2(n)$ sont solutions, alors $f(n) = c_1 \cdot f_1(n) + c_2 \cdot f_2(n)$ est solution car :
> $$
> f(n) = \sum_{i=1}^d a_i \cdot (c_1 \cdot f_1(n-i) + c_2 \cdot f_2(n-i)) = \sum_{i=1}^d a_i \cdot f(n-i)
> $$
>
> (2) $\dim(S) = d$ via l'application linéaire:
> $$A: S \to \mathbb{C}^d, f \mapsto (f(0),f(1),...,f(d-1))$$
> - $A$ est linéaire : $A(c \cdot f + g) = c \cdot A(f) + A(g)$
> - $A$ est injective : $\ker(A) = \{0\}$
> - $A$ est surjective : Pour tout choix de conditions initiales, il existe une solution.
>
> Donc $A$ est un isomorphisme et $\dim(S) = d$.

> [!example]+ Exemple (Fibonacci)
> La solution générale de l'équation $$f(n) = f(n-1) + f(n-2) \quad \forall n \geq 2$$ est :
> $$
> f(n) = c_1 \cdot \left(\frac{1+\sqrt{5}}{2}\right)^n + c_2 \cdot \left(\frac{1-\sqrt{5}}{2}\right)^n
> $$
>
> Pour les conditions initiales $$f(0)=0, f(1)=1$$, on résout :
> $$
> \begin{cases}
> f(0)=0 \\
> f(1)=1
> \end{cases} \Leftrightarrow
> \begin{cases}
> c_1 + c_2 = 0 \\
> c_1\varphi + c_2\bar{\varphi} = 1
> \end{cases} \Leftrightarrow
> \begin{cases}
> c_2 = -c_1 \\
> c_1(\varphi - \bar{\varphi}) = 1
> \end{cases} \Leftrightarrow
> \begin{cases}
> c_1 = \frac{1}{\sqrt{5}} \\
> c_2 = -\frac{1}{\sqrt{5}}
> \end{cases}
> $$
