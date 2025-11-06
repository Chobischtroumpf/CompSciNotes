---
title: Formules de Bayes
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Version discrète, traduction de la version classique
> $$p_{Y \vert X}(y \vert x) = \frac{p_Y(y) \cdot p_{X \vert Y}(x \vert y)}{\sum_u p_Y(u) \cdot p_{X \vert Y}(x \vert u)}$$

> [!info]+ Version continue
> $$f_{Y \vert X}(y \vert x) = \frac{f_Y(y) f_{X \vert Y}(x \vert y)}{\int_{-\infty}^\infty f_Y(u) f_{X \vert Y}(x \vert u) \ du}$$

> [!info]+ Versions mixtes
> $$f_{X \vert A}(x) = \frac{f_X(x) \mathbb{P}(A \vert X = x)}{\mathbb{P}(A)} = \frac{f_X(x) \mathbb{P}(A \vert X = x)}{\int_{-\infty}^\infty f_X(u) \mathbb{P}(A \vert X = u) \ du}$$
> $$\mathbb{P}(B_k \vert X = x) = \frac{\mathbb{P}(B_k) f_{X \vert B_k}(x)}{\sum_{i=1}^n \mathbb{P}(B_i) f_{X \vert B_i}(x)}$$
