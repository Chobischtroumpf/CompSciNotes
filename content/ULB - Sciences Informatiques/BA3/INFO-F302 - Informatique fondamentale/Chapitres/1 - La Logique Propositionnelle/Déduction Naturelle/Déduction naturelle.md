---
title: Déduction naturelle
authors: Alessandro Dorigo
tags:
  - InfoFond
---


Règles qui nous permettent, pas par pas, de déduire des conclusions a partir de prémisses. La déduction naturelle nous permet de prouver qu'une formule est valide.

- Supposons donnée un ensemble de formules $\phi_1, \dots, \phi_n$ (prémisses) et une formule $\psi$ (conclusion).
- Supposons que l'on désire montrer que $\psi$ peut être dérivée de $\phi_1, \dots, \phi_n$, notée $\phi_1, \dots, \phi_n \vdash \psi$ (séquent).

- La dérivation syntaxique est formalisée avec des règles de déduction.
- Les règles de déduction permettent de faire le lien entre la syntaxe et la sémantique: $$\phi_1, \dots, \phi_n \vdash \psi \text{ ssi } \phi_1, \dots, \phi_n \models \psi$$ (tout ce qui est démontrable est valide, et tout ce qui est valide est démontrable)

$\vdash \phi$: "$\phi$ est prouvable"
$\models \phi$: "$\phi$ est valide"
