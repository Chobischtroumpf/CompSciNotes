---
title: Bijectivité
authors: Alessandro Dorigo
tags:
  - MathDis
  - Comptage
---


> [!info]+ Définition
> Une fonction $f : X \to Y$ est dite **bijective** **si et seulement si** $f$ est **[[Surjectivité#^a4af3a|surjective]]** et **[[Injectivité#^4e3053|injective]]**. C’est à dire, tout élément de $Y$ est l’image d’exactement un élément de $X$.
> $$\forall y \in Y, \exists!x \in X \text{ tel que } y = f(x)$$

> [!info]+ $k$-bijection
> Une fonction $f : X \to Y$ est dite **$k$-bijective** (ou **"k-to-1"**) si tout élément de $Y$ est l’image d'**exactement $k$** éléments de $X$.
>
> **Règle de division**:
> $$\vert X \vert = k \cdot \vert Y \vert \quad \Leftrightarrow \quad \vert Y \vert = \frac{\vert X \vert}{k}$$

> [!example]+ Exemple
> De combien de façons peut-on placer deux tours identiques sur un échiquier de telle sorte qu’aucune ligne ou colonne contienne les deux tours?
>
> ![[Pasted image 20241112151208.png]]
>
> **Ensemble $X$**: L'ensemble des quadruplets $(l_1, c_1, l_2, c_2)$ où $1 \leq l_1, l_2 \leq 8$, $1 \leq c_1, c_2 \leq 8$, $l_1 \neq l_2$, et $c_1 \neq c_2$.
>
> **Ensemble $Y$**: Les placements "neutres" des deux tours (c'est-à-dire les configurations distinctes sous rotation ou symétrie).
>
> La fonction $f$ est **2-bijective**, ce qui implique que:
> $$\vert Y \vert = \frac{\vert X \vert}{2} = \frac{8 \cdot 8 \cdot 8 \cdot 7}{2} = 224$$
