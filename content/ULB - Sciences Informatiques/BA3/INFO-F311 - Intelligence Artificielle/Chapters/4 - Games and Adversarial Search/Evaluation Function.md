---
title: Evaluation Function
authors: Mihai Bors
tags:
  - AI
---


- Score non-terminals in depth-limited search
- Typically weighted linear sum of features:
	- $\text{EVAL}(s) = w_1 f_1(s) + w_2 f_2(s) + \dots + w_n f_n(s)$
- Or more complex non-linear functions trained via self-play RL

![[Pasted image 20251111134038.png]]
Chess positions to minimax tree

- Evaluation functions are always imperfect
	- Deeper search -> better play (but could give same quality of play if function is less accurate)
