---
title: Top-down Mergesort
authors: Alessandro Dorigo
tags:
  - Algo
---


## Implémentation
```java
private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi)
{
	if (hi <= lo) return;
	int mid = lo + (hi - lo) / 2;
	sort(a, aux, lo, mid);
	sort(a, aux, mid + 1, hi);
	merge(a, aux, lo, mid, hi);
}

private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi)
{
	for (int k = lo; k <= hi; k++)
		aux[k] = a[k];

	int i = lo, j = mid + 1;
	for (int k = lo; k <= hi; k++)
		{
			if (i > mid) a[k] = aux[j++];
			else if (j > hi) a[k] = aux[i++];
			else if (less(aux[j], aux[i])) a[k] = aux[j++];
			else a[k] = aux[i++];
		}
}
```

> [!abstract]- Théorème
> Le tri fusion utilise au plus $\thicksim n \log_2 n$ comparaisons pour trier un tableau de taille $n$.
>
> On sait que [[Analyse de Mergesort#Relation de récurrence]].
>
> **Démonstration:**
> Nous allons procéder par induction.
>
> 1. **Hypothèse d'induction**: Supposons que pour une certaine valeur de $n$, nous ayons:
>    $$D(n) \leq n \log_2(n)$$
>
> 2. **Étape d'induction**: Pour $2n$, nous avons:
>      $$
>     \begin{align*}
>     D(2n) &\leq 2D(n) + 2n \\
>     &\leq 2(n \log_2(n)) + 2n \\
>     &= 2n (\log_2(n) + 1) \\
>     &= 2n \log_2(2n)
>     \end{align*}
>     $$
> 3. **Cas de base**: Pour $n = 1$, nous avons $D(1) = 0$, ce qui vérifie l'inégalité.
