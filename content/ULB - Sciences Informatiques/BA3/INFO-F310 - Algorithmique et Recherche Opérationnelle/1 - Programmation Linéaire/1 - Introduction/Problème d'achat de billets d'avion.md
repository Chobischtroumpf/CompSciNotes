---
title: Problème d'achat de billets d'avion
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Énoncé
> Un homme d'affaires doit effectuer 5 voyages entre Fayetteville (FYV) et Denver (DEN), en partant le lundi de FYV et revenant le mercredi de DEN à FYV.
> - Un billet aller-retour coûte $400
> - Un billet aller simple coûte 75% d'un billet aller-retour
> - Une réduction de 20% est appliquée si un weekend est inclus
>
> Comment acheter les billets pour les 5 semaines (à un prix minimum)?

**Restrictions**: FYV-DEN le lundi et DEN-FYV le mercredi de la même semaine

## Solutions
1) Acheter 5 aller-retour FYV-DEN-FYV normaux: $$5 \times \$400 = \$2000$$
2) Acheter un aller simple FYV-DEN, 4 aller-retour DEN-FYV-DEN comprenant un weekend et un aller simple DEN-FYV: $$(0.75 \times \$400) + (4 \times 0.8 \times \$400) + (0.75 \times 400) = \$1880$$
3) Acheter un aller-retour FYV-DEN-FYV pour le lundi de la première semaine et mercredi de la dernière semaine et 4 aller-retour DEN-FYV-DEN comprenant un weekend pour les autres voyages: $$5 \times 0.8 \times \$400 = \$1600$$
