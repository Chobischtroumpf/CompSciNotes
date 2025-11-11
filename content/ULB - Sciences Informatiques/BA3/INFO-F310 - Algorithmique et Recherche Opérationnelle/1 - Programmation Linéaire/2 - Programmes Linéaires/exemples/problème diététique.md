## énoncé
déterminer la compo, à coùut minimal, d'un aliment pour bétail qui est obtenu en mélangeant au plus deux prod (orge et arachide)
- quantité nécessaire par portion = 400g
- → aliment doit comporter au moins 30% de prot et au plus 5% de fibres

## données

| aliment (pour 1g) | prot | fibre | cout        |
| ----------------- | ---- | ----- | ----------- |
| orge              | 0.09 | 0.03  | 1.5(€ / kg) |
| arachide          | 0.6  | 0.06  | 4.5(€/kg)   |

## variables
- x1 : qtt orges (en grammes)
- x2 : qtt d'arachides (en grammes)
- → x1 + x2 : qtt totale

## fonction objectif
$\min z = 0.0015x_1 + 0.0045x_2$
- contraintes
	- $x_1 + x_2 \geq 400$
	- $0.09x_1 + 0.6x_2 \geq 0.3(x_1 + x_2)$
	- $0.02x_1 + 0.06x_2 \leq 0.05(x_1 + x_2)$
	- $x_1,x_2 \geq 0$
