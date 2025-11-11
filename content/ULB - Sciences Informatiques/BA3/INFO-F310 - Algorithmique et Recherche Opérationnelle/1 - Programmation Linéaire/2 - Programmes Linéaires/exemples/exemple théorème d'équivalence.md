- forme standard
	- var d'écart $s_1, s_2, s_3, s_4 \geq 0$
	- $\max z = 5x_1 + 4x_2$
	- contraintes
		- $6 x_1 + 4 x_2 + s_1 = 24$
		- $x_1 + 2x_2 + s_2 = 6$
		- $x_2 + s_3 = 2$
		- $-x_1 + x_2 + s_4 = 1$
		- $x_1, x_2, s_1, s_2, s_3, s_4 \geq 0$

- forme matricielle

$$
c = \begin{pmatrix} 5 \\ 4 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, x = \begin{pmatrix} x_1 \\ x_2 \\ s_1 \\ s_2 \\ s_3 \\ s_4 \end{pmatrix}, A = \begin{pmatrix} 6 & 4 & 1 & 0 & 0 & 0 \\ 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}, b = \begin{pmatrix} 24 \\ 6 \\ 2 \\ 1 \end{pmatrix}
$$

**variables en base B = {s1, s2, s3, s4}**
$$
\begin{gather} s_1 = 24 - 6x_1 - 4x_2 \\ s_2 = 6 - x_1 - 2x_2 \\ s_3 = 2 - x_2 \\ s_4 = 1 + x_1 - x_2\end{gather}
$$
- Si $x_1 = x_2 = 0$ (donc $x_1, x_2$ hors base), alors $s_1 = 24, s_2 = 6, s_3 = 3, s_4 = 1$
→ ttes les val des variables en base sont non-neg
→ sol de base (0,0,24,6,2,1) = solution de base réalisable
