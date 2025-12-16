---
title: automate non-déterministe
authors: Mihai Bors
tags: []
---

# automate fini non-déterministe (AFN)
- un automate fini non-déterministe (AFN) $A$ sur un alphabet $\Sigma$ est un 4-uplet $(Q,q_0,F, \Delta)$
	- $Q$ : ensemble fini d'els = états
	- $q_0 \in Q$ : état initial
	- $F \subseteq Q$ : ensemble d'états dits finaux/acceptants
	- $\Delta \subseteq Q \times \Sigma \times Q$ : relation de transition

## AF vs AFN
- tout langage accepté par un atomate fini (déterministe) peut être accepté par un automate fini non-déterministe
