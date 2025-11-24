---
title: Combinatoire
authors: Alessandro Dorigo
tags:
  - Combinatoire
  - Maths
  - Proba
---

## Permutations

> [!abstract]- Formule
> $$n!$$

> [!example]+ Exemple
> Si tu as 5 livres différents et que tu veux les organiser sur une étagère, de combien de façons différentes peux-tu les organiser?
> $$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$$
## Arrangements (avec répétition)

> [!abstract]- Formule
> $$A_{n,k} = n^k$$

> [!example]+ Exemple
> Si tu veux créer un code de 3 chiffres où chaque chiffre peut être de 0 à 9 (donc 10 possibilités pour chaque chiffre), le nombre de codes possibles est:
> $$A_{10,3} = 10^3 = 1000$$
## Arrangements (sans répétition)

> [!abstract]- Formule
> $$A_{n,k} = \frac{n!}{(n-k)!}$$

> [!example]+ Exemple
> Si tu as 7 personnes et que tu veux choisir 3 d'entre elles pour former une équipe (sans répétition), le nombre de façons de le faire est:
> $$A_{7,3} = \frac{7!}{(7-3)!} = \frac{7 \times 6 \times 5}{1} = 210$$
## Combinaisons

> [!abstract]- Formule
> $$C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

> [!example]+ Exemple
> Si tu veux choisir 3 fruits parmi 5 différents (par exemple: pomme, banane, orange, raisin, poire) sans se soucier de l'ordre, le nombre de combinaisons possibles est:
> $$C_{5,3} = \binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5 \times 4 \times 3}{3 \times 2 \times 1} = 10$$
