---
title: Extra
authors: Alessandro Dorigo
tags:
  - Algo
---


>[!info]+ P
> $$P = \bigcup_{k \geq 0} \{\text{problèmes de décision qu'on peut résoudre en temps } O(n^k)\}$$
> - Où $n$ = taille de l'instance $(|V| + |E|)$
> - Taille de l'instance = nombre de bits pour écrire le problème

>[!info]+ NP
> $$NP = \bigcup \{\text{problèmes de décision qu'on peut vérifier en } O(n^k)\}$$
> - On vérifie uniquement les instances "oui"
> - Si la réponse est "oui", on doit pouvoir montrer un "certificat" (et le vérifier facilement)
> - $P \subseteq NP$

>[!info]+ NP-Complet
> Un problème $Q \in NP$ est **NP-complet** si pour tout $R \in NP$, il existe une réduction polynomiale $R \rightarrow Q$

>[!tip]+ Premier problème NP-complet
> - Le premier problème NP-complet identifié est **SAT** (problème de satis-faisabilité)
> - SAT: déterminer si une formule booléenne quelconque sur un ensemble de variables est satisfaisante
> - Tous les autres problèmes NP-complets se basent sur SAT (on part d'un problème NP-complet pour en montrer un autre)
