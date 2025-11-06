---
title: Chap 06 - slides_abr.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Nœud Bidirectionnel
### Slides 8 et 9
```python
class NodeBidir:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.previous = None

		def getData(self):
			return self.data

		def getNext(self):
			return self.next

		def getPrevious(self):
			return self.previous

		def setData(self, newdata):
			self.data = newdata

		def setNext(self, newnext):
			self.next = newnext

		def setPrevious(self, newprevious):
			self.previous = newprevious
```

# Liste Circulaire Bidirectionnelle
### Slides 10, 11 et 12
```python
class ListeCircBidir:
	def __init__(self) -> None:
		self.head = NodeBidir(-1)
		self.head.setNext(self.head)
		self.head.setPrevious(self.head)
		self.count = 0

	def isEmpty(self):
		return self.head.getNext() == self.head

	def add(self, item):
		temp = NodeBidir(item)
		temp.setNext(self.head.getNext())
		temp.setPrevious(self.head)
		self.head.getNext().setPrevious(temp)
		self.head.setNext(temp)
		self.count = self.count + 1

	def addAfter(self, base, item):
		temp = NodeBidir(item)
		temp.setNext(base.getNext())
		temp.setPrevious(base)
		base.getNext().setPrevious(temp)
		base.setNext(temp)
		self.count = self.count + 1

	def length(self):
		return self.count

	def tete(self):
		return self.head.getNext()

	def fin(self):
		return self.head.getPrevious()

	def search(self, item):
		current = self.head.getNext()
		while current != self.head and current.getData() != item:
			current = current.getNext()
		if current == self.head:
			return None
		else:
			return current

	def remove(self, base):
		base.getPrevious().setNext(base.getNext())
		base.getNext().setPrevious(base.getPrevious())
		self.count = self.count - 1'
```

# Sequence triée
### Slides 13 et 14
```python
class SeqTriee:
	def __init__(self):
		self.liste = ListeCircBidir()

	def getFirst(self):
		return self.liste.tete()

	def getLast(self):
		return self.liste.fin()

	def length(self):
		return self.liste.length()

	def isEmpty(self):
		return self.liste.isEmpty()

	def insert(self, item):
		if self.isEmpty():
			self.liste.add(item)
		else:
			current = self.liste.tete()
			fin = current == self.liste.fin()
			while current.getData() < item and not fin:
				current = current.getNext()
				fin = current == self.liste.fin()
			if current.getData() < item:
				self.liste.addAfter(current, item)
			else:
				self.liste.addAfter(current.getPrevious(), item)

	def remove(self, base):
		self.liste.remove(base)

	def search(self, item):
		return self.liste.search(item)
```
# Binary Search Tree
### Slide 56 à 62
## BST
```python
class BinarySearchTree:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None
        self.parent = None

    def getRootVal(self):
        return self.data

    def setRootVal(self, value):
        self.data = value

    def getGlobalRoot(self):
        curr = self
        while curr.parent is not None:
            curr = curr.parent
        return curr

    def getNext(self):
        if self.right is not None:
            curr = self.right
            while curr.left is not None:
                curr = curr.left
        else:
            child = self
            curr = self.parent
            while curr is not None and curr.right == child:
                child = curr
                curr = curr.parent
        return curr

    def getPrevious(self):
        if self.left is not None:
            curr = self.left
            while curr.right is not None:
                curr = curr.right
        else:
            child = self
            curr = self.parent
            while curr is not None and curr.left == child:
                child = curr
                curr = curr.parent
        return curr

    def getFirst(self):
        curr = self.get_global_root()
        while curr.left is not None:
            curr = curr.left
        return curr

    def getLast(self):
        curr = self.get_global_root()
        while curr.right is not None:
            curr = curr.right
        return curr

    def find(self, item):
        curr = self.get_global_root()
        while curr is not None and curr.data != item:
            if item < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def insert(self, item):
        curr = self.get_global_root()
        parent = None
        while curr is not None:
            parent = curr
            if item < curr.data:
                if curr.left is None:
                    break
				curr = curr.left
            else:
                if curr.right is None:
                    break
				curr = curr.right
        new_node = BinarySearchTree(item)
        new_node.parent = parent
        if item < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def remove(self):
        if self.left is not None:
            predecessor = self.get_previous()
            self.data = predecessor.data
            predecessor.remove()
        elif self.right is not None:
            successor = self.get_next()
            self.data = successor.data
            successor.remove()
        else:
            if self.parent is not None:
                if self.parent.left == self:
                    self.parent.left = None
                else:
	                self.parent.right = None
            else:
	            self.data = None
                self.left = None
                self.right = None
