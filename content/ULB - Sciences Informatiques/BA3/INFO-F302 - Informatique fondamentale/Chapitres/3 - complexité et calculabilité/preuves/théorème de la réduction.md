# théorème (réduction)
	- Soient $A,B$ deux prb de décision 
	- Si $A$ est $NP$-dur et $A$ se réduit à $B$ en temps polynomial 
	- → $B$ est $NP$-dur
## preuve
- Pour démontrer que $B$ est $NP$-dur, il faut démontrer que tout prb de $NP$ se réduit à $B$ en tps polynomial 
- Soit $X$ un prb quelconque de $NP$ 
- Comme $A$ est $NP$-dur, $X$ se réduit à $A$ en tps polynomial 
- De plus, comme $A$ se réduit à $B$ en tps polynomial
	- par le lemme de composition de réductions
	- → on peut composer les deux réductions pour réduire $X$ à $B$  en tps polynomial