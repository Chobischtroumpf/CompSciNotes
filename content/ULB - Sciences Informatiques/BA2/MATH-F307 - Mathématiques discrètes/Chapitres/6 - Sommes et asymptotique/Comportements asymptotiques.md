---
title: Comportements asymptotiques
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


Formellement appris en `MATH-F307`. Pour les comportements asymptotiques vus de manière algorithmique, voir *link*.

> [!info]+ Équivalence asymptotique
> Soient $f, g : \mathbb{N} \to \mathbb{R}$ deux fonctions s'annulant en au plus un nombre fini de valeurs.
>
> On écrit $f \sim g$ ou $f(n) \sim g(n)$ si et seulement si
> $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = 1$$
> et on dit que $f$ et $g$ sont **asymptotiquement égales**.

^746245
## Notations de Landau
### Grand $\mathcal{O}$
![[Grand O]]

> [!note]
> La notation $\mathcal{O}(\cdot)$ est très utilisée en analyse d'algorithmes:
> - Temps pour multiplier deux matrices $n \times n = \mathcal{O}(n^3)$
> - Temps pour trier $n$ objets par comparaison $= \mathcal{O}(n \log(n))$
### Petit $\mathcal{o}$
![[Petit o#^dfe846]]
### Grand $\Omega$
![[Grand Omega#^52d6fc]]
### Petit $\omega$
![[Petit omega#^d5f9cd]]
### Grand $\Theta$
![[Grand Theta]]

> [!tip]+ Intuitivement
> - $f \in \mathcal{O}(g)$ signifie " $f(n) \leq g(n)$ à une constante près"
> - $f \in \Omega(g)$ signifie " $f(n) \geq g(n)$ à une constante près"
> - $f \in \Theta(g)$ signifie " $f(n) = g(n)$ à une constante près"
> - $f \in \mathcal{o}(g)$ signifie " $f(n) < g(n)$ à une constante près"
> - $f \in \omega(g)$ signifie " $f(n) > g(n)$ à une constante près"

> [!abstract]- Théorème 6.7.1
> Soit $f(n) = n$ et $g(n) = n^2$. Alors $f(n) \in \mathcal{O}(g(n))$.
>
> **Démonstration**:
> On a $n \leq 1 \cdot n^2$ pour tout $n \in \mathbb{N}$. Donc, $C = 1$ suffit. $\quad \square$

> [!abstract]- Théorème 6.7.2
> Soit $f(n) = n$ et $g(n) = n^2$. Alors $g(n) \notin \mathcal{O}(f(n))$.
>
> **Démonstration**:
> $$\lim_{n \to \infty} \frac{n^2}{n} = \lim_{n \to \infty} n = +\infty$$
> Ainsi, il n'existe pas de constante $C$ telle que $n^2 \leq C \cdot n$ pour $n$ grand. $\quad \square$

^16b996

> [!example]+ Exemples
> **Ex**: Est-ce que $n^2 \in \mathcal{O}(10^6n)$? **Non** (même raisonnement que pour le [[Comportements asymptotiques#^16b996|théorème 6.7.2]]).
> **Ex**: Est-ce que $10^6n^2 \in \mathcal{O}(n^2)$? **Oui** (on peut prendre $C = 10^6$).
> **Ex**: Est-ce que $7n^2 + 3n - 42 \in \mathcal{O}(n^2)$? **Oui**
> - Car $7n^2 + 3n - 42 \leq 10n^2$ pour $n$ grand.
>
> **Ex**: A-t-on $n^{10} \in \mathcal{O}(e^n)$? **Oui**
> Comme
> $$\lim_{n \to \infty} \frac{n^{10}}{e^n} = 0,$$
> $$\forall \varepsilon > 0, \exists M > 0 \text{ tel que pour tout } n \geq M \text{ on a } |n^{10}| < \varepsilon |e^n|$$
> **Ex**: A-t-on $4^n \in \mathcal{O}(2^n)$? **Non**
> Car
> $$\lim_{n \to \infty} \frac{4^n}{2^n} = \lim_{n \to \infty} \frac{(2^n)^2}{2^n} = \lim_{n \to \infty} 2^n = \infty$$
> **Ex**: A-t-on $10 \in \mathcal{O}(1)$? **Oui**
> **Ex**: A-t-on $\sin(n) \in \mathcal{O}(1)$? **Oui** (en prenant $C = 1$)
