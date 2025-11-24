---
title: Équations différentielles du 2nd ordre a coefficients constants
authors: Alessandro Dorigo
tags:
  - Maths
---


> [!info]+ Definition
> Une **équation différentielle du second ordre à coefficients constants** s’écrit sous la forme:
>
> $$ay'' + by' + cy = f(x)$$
>
> où:
> - a,b,ca, b, c sont des constantes avec a≠0a \neq 0,
> - f(x)f(x) est une fonction donnée,
> - y(x)y(x) est la fonction inconnue.

---

1. Resolution eq. caracteristique:
$$ar^2 + br + c = 0, \quad r = y' \ ; \  r^2 = y'' \ ; \  \dots$$
1.1) Cas / formes:
$$\Delta = b^2 - 4ac, \quad \lambda = \frac{-b \pm \sqrt{\Delta}}{2a}$$
1) Si $\Delta > 0$: (donc 2 racines reelles)
$$y_H = C_1 \cdot e^{\lambda_1 x} + C_2 \cdot e^{\lambda_2 x}$$
2) Si $\Delta = 0$: (qu'une seule racine)
$$y_H = (C_1 + C_2 \cdot x) \cdot e^{\lambda x}$$
3) Si $\Delta < 0$: (racines complexes)
$$y_H = [C_1 \cdot \cos(\omega x) + C_2 \cdot \sin(\omega x)] \cdot e^{\rho x}$$
$$\omega = \frac{1}{2a} \sqrt{4ac - b^2}$$
$$\rho = \frac{-b}{2a}$$

Donc:
$$\rightarrow y_H = C_1 \cdot g_1(x) + C_2 \cdot g_2(x)$$

2. Solution particuliere:
2.1) Variation des constantes:
$$y_H = u \cdot g_1 + v \cdot g_2$$
$$\begin{cases} u' \cdot g_1(x) + v' \cdot g_2(x) = 0 \\ u' \cdot g_1'(x) + v' \cdot g_2'(x) = \frac{f(x)}{a}\end{cases} \rightarrow \int u' = \dots \quad ; \quad \int v' = \dots \rightarrow u,v = \dots $$

2.2) Divination avancee: (on regarde la forme de $f(x)$)
1) Polynomiale: ($f$ est polynome de degre $n$)
$$y_P = \text{polynome de degre} \begin{cases} n \quad \text{si } c \neq 0 \\ n+1 \quad \text{si } c=0, b\neq0 \\ n+2 \quad \text{si} c=0, b=0, a\neq 0\end{cases}$$
2) Exponentielles: ($f(x) = Ae^{kx}$)
$$\begin{aligned}
y_P
&= \beta \cdot e^{kx} \quad \text{si } k \text{ n'est pas racine} \\
&= \beta x \cdot e^{kx} \quad \text{si } k \text{ est racine simple} \\
&= \beta x^2 \cdot e^{kx} \quad \text{si } k \text{ est racine double}
\end{aligned}$$
3) Trigo-exp: ($f(x) = [A \cdot \cos(kx) + B \cdot \sin(kx)] \cdot e^{lx}$)
$$\begin{aligned}
y_P
&= [\alpha \cdot \cos(kx) + \beta \cdot \sin(kx)] \cdot e^{lx} \quad \text{si } k \neq \omega; \quad l \neq \rho\\
&= x \cdot [\alpha \cdot \cos(kx) + \beta \cdot \sin(kx)] \cdot e^{lx} \quad \text{si } k = \omega; \quad l = \rho
\end{aligned}$$

Puis on remplace dans $y(x)$!

3. Solution generale:
$$y(x) = y_H(x) + y_P(x)$$
4. Conditions generales:
On remplace $y'(x), y(x), x$ puis on fait $y''(x)$ pour trouver $C_1$ et $C_2$.

---
## 1. Résolution de l'Équation Homogène

L'**équation homogène associée** est :

ay′′+by′+cy=0a y'' + b y' + c y = 0

#### Équation Caractéristique

On résout l'équation caractéristique associée :

ar2+br+c=0a r^2 + b r + c = 0

où :

- rr représente y′y',
- r2r^2 représente y′′y''.

---

### Cas en Fonction du Discriminant

Soit le discriminant :

Δ=b2−4ac,λ=−b±Δ2a\Delta = b^2 - 4ac, \quad \lambda = \frac{-b \pm \sqrt{\Delta}}{2a}

1. **Si Δ>0\Delta > 0 (Deux racines réelles distinctes)** :

    yH=C1eλ1x+C2eλ2xy_H = C_1 e^{\lambda_1 x} + C_2 e^{\lambda_2 x}
2. **Si Δ=0\Delta = 0 (Racine réelle double)** :

    yH=(C1+C2x)eλxy_H = (C_1 + C_2 x) e^{\lambda x}
