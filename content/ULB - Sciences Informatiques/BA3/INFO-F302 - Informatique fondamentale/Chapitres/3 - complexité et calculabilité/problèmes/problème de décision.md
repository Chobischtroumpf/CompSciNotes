# problèmes de décision 
- restriction d'études aux prb de décisions (dont la réponse est oui ou non)
- on peut définir un problème de décision comme un langage de mots sur un alphabet fini $\Sigma$ 
	- $\Sigma^*$ l'ensemble des mots  sur un alphabet $\Sigma$ ($\epsilon$ le mot vide)
	- un langage sur $\Sigma$ est un sous-ensemble $L \subseteq \Sigma^*$ 
	- _ex. $\Sigma = \set{0,1}, 00100 \in \Sigma^*$_

- → problème de décision = langage $P \subseteq \Sigma^*$ 
	- N.B. : chaque langage $P$ rep bien un prb dont la rep est oui ou non, en l'identifiant à sa fonction caractéristique $\chi_p$
$$
\begin{gather}
\chi_p : \Sigma^* \to {0,1} \\
\ u \mapsto \begin{cases} 1 \text{ si } u \in P \\ 0 \text{ si } u \not \in P\end{cases}
\end{gather}
$$
