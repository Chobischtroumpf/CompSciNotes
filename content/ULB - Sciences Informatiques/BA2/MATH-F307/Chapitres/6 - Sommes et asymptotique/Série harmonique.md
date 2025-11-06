---
title: Série harmonique
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


> [!info]+ Définition
> La **série harmonique** est la somme des inverses des entiers naturels.
> $$\sum_{k=1}^{\infty} \frac{1}{k}$$

> [!info]+ Définition
> Le **nombre harmonique** $H_n$ est la somme partielle de la série harmonique jusqu’à un certain entier $n$.
>
> En d'autres termes, $n$ est l'indice jusqu’au quel on somme les termes, et $H_n$​ est le **résultat** de cette somme, qui est considéré comme le "nombre harmonique".
> $$H_n := \sum_{k=1}^n \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

> [!example]+ Exemples
> $$H_1 = 1$$
> $$H_2 = 1 + \frac{1}{2} = \frac{3}{2}$$
> $$H_3 = \frac{3}{2} + \frac{1}{3} = \frac{11}{6}$$
> $$H_4 = \frac{11}{6} + \frac{1}{4} = \frac{25}{12} > 2$$

Approximation par une intégrale: avec $f(x) = \frac{1}{x}$ décroissante.
$$\frac{1}{n} + \int_1^n \frac{1}{x} dx \leq \sum_{k=1}^n \frac{1}{k} \leq 1 + \int_1^n \frac{1}{x} dx$$
$$\frac{1}{n} + \log(n) \leq H_n \leq 1 + \log(n)$$
$$\Rightarrow H_n = \log(n) + \delta(n) \quad \text{où} \quad \frac{1}{n} \leq \delta(n) \leq 1$$
$$\Rightarrow H_n \sim \log(n) \quad \text{[égalité asymptotique]}$$

> [!abstract]- Théorème 6.5.1
> $$H_n = \log(n) + \gamma + \frac{1}{2n} + \frac{1}{12n^2} + \frac{\varepsilon(n)}{120n^4}$$
>
> où $0 < \varepsilon(n) < 1$ et $\gamma = \text{constante d'Euler} = 0{,}577215664\ldots$

> [!abstract]- Théorème 6.5.2
> La suite $(H_n - \log(n))_{n \geq 1}$ converge vers un réel positif.
>
> Ce reel est $\gamma = 0{,}5772156649\ldots \Rightarrow H_n = \log(n) + \gamma + o(1)$
>
> ![[Pasted image 20241212134724.png]]
> ![[Pasted image 20241212134737.png]]

> [!tip]+ Remarque
> On peut montrer qu'en fait
>
> $$H_n = \log(n) + \gamma + \frac{1}{2n} - \frac{1}{12n^2} + \frac{1}{240n^4} - \varepsilon_n \quad \text{avec} \quad 0 < \varepsilon_n < \frac{1}{252n^6}$$