3. **Si Δ<0\Delta < 0 (Racines complexes)** :

    yH=[C1cos⁡(ωx)+C2sin⁡(ωx)]eρxy_H = \left[ C_1 \cos(\omega x) + C_2 \sin(\omega x) \right] e^{\rho x}

    où :

    - ω=12a4ac−b2\omega = \frac{1}{2a} \sqrt{4ac - b^2},
    - ρ=−b2a\rho = \frac{-b}{2a}.

---

### Forme Générale de la Solution Homogène

yH=C1g1(x)+C2g2(x)y_H = C_1 g_1(x) + C_2 g_2(x)

où g1(x)g_1(x) et g2(x)g_2(x) dépendent du cas considéré.

---

## 2. Solution Particulière

### 2.1. Méthode de Variation des Constantes

On cherche une solution particulière sous la forme :

yP=u(x)g1(x)+v(x)g2(x)y_P = u(x) g_1(x) + v(x) g_2(x)

On impose les conditions :

{u′(x)g1(x)+v′(x)g2(x)=0u′(x)g1′(x)+v′(x)g2′(x)=f(x)a\begin{cases} u'(x) g_1(x) + v'(x) g_2(x) = 0 \\ u'(x) g_1'(x) + v'(x) g_2'(x) = \frac{f(x)}{a} \end{cases}

On résout pour u′(x)u'(x) et v′(x)v'(x), puis on intègre pour obtenir u(x)u(x) et v(x)v(x).

---

### 2.2. Méthode de la "Divination Avancée"

La forme de la solution particulière dépend de la forme de f(x)f(x) :

1. **f(x)f(x) Polynomiale** :
    Si f(x)f(x) est un polynôme de degré nn :

    yP={polynoˆme de degreˊ nsi c≠0polynoˆme de degreˊ n+1si c=0,b≠0polynoˆme de degreˊ n+2si c=0,b=0,a≠0y_P = \begin{cases} \text{polynôme de degré } n \quad \text{si } c \neq 0 \\ \text{polynôme de degré } n + 1 \quad \text{si } c = 0, b \neq 0 \\ \text{polynôme de degré } n + 2 \quad \text{si } c = 0, b = 0, a \neq 0 \end{cases}
2. **f(x)f(x) Exponentielle** :
    Si f(x)=Aekxf(x) = A e^{kx} :

    yP={βekxsi k n’est pas racineβxekxsi k est racine simpleβx2ekxsi k est racine doubley_P = \begin{cases} \beta e^{kx} \quad \text{si } k \text{ n'est pas racine} \\ \beta x e^{kx} \quad \text{si } k \text{ est racine simple} \\ \beta x^2 e^{kx} \quad \text{si } k \text{ est racine double} \end{cases}
3. **f(x)f(x) Trigonométrique-Exponentielle** :
    Si f(x)=[Acos⁡(kx)+Bsin⁡(kx)]elxf(x) = \left[ A \cos(kx) + B \sin(kx) \right] e^{lx} :

    yP={[αcos⁡(kx)+βsin⁡(kx)]elxsi k≠ω, l≠ρx[αcos⁡(kx)+βsin⁡(kx)]elxsi k=ω, l=ρy_P = \begin{cases} \left[ \alpha \cos(kx) + \beta \sin(kx) \right] e^{lx} \quad \text{si } k \neq \omega, \ l \neq \rho \\ x \left[ \alpha \cos(kx) + \beta \sin(kx) \right] e^{lx} \quad \text{si } k = \omega, \ l = \rho \end{cases}

---

## 3. Solution Générale

La **solution générale** de l'équation différentielle est la somme de la solution homogène et de la solution particulière :

y(x)=yH(x)+yP(x)y(x) = y_H(x) + y_P(x)

---

## 4. Application des Conditions Initiales

Pour déterminer les constantes C1C_1 et C2C_2, on utilise les conditions initiales données :

1. **Substituer** y(x)y(x) et y′(x)y'(x) dans les conditions initiales.
2. **Résoudre le système d'équations** pour C1C_1 et C2C_2.

---

### Exemple Résumé

1. **Équation** :

    y′′−3y′+2y=e2xy'' - 3y' + 2y = e^{2x}
2. **Équation caractéristique** :

    r2−3r+2=0  ⟹  r1=2, r2=1r^2 - 3r + 2 = 0 \implies r_1 = 2, \ r_2 = 1
3. **Solution homogène** :

    yH=C1e2x+C2exy_H = C_1 e^{2x} + C_2 e^{x}
4. **Solution particulière** :
    Comme f(x)=e2xf(x) = e^{2x} et 22 est une racine simple,

    yP=βxe2xy_P = \beta x e^{2x}
5. **Solution générale** :

    y(x)=C1e2x+C2ex+βxe2xy(x) = C_1 e^{2x} + C_2 e^{x} + \beta x e^{2x}

Cette présentation couvre toutes les étapes de résolution des équations différentielles du second ordre à coefficients constants avec des explications détaillées.
