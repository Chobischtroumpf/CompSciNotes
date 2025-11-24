---
title: Théorème de McMillan
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!abstract]- Théorème de McMillan
> Tout [[Code univoque#^95f169|code univoque]] satisfait [[Inégalité de Kraft#^f120a9|l’inégalité de Kraft]].

Le théorème de McMillan s'applique à **tous** les codes univoques, y compris:
- Les codes univoques **avec préfixe** (non sans préfixe)
- Les codes à longueur variable quelconques
- Pas seulement les [[Code sans préfixe#^392e5f|codes sans préfixe]]

> [!abstract]- Corollaire 1.0.1
> Pour tout [[Code univoque#^95f169|code univoque]]:
> $$\ell_{\max} \geq \lceil \log_r q \rceil \geq \log_r q$$
> **Preuve**:
> $$1 \geq \sum_{i=1}^{q} r^{-\ell_i} \geq q \cdot r^{-\ell_{\max}} \implies r^{\ell_{\max}} \geq q$$

## Démonstration
- Soit $c = \sum_{i=1}^q r^{-\ell_i}$. On va montrer $\lim_{n \rightarrow \infty} \frac{c^n}{n} < \infty$:

![[f42aa4cd94f23f562fd895e3c8b0dd40.png]]
![[79ee53c17c6ff3e0925a8f67561cfde3.png]]
