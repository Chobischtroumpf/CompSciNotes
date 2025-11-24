---
title: Probabilités
authors: Alessandro Dorigo
tags:
  - Proba
  - Maths
---

## Règles de Morgan

> [!abstract]- Formules
> $$
> \begin{align*}
> (A \cap B)^c &= A^c \cup B^c \\
> (A \cup B)' &= A^c \cap B^c \\
> (A \cap B \cap C)^c &= A^c \cup B^c \cup C^c \\
> (A \cup B \cup C)^c &= A^c \cap B^c \cap C^c
> \end{align*}
> $$
## Lois utiles

> [!abstract]- Propriétés
> ### Commutativité
> $$
> \begin{align*}
> A \cup B &= B \cup A \\
> A \cap B &= B \cap A
> \end{align*}
> $$
> ### Associativité
> $$
> \begin{align*}
> (A \cup B) \cup C &= A \cup (B \cup C) \\
> (A \cap B) \cap C &= A \cap (B \cap C)
> \end{align*}
> $$
> ### Distributivité
> $$
> \begin{align*}
> (A \cup B) \cap C &= (A \cap C) \cup (B \cap C) \\
> (A \cap B) \cup C &= (A \cup C) \cap (B \cup C)
> \end{align*}
> $$
## Propriétés des probabilités

> [!abstract]- Formules
> $$
> \begin{align*}
> P(E_1 \cup E_2) &= P(E_1) + P(E_2) - P(E_1 \cap E_2) \\
> P(A \backslash B) &= \frac{P(A \cap B)}{P(B)} \\
> P(E^c) &= 1 - P(E)
> \end{align*}
> $$

> [!example]+ Pour trois événements
> $$
> \begin{align*}
> P(E_1 \cup E_2 \cup E_3) &= P(E_1) + P(E_2) + P(E_3) - P(E_1 \cap E_2) - \\
> &\ \ \ \ P(E_2 \cap E_3) - P(E_1 \cap E_3) + P(E_1 \cap E_2 \cap E_3)
> \end{align*}
> $$
## Probabilités conditionnelles

> [!abstract]- Formules
> $$
> P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \Longleftrightarrow \quad P(A \cap B) = P(A \mid B) \cdot P(B)
> $$

> [!example]+ Probabilité de $A$ à priori
> $$
> P(A) = \sum_{k=1}^{\infty} P(A \cap E_k) = \sum_{k=1}^{\infty} P(A \mid E_k) \cdot P(E_k)
> $$

> [!example]+ Probabilité de $A$ à postériori
> $$
> P(A \mid T) = \frac{P(A)P(T \mid A)}{P(T)} = \frac{P(A)P(T \mid A)}{P(A)P(T \mid A) + P(A^c)P(T \mid A^c)}
> $$
## Indépendance

> [!abstract]- Formules
> $$
> \begin{align*}
> P(A \cap B) &= P(A) \cdot P(B) \\
> P(A \mid B) &= P(A)\\
> P(B \mid A) &= P(B)
> \end{align*}
> $$
