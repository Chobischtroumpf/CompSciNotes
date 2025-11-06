---
title: Problème des 8 reines
authors: Alessandro Dorigo
tags:
  -
---

![[Pasted image 20251007165146.png]]
## codage en PySAT
- variable booléenne
	- entier positif
- classe `IDPool` : créer automatiquement un codage des objets qu'on veut manipuler
	- _ex. des entiers positifs_
- classe `CNF`: représente une formule en FNC
	- chq clause = liste de litéraux
	- formule = liste de clauses

### code
#### code de départ
```python
from pysat.solvers import Minisat22
from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool

nb = 8 #nb reines

affichage_sol = True

vpool = IDPool(strat_from = 1) # pour stockage des identifiants entiers des couples (i,j)

cnf = CNF() # construction objet formule en CNF

# ajout d'un ensemble de cntrainte qui code la contrainte qu'il existe au moins une reine par ligne i
for i in range(nb) :
	d = [] # disjonction de litéraux
	for j in range (nb) :
		d.append(vpool.id((i,j)))
	cnf.append(d)

# encodage contraintes : pas d'attaque en ligne ni d'attaque en colonne
# pas d'attaque en ligne
for i in range(nb) :
	for j in range(nb):
		for k in range(nb) :
			if k > j:
				cnf.append([-vpool.id((i,j)), -vpool.id((i,k))])

# pas attaque en colonne
for i in range(nb) :
	for j in range(nb) :
		for k in range(nb) :
			if k > j :
				cnf.append([-vpool.id((j,i)), -vpool.id((k,i))])
```
#### code pour les restrictions de la diagonale
```python
# pas attaque en diagonale V1
for i in range(nb):
	for j in range(nb) :
		for k in range(nb) :
			for l in range(nb):
				if abs(i - k) == abs(j-l) and i != k:
					cnf.append([-vpool.id((i,j)), -vpool.id((k,l))])

# pas attaque en diagonale version optimisée
# cas 1
for i in range(nb):
	for j in range(nb):
		for k in range(nb-1):
			if i + k + 1 < nb and j + k + 1 < nb:
				cnf.append([-vpool.id((i,j)), -vpool.id((i+k+1, j + k + 1))])

# cas 2
for i in range(nb) :
	for j in range(nb) :
		for k in range(nb-1):
			if i + k + 1 < nb and j - k - 1 >= 0 :
				cnf.append([-vppol.id((i,j)), -vpool.id((i+k+1, j-k-1))])
```
![[Pasted image 20251007170942.png]]
#### lancement d'un solveur
```python
# phase résolution

s = Minisat22(use_timer=True) # utiliser solveur MiniSAT
# utilisation d'un solveur
# paramètre permet de compter le temps passé à la résolution

# s = Glucose4(use_timer=True) # utiliser solveur Glucose

s.append_formula(cnf.clauses, no_return=False)
#ajoute la formule au solveur

print("Résolution")
res = s.solve() # lance le solveur et retourne le résultat dans res
print("satisfaisable : " + str(res))
print("temps de résolution : " + '{0:.2f}s'.format(s.time()))
```
→ résolution incrémentale : si on ajoute de nouvelles clauses à `s` et qu'on appelle une 2e fois la méthode `solve()` - réutilisation des calculs déjà faits lors du premier appel

### comment trouver une solution différente ?
Soit V: X → {0,1}, la solution (interprétation) trouvée par le solveur. Comment obtenir une interprétation différente ?
- on se base sur l'observation suivante, pour tout V':X → {0,1}
- $V \neq V' \leftrightarrow \exists (i,j) \in \set{1,...,8}^2, V(x_{i,j}) \neq V'(x_{i,j})$
- → comme V est la solution trouvée et V', une nouvelle soltuion à trouver, on peut utiliser la formule suivante :
$\bigvee_{(i,j) \in \set{1,...,8}^2, V(x_{i,j}) = 1} \neg x_{i,j} \vee \underbrace{\bigvee_{i,j, v(x_{i,j}) = 0} x_{i,j}}_{\text{ pas nécessaire}}$
