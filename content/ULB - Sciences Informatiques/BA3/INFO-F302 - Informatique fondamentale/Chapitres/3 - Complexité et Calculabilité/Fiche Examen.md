---
title: Fiche Examen
authors: Mihai Bors
tags:
  - InfoFond
---
Pour montrer que $X \in NP$ :
1. définir un **certificat naturel** (coloriage, clique, valuation, cycle, etc.)
2. montrer que sa **vérification est polynomiale**

## Réductions polynomiales

**Définition** : $A \le_p B$ s'il existe une fonction $f$ calculable en temps polynomial telle que :
$$u \in A \iff f(u) \in B$$

### Lemme 1 — Composition

Si :
$$A \le_p B \quad \text{et} \quad B \le_p C$$
alors :
$$A \le_p C$$

### Lemme 2 — Conservation de la facilité

Si :
$$A \le_p B \quad \text{et} \quad B \in P$$
alors :
$$A \in P$$

*(Très utilisé pour les preuves par contradiction)*

## NP-dur et NP-complet

**NP-dur** : $X$ est NP-dur si :
$$\forall Y \in NP,\ Y \le_p X$$

**NP-complet** : $X$ est NP-complet ssi :
- $X \in NP$
- $X$ est NP-dur

### Lemme 3 — Méthode standard de NP-complétude

Pour montrer que $X$ est NP-complet :
1. montrer $X \in NP$
2. réduire un problème NP-complet connu vers $X$


### Lemme 4 — Héritage de dureté

Si $A$ est NP-dur et $A \le_p B$, alors $B$ est NP-dur.

## SAT

**Théorème de Cook (1971)**
$$SAT \text{ est NP-complet}$$

Conséquence :
- tout problème de $NP$ se réduit à SAT
- SAT est la source principale des réductions

### Lemme 5 — NP-complet dans P

Si un problème NP-complet est dans $P$, alors :
$$P = NP$$

### Lemme 6 — Contraposée

Si :
$$
P \neq NP
$$
alors :
$$
\forall X\ \text{NP-complet},\ X \notin P
$$

En particulier :
$$
P \neq NP \Rightarrow SAT \notin P
$$

### Lemme 7 — Équivalences classiques (QCM)

Pour un problème NP-complet $X$, les assertions suivantes sont équivalentes :
- $X \notin P$
- $SAT \notin P$
- aucun problème NP-complet n'est dans $P$

## Schémas de preuve type examen

### Schéma A — « Si P ≠ NP alors X ∉ P »

1. supposer $X \in P$
2. utiliser que $X$ est NP-complet
3. déduire que tout $Y \in NP$ est dans $P$
4. conclure $P = NP$ (contradiction)

### Schéma B — Montrer $X \in NP$

> « On prend comme certificat …
> Sa taille est polynomiale
> Sa vérification est polynomiale »

### Schéma C — Montrer NP-dur

> « On réduit SAT / 3SAT / Clique vers $X$ en temps polynomial »

## À savoir reconnaître sans réfléchir

- SAT, 3-SAT, Clique, Vertex Cover, Graph Coloring, Bin Packing → NP-complets
- $P \subseteq NP$ toujours vrai
- Une réduction **ne prouve jamais** que deux problèmes ont la même complexité
