---
title: Fonction convexe
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Définition
> Une fonction $f : \mathbb{R}^n \rightarrow \mathbb{R}$ est convexe si le domaine de la fonction $f$, dénoté $\text{dom}(f)$, est un ensemble convexe et pour tout $(x,y) \in \text{dom}(f) \times \text{dom}(f)$ l’inégalité suivante est vérifiée pour tout $\alpha \in [0,1]$:
>
> $$f(\underbrace{\alpha x + (1-\alpha)y}_{\text{convex combination}}) \leq \underbrace{\alpha f(x) + (1-\alpha)f(y)}_{\text{chord}}$$

> [!note]
> Une fonction $f : \mathbb{R}^n \rightarrow \mathbb{R}$ est convexe ssi sa réflexive $-f$ est concave et concave si $-f$ est convexe.

> [!example]+ Exemple
> ![[eb1ad75068c3c329ec02f60c198bfc9d.png]]

> [!abstract]- Théorème 1.0.1
> Toute fonction linéaire $f : \mathbb{R} \rightarrow \mathbb{R} : x \rightarrow ax$ est convexe.
>
> **Preuve**:
> $$
> \begin{align}
> f(\alpha x_1 + (1-\alpha)x_2) &= a((1-\alpha)x_1 + \alpha x_2) \\
> &= (1-\alpha) ax_1 + \alpha ax_2 \\
> &= (1-\alpha)f(x_1) + \alpha f(x_2)
> \end{align}
> $$

> [!abstract]- Théorème 1.0.2
> Toute fonction affine $f : \mathbb{R} \rightarrow \mathbb{R} : x \rightarrow ax + b$ est convexe.
>
> **Preuve**:
> $$
> \begin{align}
> f(\alpha x_1 + (1-\alpha)x_2) &= a(\alpha x_1 + (1-\alpha)x_2) + b \\
> &= a(\alpha x_1 + (1-\alpha)x_2) + (\alpha + (1-\alpha))b \\
> &= \alpha(ax_1 + b) + (1-\alpha)(ax_2 + b) \\
> &= \alpha f(x_1) + (1-\alpha)f(x_2)
> \end{align}
> $$
