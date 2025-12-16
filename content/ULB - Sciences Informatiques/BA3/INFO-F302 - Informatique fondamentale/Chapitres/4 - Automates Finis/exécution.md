---
title: exécution
authors: Mihai Bors
tags: []
---

# exécution
## exécution pour AF
- une exécution de $A$
	- suite finie $e = p_0\sigma_1p_1\sigma_2...p_{n-1}\sigma_n p_n$ pour $n \geq 0$
		- $p0 = q_0$
		- $\forall i \in \set{0,...,n}, p_i \in Q$
		- $\forall i \in \set{1,...,n}, \sigma_i \in \Sigma$
		- $\forall i \in \set{0,..,n-1}, \delta (p_i, \sigma_{i+1}) = p_{i+1}$
			- $\sigma(p_i, \sigma_{i+1})$ est définit
	- exécution $e$ = exécution sur le mot $\sigma_1...\sigma_n$
		- et $e$ est acceptant si l'état atteint est final
			- ie $p_n \in F$

- Rq: la suite $q_0$ est une exécution sur le mot vide $\epsilon$
	- elle est acceptante ssi $q_0$ est final

## exécution pour AFN
- exécution de $A$ : suite finie
	- $e = p_0\sigma_1p_1\sigma_2...p_{n-1}\sigma_np_n$
		- $n \geq 0$
	- $p_0=q_0$
	- $\forall i=0:n, p_i \in Q$
	- $\forall i=1:n, \sigma_i \in \Sigma$
	- $\forall i = 0:n-1, (p_i, \sigma_{i+1}, p_{i+1}) \in \Delta$
- → $e$ exécution sur le mot $\sigma_1...\sigma_n$
- → $e$ est acceptante si l'état atteint est final
	- ie. $p_n \in F$
