---
title: Chap 07 - slides_heap.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Heap
### Slides 27 à 31
```Python
Class Heap:
	def __init__(self):
		self.heapList = []
		self.taille = 0

	def pere(self, indice):
		return (indice − 1) // 2

	def leftChild(self, indice):
		return (indice ∗ 2) + 1

	def rightChild(self, indice):
		return (indice ∗ 2) + 2

	def existe(self, indice):
		return indice <= self.taille −1

	def swapL(self, alist, indice1, indice2):
		tmp = alist[indice1]
		alist[indice1] = alist[indice2]
		alist[indice2] = tmp

	def priorityUp(self, i):
		while i > 0 and \
			self.heapList[i] > self.heapList[self.pere(i)] :
		self.swapL(self.heapList ,i ,self.pere(i))
		i = self.pere(i)

	def prioChild(self, i):
		if not self.existe(self.leftChild(i)):
			return −1
		elif not self.existe(self.rightChild(i)):
			return self.leftChild(i)
		else:
			if self.heapList[self.leftChild(i)] > \
					self.heapList[self.rightChild(i)]:
				return self.leftChild(i)
			else:
				return self.rightChild(i)

	def priorityDown(self, i):
		while self.existe(self.leftChild(i)):
			child = self.leftChild(i)
			mc = self.prioChild(i)
			if self.heapList[i] < self.heapList[mc]:
				self.swapL(self.heapList, i, mc)
			i = mc

	def insert(self, item):
		self.heapList.append(item)
		self.taille += 1
		self.priorityUp(self.taille-1)

	def delete(self):
		retval = self.heapList[0]
		self.heapList[0] = self.heapList[self.taille − 1]
		self.taille = self.taille − 1
		self.heapList.pop()
		self.priorityDown(0)
		return retval
```
# Heapsort
### Slide 53
```Python
def heapsort(array, array_size):
	h = Heap ( )
	for i in range(n):
		h.insert(a[i])
	for i in range(n−1,−1,−1):
		a[i] = h.delete()
```
