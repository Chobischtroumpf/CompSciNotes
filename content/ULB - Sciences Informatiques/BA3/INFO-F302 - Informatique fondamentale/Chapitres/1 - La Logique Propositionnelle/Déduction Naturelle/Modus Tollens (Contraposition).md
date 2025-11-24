---
title: Modus Tollens (Contraposition)
authors: Alessandro Dorigo
tags:
  - InfoFond
---


Supposons que $x \rightarrow y$ et $\neg y$ soient vraies, si $x$ est vrai alors par la règle du modus ponens on peut dériver $y$ ce qui est en contradiction avec le fait que $\neg y$ est vrai, donc on en déduit que $\neg x$ est vrai.

$$\frac{\phi \rightarrow \psi \quad \neg \psi}{\neg \phi} MT$$

> [!example] Exemple
> 1. S'il pleut alors la route est mouillée
> 2. La route n'est pas mouillée
>
> Alors on peut déduire qu'il ne pleut pas

> [!example] Application
> $x \rightarrow (y \rightarrow z), x, \neg z \vdash \neg y$
> 1. $x \rightarrow (y \rightarrow z)$ prémisse
> 2. $x$ prémisse
> 3. $\neg z$ prémisse
> 4. $y \rightarrow z \rightarrow_{MP}, 1,2$
> 5. $\neg y \rightarrow_{MT}, 4,5$
