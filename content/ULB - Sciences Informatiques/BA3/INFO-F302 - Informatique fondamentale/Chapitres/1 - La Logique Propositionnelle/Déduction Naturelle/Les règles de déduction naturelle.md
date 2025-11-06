---
title: Les règles de déduction naturelle
authors: Alessandro Dorigo
tags:
  -
---

>[!info] Introduction d'implication
$$\frac{\begin{array}{c} \phi \quad \text{hyp.} \quad \; \\ \vdots \quad \quad \quad \ \ \  \ \  \\ \psi \quad \text{fin hyp.}\end{array}}{\phi \to \psi}\;\to i$$

>[!info] Introduction de disjonction
>$$\frac{\phi}{\phi \vee \psi} \vee_{i_{1}} \quad \quad \frac{\psi}{\phi \vee \psi} \vee_{i_{2}}$$

>[!info] Élimination de disjonction
>$$\frac{\begin{array}{c} \quad \quad \quad \quad \quad \phi_{1} \quad \text{hyp.} \quad \quad \phi_{2} \quad \text{hyp.}\\ \quad \quad \quad \vdots \ \ \quad \quad \quad \quad\quad  \ \vdots \quad \\ \phi_{1} \wedge \phi_{2} \quad \quad \ \ \ \ \ \ \psi \quad \text{fin hyp.} \quad \psi \quad \text{fin hyp.} \end{array}}{\psi}\;\vee e$$

>[!info] Élimination de la négation
>$$\frac{\perp}{\phi}\perp_{e}$$

>[!info] Élimination de négation
>$$\frac{\phi \quad \neg \phi}{\perp} \neg e$$

>[!info] Introduction de négation
>$$\frac{\begin{array}{c} \phi \quad \text{hyp.} \quad \; \\ \vdots \quad \quad \quad \quad \\ \ \perp \quad \text{fin hyp.}\end{array}}{\neg \phi}\;\neg i$$
