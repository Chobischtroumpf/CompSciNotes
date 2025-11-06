---
title: Module
authors: Alessandro Dorigo
tags:
  - MathDis
  - TheorieDesNombres
---


> [!info]+ Définition
> Soient $x, y \in \mathbb{Z}$ (les entiers relatifs) et $n \in \mathbb{N}$ (les entiers naturels non nuls).
>
> On dit que **$x$ est congru à $y$ modulo $n$**, noté:
> $$x \equiv y \pmod{n}$$
> si $n$ divise $x - y$, c'est-à-dire si:
> $$x - y \in n\mathbb{Z} \quad \text{ou encore} \quad n \mid (x - y)$$

> [!tip]+ Congruence
> La congruence modulo $n$ est une **relation d’équivalence** compatible avec les opérations arithmétiques:
> 1. **Réflexivité**: $x \equiv x \pmod{n}$.
> 2. **Symétrie**: Si $x \equiv y \pmod{n}$, alors $y \equiv x \pmod{n}$.
> 3. **Transitivité**: Si $x \equiv y \pmod{n}$ et $y \equiv z \pmod{n}$, alors $x \equiv z \pmod{n}$.

**Compatibilité avec les Opérations:**
Si $x \equiv y \pmod{n}$ et $u \equiv v \pmod{n}$, alors:
- $x + u \equiv y + v \pmod{n}$,
- $x - u \equiv y - v \pmod{n}$,
- $x \cdot u \equiv y \cdot v \pmod{n}$.

De plus, si $x \equiv y \pmod{n}$, alors pour tout $k \in \mathbb{N}$: $$x^k \equiv y^k \pmod{n}$$

**Compatibilité avec les Transformations:**
1. **Translation**: $a + k \equiv b + k \pmod{n}, \quad \forall k \in \mathbb{Z}$.
2. **Scaling**: $k \cdot a \equiv k \cdot b \pmod{n}, \quad \forall k \in \mathbb{Z}$.
3. **Polynomial**:
    Si $p(x)$ est un polynôme à coefficients entiers, alors: $$p(a) \equiv p(b) \pmod{n}$$

**Annulation des Termes Communs:**
1. Si $a + k \equiv b + k \pmod{n}$, alors: $$a \equiv b \pmod{n}$$
2. Si $k \cdot a \equiv k \cdot b \pmod{n}$ et que $k$ est co-premier avec $n$, alors: $$a \equiv b \pmod{n}$$
3. Si $k \cdot a \equiv k \cdot b \pmod{k \cdot n}$ avec $k \neq 0$, alors: $$a \equiv b \pmod{n}$$

**Modulo et Division:**
La dernière règle permet d’intégrer l’arithmétique modulaire à la division. Si $b$ divise $a$, alors:
$$\left( \frac{a}{b} \right) \mod n = \frac{a \mod (b \cdot n)}{b}$$

> [!info]+ Inverse Multiplicatif Modulo $n$
> Si $x \cdot y \equiv 1 \pmod{n}$, alors $y$ est appelé **l'inverse multiplicatif de $x$ modulo $n$**.
> - On le note $y \equiv x^{-1} \pmod{n}$.
>
> Un entier $x$ possède un inverse multiplicatif modulo $n$ **si et seulement si** [[PGCD#^86c2aa|pgcd]]$(x, n) = 1$.
>
> Dans l'autre direction:
> $$\exists y \in \mathbb{Z}: x \cdot y \equiv 1 \pmod{n}$$
> $$\exists y \in \mathbb{Z}, \exists k \in \mathbb{Z}: x \cdot y = 1 + k \cdot n$$
> $$\exists y \in \mathbb{Z}, \exists k \in \mathbb{Z}: x \cdot y - k \cdot n = 1$$
> $$\text{pgcd}(x, n) = 1$$

> [!tip]+ Co-primalité
> Deux entiers $a$ et $b$ sont dits premiers entre eux si [[PGCD#^86c2aa|pgcd]]$(a, b) = 1$.
> - Si $\text{pgcd}(a, b) = 1$ et $\text{pgcd}(a, c) = 1$, alors $\text{pgcd}(a, bc) = 1$.
> - Si $a \mid bc$ et $\text{pgcd}(a, b) = 1$, alors $a \mid c$.

> [!tip]+ Congruence vs Modulo
> 1. **Congruence**:
> $x \equiv y \pmod{n}$ signifie que $x$ et $y$ ont le même reste lorsqu’ils sont divisés par $n$.
> 2. **Modulo (opération)**:
> $x \mod n$ donne directement le reste de la division de $x$ par $n$, qui est unique dans $[0, n - 1]$.
