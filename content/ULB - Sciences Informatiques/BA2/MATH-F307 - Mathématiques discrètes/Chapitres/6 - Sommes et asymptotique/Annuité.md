---
title: Annuité
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


*Préféreriez-vous recevoir un million d’euros aujourd'hui ou 50.000€ par an pour le reste de votre vie ? D'un côté, il est tentant d'avoir la somme tout de suite. D'un autre côté, la somme totale de 50.000 € par an pourrait être bien supérieure si vous vivez suffisamment longtemps.*

Formellement, cette question concerne la **valeur d’une annuité**.

> [!info]+ Définition
> Une **annuité** est un instrument financier qui verse un montant fixe au début de chaque année pendant un nombre d’années spécifié. En particulier, une annuité de $n$ ans avec un paiement de montant $m$ verse $m$ euros au début de chaque année pour $n$ années.
>
> *Parfois, $n$ est fini, mais ce n'est pas toujours le cas.*
>
> **Note**: Cette définition est une approximation intuitive et n'est pas formelle.

> [!example]+ Exemples
> - Prêt immobilier
> - “Win for life” (ou “Megabucks”): 40 000 €/an à vie
> - Épargne-pension
### Valeur actuelle d'une annuité
**Question**: Quelle est la valeur actuelle d’une annuité?

Prenons un exemple: un “win for life” de 40.000 € par an pendant 50 ans. Sa valeur actuelle dépasse-t-elle 2.000.000 €? Ou bien 1.000.000 €? Et qu’en est-il de 500.000 €?

> [!abstract]- Hypothèse d'actualisation
>
> L’actualisation nous permet de calculer la valeur actuelle de chaque paiement futur en tenant compte d'un taux d'intérêt $p$.
>
> - $1 \unicode{0x20ac}$ aujourd’hui équivaut à $(1 + p)^2 \unicode{0x20ac}$ dans 2 ans.
> - $1 \unicode{0x20ac}$ aujourd’hui équivaut à $(1 + p)^3 \unicode{0x20ac}$ dans 3 ans.
> - $\frac{1}{1 + p} \unicode{0x20ac}$ aujourd’hui équivaut à $1 \unicode{0x20ac}$ dans 1 an.
> - $\frac{1}{(1 + p)^2} \unicode{0x20ac}$ aujourd’hui équivaut à $1 \unicode{0x20ac}$ dans 2 ans.

Pour une série d’annuités de montant $m \unicode{0x20ac}$, nous pouvons calculer la valeur actuelle de chaque paiement en l'actualisant selon le nombre d'années correspondant. Par exemple:

$$
\begin{array}{|c|c|c|}
\hline
\text{Annuités} & \text{Valeur actuelle} & \text{Temps} \\
\hline
m \unicode{0x20ac} & m \unicode{0x20ac} & \text{aujourd’hui} \\
\hline
m \unicode{0x20ac} & \frac{m}{1 + p} \unicode{0x20ac} & \text{dans 1 an} \\
\hline
m \unicode{0x20ac} & \frac{m}{(1 + p)^2} \unicode{0x20ac} & \text{dans 2 ans} \\
\hline
\vdots & \vdots & \vdots \\
\hline
m \unicode{0x20ac} & \frac{m}{(1 + p)^{n - 1}} \unicode{0x20ac} & \text{dans } n - 1 \text{ ans} \\
\hline
\end{array}
$$

En ajoutant ces valeurs, nous obtenons la **valeur actuelle totale** de l'annuité $V$, exprimée comme une [[Série géométrique|somme géométrique]]:

$$
V = m + \frac{m}{1 + p} + \frac{m}{(1 + p)^2} + \cdots + \frac{m}{(1 + p)^{n - 1}} = \sum_{k=0}^{n-1} \frac{m}{(1 + p)^k}
$$

ou encore:

$$
V = m \cdot \sum_{k=0}^{n-1} x^k \quad \left(\text{où } x = \frac{1}{1 + p}\right)
$$

### Justification par la méthode de perturbation
L'objectif des substitutions précédentes est de transformer la somme en une forme simple de **[[Série géométrique|série géométrique]]**. Nous démontrerons la formule à l'aide de la **[[Méthode par perturbation|méthode par perturbation]]**.

Grace au théorème 6.2.1: ![[Méthode par perturbation#^ad038b]]
$$
\begin{align*}
V &= \sum_{k=0}^{n-1} \frac{m}{(1 + p)^k} = m \cdot \sum_{k=0}^{n-1} x^k \quad \left( \text{où } x = \frac{1}{1 + p} \right) \\
&= m \cdot \frac{1 - x^n}{1 - x} = m \cdot \frac{(1 + p)^n - 1}{p(1 + p)^{n-1}} < n \cdot m
\end{align*}
$$

> [!example]+ Exemple
> $$
> m = 40.000 \, \unicode{0x20ac}, \quad n = 50 \text{ ans}, \quad p = 0,06 \Rightarrow V \approx 668.303 \, \unicode{0x20ac}
> $$

> [!abstract]- Lemme 6.1.1
> Si $n = \infty$, alors $V = m \cdot \frac{1 + p}{p}$
>
> $$V = m \cdot \frac{1 - \left(\frac{1}{1+p}\right)^n}{1 - \frac{1}{1+p}} = m \cdot \frac{1 + p - \left(\frac{1}{1+p}\right)^{n-1}}{p} \Rightarrow^{n \to \infty} m \cdot \frac{1 + p}{p}$$
>
>  - $m = 40.000 \, \unicode{0x20ac}, \quad p = 0,06 \Rightarrow V \approx 706.667 \, \unicode{0x20ac}$

Il est aussi possible de résoudre ce problème a l'aide de la [[Méthode par dérivation]], ou par l'[[Approximation d’une somme par une intégrale]]
