---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

# 10: Hachage
- De nombreuses applications ont besoin d’un ensemble dynamique qui permet les opérations `INSERT`, `DELETE` , `SEARCH`.
- Table de symboles $S$ contenant $n$ enregistrements.

| ![[Pasted image 20240327143048.png]] | ![[Pasted image 20240327143407.png]] |
| :----------------------------------: | :----------------------------------: |

Supposons que les clés appartiennent à l'ensemble $U \subseteq \{0, 1, \ldots, m-1\}$ et qu'elles sont toutes distinctes.
- Tableau $T[0 .. m-1]$:
$$T[k] = \begin{cases}
x & \text{si } x \in S \text{ et } \text{key}[x] = k, \\
\text{NULL} & \text{sinon}.
\end{cases}$$
## Résolution des collisions par chaînage
- Quand un enregistrement à insérer est envoyé sur un espace déjà utilisé dans $T$, une collision se produit.

| ![[Pasted image 20240327143525.png]] | ---------------------------------------------------------------------------------- |
| :----------------------------------: | :--------------------------------------------------------------------------------: |

### Pire cas
- Tous les enregistrements sont envoyés sur le même emplacement.
- Temps d'accès : $\Theta(n)$ si $|S| = n$.
### Analyse du hachage avec liste chaînées
- **Hypothèse:** hachage uniforme simple: chaque clé $k \in S$ a la même probabilité d'être envoyée sur chaque emplacement de $T$, indépendamment des autres clés.
- Soient
	- $n$ le nombre de clés dans la table,
	- $m$ le nombre d'emplacements.
- Le facteur de charge (load factor) de $T$ est défini par $$ \alpha = \frac{n}{m} $$
	- i.e. le nombre moyen de clés par emplacement.
- On suppose que le calcul de $h(k)$ est réalisable en $O(1)$.
## Choix d'une bonne fonction de hachage
- Une bonne fonction de hachage devrait distribuer les clés uniformément dans les emplacements de la table.
- La régularité dans la distribution des clés ne doit pas affecter l’uniformité de la distribution.
## Méthode de division
$$h(k)= k \mod m$$
- Éviter un $m$ qui a un petit diviseur $d$, car une prépondérance de clés congruentes modulo $d$ peut affecter l'uniformité.
- Si $m = 2^r$, le hachage ne dépend même pas de tous les bits de $k$:
$$k = 1011000111 \ 011010_2 \ \ \ \ \ \ \ r = 6 \ \ \ \ \ \ \ h(k) = 011010_2$$

Choisir $m$ premier, pas trop proche d’une puissance de 2 ou 10, et pas trop utilisé dans l’environnement de calcul.
## Méthode de multiplication
Supposons que $m = 2^r$ et notre ordinateur utilise des mots de $w$ bits.
$$h(k) = (Ak \mod 2^w) \text{ rsh } (w - r)$$
où $rsh$ est l'opérateur "bitwise right-shift" (`>>` en C et java) et $A$ est un entier impair tel que $2^{w-1} < A < 2^w$.
- Ne pas prendre $A$ trop proche de $2^{w-1}$ ou $2^w$.

![[Pasted image 20240327144907.png]]
## Adressage ouvert
- Aucun stockage n’est fait hors de la table de hachage.
- L’insertion sonde systématiquement la table jusqu’à trouver un emplacement vide.

| ![[Pasted image 20240327145016.png]] | ![[Pasted image 20240327145025.png]] |
| :----------------------------------: | :----------------------------------: |
## Sondage linéaire
Étant donné une fonction de hachage ordinaire $h'(k)$, le sondage linéaire utilise la fonction:
$$h(k, i) = (h'(k) + i) \mod m$$
- Problème majeur: "primary clustering", de longues séquences d'emplacements occupés se créent, augmentant le temps moyen de recherche.
## Double hachage
Étant données deux fonctions de hachage ordinaire $h_1(k)$ et $h_2(k)$, le double hachage utilise la fonction:
$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \mod m$$
- Cette méthode produit généralement d’excellents résultats, mais $h_2(k)$ et $m$ doivent être premiers entre eux. Une manière de faire est de prendre pour $m$ une puissance de 2 et de concevoir $h_2(k)$ de sorte qu’elle ne produise que des nombres impairs.
