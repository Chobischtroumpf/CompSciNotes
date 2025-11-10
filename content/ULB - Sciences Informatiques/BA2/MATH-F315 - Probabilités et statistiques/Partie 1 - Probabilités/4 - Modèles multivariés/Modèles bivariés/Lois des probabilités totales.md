---
title: Lois des probabilités totales
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Version continue
> $$f_X(x) = \int_{-\infty}^{\infty} f_{X \vert Y}(x \vert v) f_Y(v) \ dv$$

> [!info]+ Version discrète
> $$p_X(x) = \sum_v p_{X \vert Y}(x \vert v) p_Y(v)$$

> [!info]+ Version cumulative
> $$F_X(x) = \int_{-\infty}^{\infty} F_{X \vert Y}(x \vert v) f_Y(v) \ dv$$

> [!info]+ Versions mixtes
> $$f_X(x) = \sum_{i=1}^n f_{X \vert B_i}(x) \mathbb{P}(B_i)$$
> $$\mathbb{P}(A) = \int_{-\infty}^{\infty} \mathbb{P}(A \vert X = u) f_X(u) \ du$$
