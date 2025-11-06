---
title: Formule de Binet
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
---


> [!abstract]- Théorème "Formule de Binet"
> Pour tout $n \in \mathbb{N}$, le $n$-ème nombre de Fibonacci est donné par :
> $$
> F_n = \frac{1}{\sqrt{5}} \cdot \left(\frac{1+\sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}} \cdot \left(\frac{1-\sqrt{5}}{2}\right)^n = \frac{\varphi^n - \bar{\varphi}^n}{\sqrt{5}}
> $$
>
> De plus, pour $n \geq 1$, $F_n$ est l'entier le plus proche de $\varphi^n/\sqrt{5}$ car $\bar{\varphi}^n = \left(\frac{1-\sqrt{5}}{2}\right)^n \xrightarrow{n \to \infty} 0$ exponentiellement.

> [!example]+ Exemple (Fibonacci)
> Pour trouver une valeur de $n$ tel que  $F_n = f(n) \geq M$, il suffit de faire :
> $$\frac{\varphi^n}{\sqrt{5}} - \frac{\bar{\varphi}^n}{\sqrt{5}} \geq M \quad \text{où} \quad \varepsilon(n) = \frac{\bar{\varphi}^n}{\sqrt{5}} \xrightarrow{n \to \infty} 0$$
> $$\Leftrightarrow \frac{\varphi^n}{\sqrt{5}} \geq M + \varepsilon(n)$$
> $$\Leftrightarrow \varphi^n \geq \sqrt{5} \cdot (M + \varepsilon(n))$$
> $$\Leftrightarrow n \geq \log_\varphi(\sqrt{5} \cdot (M + \varepsilon(n))) = \Theta(\log(M))$$
