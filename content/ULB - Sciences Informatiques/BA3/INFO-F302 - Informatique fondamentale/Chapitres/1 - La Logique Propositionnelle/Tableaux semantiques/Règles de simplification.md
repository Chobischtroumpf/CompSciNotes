---
title: Règles de simplification
authors: Alessandro Dorigo
tags:
  -
---

## $\land$-règles
> [!definition] $\land$-regles
> Étant donné un ensemble $S$ contenant une formule $\alpha$, on crée un ensemble fils égal $S \setminus {\alpha}$ auquel on ajoute $\alpha_1$ et $\alpha_2$.
>
| $\alpha$                          | $\alpha_1$                  | $\alpha_2$                  |
| --------------------------------- | --------------------------- | --------------------------- |
| $\neg\neg\phi$                    | $\phi$                      |                             |
| $\phi_1 \land \phi_2$             | $\phi_1$                    | $\phi_2$                    |
| $\neg(\phi_1 \lor \phi_2)$        | $\neg\phi_1$                | $\neg\phi_2$                |
| $\neg(\phi_1 \rightarrow \phi_2)$ | $\phi_1$                    | $\neg\phi_2$                |
| $\phi_1 \leftrightarrow \phi_2$   | $\phi_1 \rightarrow \phi_2$ | $\phi_2 \rightarrow \phi_1$ |


> [!tip]+ Remarque Toutes les formules $\alpha$ peuvent être considérées comme équivalentes à des conjonctions. Par exemple :
>
> $\neg(\phi_1 \lor \phi_2)$ est équivalent à $\neg\phi_1 \land \neg\phi_2$
## $\lor$-règles

> [!definition] $\lor$-règles
> Étant donné un ensemble $S$ contenant une formule $\beta$, on crée deux ensembles fils, l'un étant $(S \cup {\beta_1})\backslash\beta$, et l'autre $(S \cup {\beta_2})\backslash\beta$.
>
| $\beta$                               | $\beta_1$                         | $\beta_2$                         |
| ------------------------------------- | --------------------------------- | --------------------------------- |
| $\phi_1 \lor \phi_2$                  | $\phi_1$                          | $\phi_2$                          |
| $\neg(\phi_1 \land \phi_2)$           | $\neg\phi_1$                      | $\neg\phi_2$                      |
| $\phi_1 \rightarrow \phi_2$           | $\neg\phi_1$                      | $\phi_2$                          |
| $\neg(\phi_1 \leftrightarrow \phi_2)$ | $\neg(\phi_1 \rightarrow \phi_2)$ | $\neg(\phi_2 \rightarrow \phi_1)$ |

> [!tip]+ Remarque Toutes les formules $\beta$ peuvent être considérées comme équivalentes à des disjonctions. Par exemple :
>
> $\neg(\phi_1 \land \phi_2)$ est équivalent à $\neg\phi_1 \lor \neg\phi_2$
