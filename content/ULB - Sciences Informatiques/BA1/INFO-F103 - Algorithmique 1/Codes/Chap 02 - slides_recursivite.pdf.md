---
title: Chap 02 - slides_recursivite.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Factorielle récursive
### Slide 11
```Python
def factorielle(n):
	if n == 0: # Référence à un cas simple qui ne fait pas référence, directement ou indirectement, à un objet identique (2)
		return 1
	else:
		result = n ∗ factorielle(n − 1) # Référence directe à un objet identique (1) et référence directe à un objet identique mais de plus petite taille (3)
		return result
```
# Factorielle itérative
### Slide 28
```Python
def factorielle(n):
	result = 1
	while n > 1:
		result = result ∗ n
		n = n − 1
	return result
```
# Fibonacci récursif
### Slide 29
```Python
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n − 1) + fibonacci(n − 2)
```
# Fibonacci itératif
### Slide 30
```Python
def fibonacci(n):
	precedent = 0
	result = 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		for i in range(n − 1):
			result = result + precedent
			precedent = result − precedent
		return result
```
# Recherche dans une liste
### Slide 58
```Python
def recherche(alist, item):
	return item in alist
```
# Recherche séquentielle dans une liste
### Slide 59
```Python
def rechSequentielle(alist, item):
	pos = 0
	found = False
	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos = pos + 1
	return found
```
# Recherche séquentielle dans une liste triée
### Slide 61
```Python
def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False
	while pos < len(alist) and not found and not stop:
		if alist [pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos = pos + 1
	return found
```
# Recherche dichotomique
### Slide 63
```Python
def rechDicho(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return rechDicho(alist[:midpoint], item)
			else:
				return rechDicho(alist[midpoint + 1:], item)
```
# Recherche dichotomique itérative
### Slide
```Python
def rechDicho(alist, item):
	first = 0
	last = len(alist) − 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint − 1
			else:
				first = midpoint + 1
	return found
```
# Changement de base récursive
```Python
unites = '0123456789ABCDEF'

def convert(n, base):
	if n < base:
		return unites[n]
	else:
		return convert(n // base, base) + unites[n % base]
```
# Changement de base itérative
```Python
def convert(n, base):
	pile = Stack()
	while n >= base:
		pile.push(n)
		n = n // base
	res = unites[n]
	while not pile.isEmpty():
		n = pile.pop()
		res = res + unites[n % base]
	return res
```
# Conversion d'une expression infixe en postfixe
```Python
class ExpressionInfixe:
	def __init__(self, chaine):
		self.nad = chaine
		self.npi = ' '
		self.i = 0
		self.operande = '0123456789abcdefghijklmnopqrstuvwxyz'
		self.getcar()
		self.val = self.expr()

	def getcar(self):
		self.c = ' '
		if self.i < len(self.nad):
			self.c = self.nad[self.i]
		self.i = self.i + 1

	def putcar(self, caractere):
		self.npi = self.npi + caractere

	def expr(self):
		self.terme()
		while self.c == '+' or self.c == '-':
			operateur = self.c
			self.getcar()
			self.terme()
			self.putcar(operateur)
			self.putcar(' ')

	def terme(self):
		self.facteur()
		while self.c == '∗'  or self.c == '/':
			operateur = self.c
			self.getcar()
			self.facteur()
			self.putcar(operateur)
			self.putcar(' ')

	def afficheNAD(self):
		return self.nad

	def afficheNPI(self):
		return self.npi
```
# Evaluation d’une expression infixe
```Python
class ExpressionInfixe:
    def __init__(self, chaine):
        self.s = chaine
        self.i = 0
        self.getcar()
        self.val = self.expr()

    def valeur(self):
        return self.val

    def getcar(self):
        self.c = ' '
        if self.i < len(self.s):
            self.c = self.s[self.i]
            self.i = self.i + 1

    def expr(self):
        res = self.terme()
        while self.c == '+' or self.c == '−':
            if self.c == '+':
                self.getcar()
                res = res + self.terme()
            else:
                self.getcar()
                res = res - self.terme()
        return res

    def terme(self):
        res = self.facteur()
        while self.c == '*' or self.c == '/':
            if self.c == '*':
                self.getcar()
                res = res * self.facteur()
            else:
                self.getcar()
                res = res / self.facteur()
        return res

    def facteur(self):
        res = 0
        if self.c == '(':
            self.getcar()
            res = self.expr()
            self.getcar()
        elif self.c in '0123456789':
            while self.c in '0123456789':
                res = 10 * res + int(self.c)
                self.getcar()
        else:
            self.i = len(self.s)
        return res
```
# Problème consistant à trouver la plus grande valeur contenue dans une liste non triée de n éléments
```Python
def maximum(alist):
	res = alist[0]
	for i in range(1, len(alist)):
		if alist[i] > res:
			res = alist [i]
	return res
```
# Version divide and conquer
```Python
def maximumDivConquer(alist, g, d):
	if g == d:
		return alist[g]
	else:
		m = (g + d) // 2
		u = maximumDivConquer(alist, g, m)
		v = maximumDivConquer(alist, m + 1, d)
		if u > v:
			return u
		else:
			return v
```
