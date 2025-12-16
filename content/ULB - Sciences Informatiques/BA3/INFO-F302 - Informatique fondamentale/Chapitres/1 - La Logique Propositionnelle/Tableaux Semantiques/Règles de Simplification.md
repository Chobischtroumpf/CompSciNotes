---
title: Règles de Simplification
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les **règles de simplification** sont utilisées dans la méthode des [[Tableau Sémantique|tableaux sémantiques]] pour décomposer les formules complexes en formules plus simples.

## $\land$-Règles

> [!abstract]+ Règles de Conjonction
> Étant donné un ensemble $S$ contenant une formule $\alpha$, on crée un ensemble fils égal à $S \setminus \{\alpha\}$ auquel on ajoute $\alpha_1$ et $\alpha_2$.
>
> | $\alpha$ | $\alpha_1$ | $\alpha_2$ |
> |:--------:|:----------:|:----------:|
> | $\neg\neg\phi$ | $\phi$ | |
> | $\phi_1 \land \phi_2$ | $\phi_1$ | $\phi_2$ |
> | $\neg(\phi_1 \lor \phi_2)$ | $\neg\phi_1$ | $\neg\phi_2$ |
> | $\neg(\phi_1 \rightarrow \phi_2)$ | $\phi_1$ | $\neg\phi_2$ |
> | $\phi_1 \leftrightarrow \phi_2$ | $\phi_1 \rightarrow \phi_2$ | $\phi_2 \rightarrow \phi_1$ |

^71c7ba

> [!tip]+ Interprétation
> Toutes les formules $\alpha$ peuvent être considérées comme équivalentes à des conjonctions.
>
> **Exemple** : $\neg(\phi_1 \lor \phi_2)$ est équivalent à $\neg\phi_1 \land \neg\phi_2$ (loi de De Morgan).

## $\lor$-Règles

> [!abstract]+ Règles de Disjonction
> Étant donné un ensemble $S$ contenant une formule $\beta$, on crée deux ensembles fils :
> - L'un étant $(S \cup \{\beta_1\}) \setminus \{\beta\}$
> - L'autre $(S \cup \{\beta_2\}) \setminus \{\beta\}$
>
> | $\beta$ | $\beta_1$ | $\beta_2$ |
> |:-------:|:---------:|:---------:|
> | $\phi_1 \lor \phi_2$ | $\phi_1$ | $\phi_2$ |
> | $\neg(\phi_1 \land \phi_2)$ | $\neg\phi_1$ | $\neg\phi_2$ |
> | $\phi_1 \rightarrow \phi_2$ | $\neg\phi_1$ | $\phi_2$ |
> | $\neg(\phi_1 \leftrightarrow \phi_2)$ | $\neg(\phi_1 \rightarrow \phi_2)$ | $\neg(\phi_2 \rightarrow \phi_1)$ |

^f8ffbf

> [!tip]+ Interprétation
> Toutes les formules $\beta$ peuvent être considérées comme équivalentes à des disjonctions.
>
> **Exemple** : $\neg(\phi_1 \land \phi_2)$ est équivalent à $\neg\phi_1 \lor \neg\phi_2$ (loi de De Morgan).

## Justification

> [!note]+ Équivalences Logiques
> Ces règles sont basées sur les équivalences logiques fondamentales :
>
> - **Lois de De Morgan** :
>   - $\neg(A \land B) \equiv \neg A \lor \neg B$
>   - $\neg(A \lor B) \equiv \neg A \land \neg B$
>
> - **Implication** :
>   - $A \rightarrow B \equiv \neg A \lor B$
>
> - **Équivalence** :
>   - $A \leftrightarrow B \equiv (A \rightarrow B) \land (B \rightarrow A)$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Tableau Sémantique]]** : Algorithme utilisant ces règles
> - **[[Satisfaisabilité]]** : Propriété testée via les tableaux
> - **[[Sémantique]]** : Justification théorique des règles
