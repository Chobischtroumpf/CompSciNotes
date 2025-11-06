---
title: Preuve par récurrence forte
authors: Alessandro Dorigo
tags:
  - MathDis
  - Maths
---


> [!info]+ Définition
> La **récurrence forte** est une méthode de [[Preuve par induction#^33574a|démonstration par induction]] où, à l'étape inductive, on suppose que la proposition est vraie pour **toutes les valeurs précédentes**, et pas seulement pour la valeur précédente immédiate.
>
> Elle a 4 étapes:
> 1. **Base de la récurrence**:
> 	- Prouver que $P(n)$ est vraie pour une ou plusieurs valeurs initiales de $n$.
> 2. **Hypothèse de récurrence forte**:
> 	- Supposons que la proposition $P(k)$ est vraie pour **toutes les valeurs** $k$ telles que $k \leq n$.
> 3. **Étape inductive**:
> 	- Prouver que, sous l'hypothèse que $P(k)$ est vraie pour toutes les valeurs $k \leq n$, la proposition $P(n+1)$ est également vraie. Utilisez l'ensemble des cas $P(0), P(1), \ldots, P(n)$ pour démontrer $P(n+1)$.
> 4. **Conclusion**:
> 	- Par le principe de récurrence forte, la proposition $P(n)$ est alors vraie pour tous les entiers $n \geq$ (valeur de départ).

^726214

> [!example]+ Exemple: Division d’un entier $n \geq 2$ en nombres premiers
> **Problème**: Montrons par récurrence forte que tout entier $n \geq 2$ peut être écrit comme un produit de nombres premiers.
>
> **Étape 1: Base de la récurrence**
> Pour $n = 2$, $2$ est un nombre premier, donc $n$ est écrit comme un produit de nombres premiers (lui-même). La propriété est vraie pour $n = 2$.
>
> **Étape 2: Hypothèse de récurrence**
> Supposons que tout entier $k$ tel que $2 \leq k \leq n$ peut être écrit comme un produit de nombres premiers.
>
> **Étape 3: Étape inductive**
> Montrons que $n+1$ peut être écrit comme un produit de nombres premiers.
> - Si $n+1$ est un nombre premier, alors $n+1$ est lui-même un produit de nombres premiers.
> - Sinon, $n+1$ est composé ($n+1 = a \times b$, avec $2 \leq a, b \leq n$).
>   - Par l’hypothèse de récurrence forte, $a$ et $b$ peuvent être écrits comme des produits de nombres premiers. Donc $n+1 = a \times b$ est aussi un produit de nombres premiers.
>
> **Étape 4: Conclusion**
> Par récurrence forte, tout entier $n \geq 2$ peut être écrit comme un produit de nombres premiers.
### Différence avec la récurrence simple
- **Récurrence simple**: On utilise uniquement $P(n)$ pour prouver $P(n+1)$.
- **Récurrence forte**: On utilise $P(0), P(1), \dots, P(n)$ pour prouver $P(n+1)$.

La récurrence forte est particulièrement utile lorsque le problème nécessite de s’appuyer sur **toutes les valeurs précédentes**, pas seulement sur la dernière.
