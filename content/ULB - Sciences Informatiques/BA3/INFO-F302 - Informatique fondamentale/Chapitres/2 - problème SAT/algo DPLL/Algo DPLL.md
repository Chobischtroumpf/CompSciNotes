---
title: Algo DPLL
authors: Alessandro Dorigo
tags:
  - InfoFond
---

## idée
- principe de base : engendrer et tester des solutions partielle
	- faire une valuation (partielle) qui satisfait la formule, peu importe l'interprétation des autres propositions de la même formule
- → algo DPLL propose des critères pour choisir quelles variables tester en premier
# Algo DPLL
## proposition pivot
- algo DPLL va essayer des interprétations partielle, la prop choisie = proposition pivot
	- → essayer successivement de mettre la prop à vrai ou à faux et tester récursivement la satisfaisabilité de formules simplifiées obtenues
	- le choix de la proposition choisie peut fortement influencer le résultat

**exemple**
![[Pasted image 20251014145706.png]]

### premier critère de choix : clauses unitaires
- une clause unitaire = clause qui ne contient qu'un seul littéral
	- force donc le choix de la valeur de la prop
		- _ex : $x \wedge(y \vee \neg z)$ - clause unitaire $x$ et on sait que pour satisfaire cette formule, il faut nécessairement interpréter $x$ par $1$_
	- algo DPLL choisi en priorité la prop d'une clause unitaire comme prop pivot
	- formule simplifiée obtenue peut elle mê contenir des clauses unitaires : _propagation des clauses unitaires_
- → optimisation essentielle des solveurs SAT (qui passent l'essentiel de leur temps à faire de la propagration des clauses unitaires)

**exemple**
$\phi = (x \vee y) \wedge \neg y \wedge (\neg x \vee y \vee \neg z)$
→ $\phi[y=0] = x \wedge(\neg x \vee \neg z)$
→ $\phi[y/0][x/1] = \neg z$
→ $\phi[y/0][x/1][z/0] = \top$
Donc $\phi$ est satisfaisable avec l'interprétation
$$
\begin{gather}
V(x) = 1 \\ V(y) = V(z) = 0
\end{gather}
$$

### deuxième critère de choix : proposition à polarité unique
Prenons la formule :
$\phi = (x \vee \neg y \vee z) \wedge (x \vee \neg z) \wedge (y \vee z) \wedge (x \vee \neg y)$
- dans cette formule, $x$ appraît toujours positivement, on peut donc directement lui assigner la valeur 1 sans être obligé de tester la valeur 0
- on peut de même avoir un effet cascade
	- $(x \vee \neg y) \wedge (y \vee \neg z_1) \wedge (\neg z_1 \vee \neg z_2)$

## pseudo code
- principe
	- génération d'interprétation partielle
	- proposition pivot est choisie avec le critère de clause unitaire d'abord, et de polarité ensuite
	- sinon lorsque les deux critères ne s'appliquent pas, une proposition est choisie au hasard

```
fonction DPLL(phi) = retourne Vrai <-> phi satisfaisable
	si phi = true alors retourner vrai
	sinon si phi = faux alors retourner faux

	sinon si phi contient clause unitaire x
		retourner DPLL(phi[x/1])
	sinon si phi contient une clause unitaire !x
		retourner DPLL(phi[x/0])

	sinon si phi contient une proposition x de polarité toujours positive
		retourner DPLL(phi[x/1])
	sinon si phi contient une proposition de polarité toujours négative
		retourner DPLL(phi[x/0])

	sinon dans tous les autres cas, choisir une proposition x au hasard
		retourner DPLL(phi[x/0]) ou DPLL(phi[x/1])
```
