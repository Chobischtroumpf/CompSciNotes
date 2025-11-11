---
title: théorème d'équivalence
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---

# théorème d'équivalence
- tout programme linéaire peut s'écrire sous forme standard **et** canonique

- opérations
	- $\min_x c^T x = - \max_x -c^Tx$
	- $a^T x = b \leftrightarrow \begin{cases} a^Tx \leq b \\ a^Tx \geq b \leftrightarrow -a^T x \leq -b \end{cases}$
	- $\begin{gather} a^T x \leq b \leftrightarrow a^T x + s = b, s(\text{ lack }) \geq 0 \\ a^T x \geq b \leftrightarrow a^T x - e = b, e(\text{xcess}) \geq 0 \end{gather}$
	- var. non resteintes $x$ : définir nouvelles variables
		- $x^+ = \max[0,x] \geq 0$
		- $x^- = \max[0,-x] \geq 0$
		- $x = x^+ - x^-$
- en gros on s'en fout des opération, c'est juste pour passer d'une forme à une autre
