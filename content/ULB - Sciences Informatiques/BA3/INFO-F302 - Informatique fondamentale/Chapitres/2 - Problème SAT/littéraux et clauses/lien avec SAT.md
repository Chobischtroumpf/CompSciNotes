---
title: lien avec SAT
authors: Alessandro Dorigo
tags:
  - InfoFond
---

- possible de faire un algo de complexité au pire des cas en temps polynomiale pour tester satisfaisabilité d'une formule FND  ?
	- rep : oui
```
FIND_SOLVE(Phi : formule en FND)
	pour toute conjonction C de Phi
		Si C ne contient pas de litéraux contradictoires
			retourner true

	retourner false
```
→ pas correct car la mise sous FND crée, au pire, une formule exponentiellement plus grande
