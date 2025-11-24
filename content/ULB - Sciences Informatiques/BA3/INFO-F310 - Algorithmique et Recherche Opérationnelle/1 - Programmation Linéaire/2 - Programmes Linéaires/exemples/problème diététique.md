---
title: problème diététique
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
## Énoncé

> [!info]+ Énoncé
>
> Déterminer la composition, à coût minimal, d'un aliment pour bétail qui est obtenu en mélangeant au plus deux produits (orge et arachide).
>
> - Quantité nécessaire par portion = 400g
> - L'aliment doit comporter au moins 30% de protéines et au plus 5% de fibres

## Données

|Aliment (pour 1g)|Protéines|Fibres|Coût (€/kg)|
|---|---|---|---|
|Orge|0.09|0.02|1.5|
|Arachide|0.6|0.06|4.5|

## Variables

- $x_1$ : quantité d'orge (en grammes)
- $x_2$ : quantité d'arachides (en grammes)
- $x_1 + x_2$ : quantité totale

## Fonction objectif

$$ \min z = 0.0015x_1 + 0.0045x_2 $$

**Contraintes**

$$ \begin{align} x_1 + x_2 &\geq 400 \ 0.09x_1 + 0.6x_2 &\geq 0.3(x_1 + x_2) \ 0.02x_1 + 0.06x_2 &\leq 0.05(x_1 + x_2) \ x_1, x_2 &\geq 0 \end{align} $$
