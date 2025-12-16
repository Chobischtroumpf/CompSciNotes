---
title: exemple AFN
authors: Mihai Bors
tags: []
---

# automate non-déterministe
![[Pasted image 20251125153208.png]]
- sur un mot, il existe plusieurs exécution
	- → pour accepter le mot, au moins une doit être acceptante
- sur le mot $ababb$, on a
	![[Pasted image 20251125153319.png]]
	→ la troisième est acceptante donc le mot est accepté
- sur le mot $abbab$, on a
	![[Pasted image 20251125153359.png]]
	→ aucune n'est acceptante donc le mort est rejeté
