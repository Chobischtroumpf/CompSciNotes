---
title: Chap 05 - slides_arbres.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Arbre binaire via listes Python
### Slide 39
```python
def BinaryTree(r):
    return [r, [], []]

def modifyLeft(root,value):
	t = root.pop(1)
	root.insert(1,[value,[],[]])
	return root

def modifyRight(root,value):
	t = root.pop(2)
	root.insert(2,[value,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]
```
# Arbre binaire
### Slide 42
```python
class BinaryTree:
	def __init__(self,item):
		self.info = item
		self.left = None
		self.right = None

	def modifyLeft(self,item):
		self.left = BinaryTree(item)

	def modifyRight(self,item):
		self.right = BinaryTree(item)

	def getRootVal(self):
		return self.info

	def setRootVal(self,item):
		self.info = item

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right
```
# Nœud d'un arbre binaire non récursif
### Slide 49
```python
class Node:
	def __init__(self,item):
		self.info = item
		self.left = None
		self.right = None

	def getInfo(self):
		return self.info

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setInfo(self,newinfo):
		self.info = newinfo

	def setLeft(self,newleft):
		self.left = newleft

	def setRight(self,newright):
		self.right = newright
```
# Arbre binaire non récursif via nœuds
### Slide 51
```python
class BinaryTree:
	def __init__(self,item):
		self.root = Node(item)

	def getRoot(self):
		return self.root

	def modifyLeft(self,base,item):
		base.setLeft(Node(item))

	def modifyRight(self,base,item):
		base.setRight(Node(item))
```
# Parcours préfixé d’arbres récursifs
### Slide 57
```python
def preorder(tree):
	if tree != None:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	while tree != None:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		tree = tree.getRightChild()
```
# Parcours infixé d’arbres récursifs
### Slide 58
```python
def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def inorder(tree):
	while tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		tree = tree.getRightChild()
```
# Parcours suffixé d’arbres récursifs
### Slide 59
```python
def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())
```
# Parcours par niveau d’arbres récursifs
### Slide 60
```python
def niveau(tree):
	f = Queue()
	f.insert(tree)
	while not f.isEmpty():
		n = f.remove()
		if n != None:
			print(n.getRootVal())
			f.insert(n.getLeftChild())
			f.insert(n.getRightChild())
```
# Parcours préfixé d’arbres non récursifs
### Slide 61
```python
def preorder(noeud):
	while noeud != None:
		print(noeud.getInfo())
		preorder(noeud.getLeft())
		noeud = noeud.getRight()
```
# Parcours infixé d’arbres non récursifs
### Slide 62
```python
def inorder(noeud):
	while noeud != None:
		inorder(noeud.getLeft())
		print(noeud.getInfo())
		noeud = noeud.getRight()
```
# Parcours suffixé d’arbres non récursifs
### Slide 63
```python
def postorder(noeud):
	if noeud != None:
		postorder(noeud.getLeft())
		postorder(noeud.getRight())
		print(noeud.getInfo())
```
# Parcours par niveau d’arbres non récursifs
### Slide 64
```python
def niveau(noeud):
	f = Queue()
	f.insert(noeud)
	while not f.isEmpty():
		n = f.remove()
		if n != None:
			print(n.getInfo())
			f.insert(n.getLeft())
			f.insert(n.getRight())
```
# Forêt ou arbre m-aire
### Slides 70 et 71
```python
class Foret:
	def __init__(self, item):
		self.info = item
		self.child = None
		self.brother = None

	def getRootVal(self):
		return self.info

	def setRootVal(self, item):
		self.info = item

	def getChild(self):
		return self.child

	def getBrother(self):
		return self.brother

	def modifyChild(self, newNode):
		self.child = Foret(newNode)

	def modifyBrother(self, newNode):
		self.brother = Foret(newNode)
```
# Parcours en preordre d'une foret / arbre m-aire
### Slide 72
```python
def preorder(forest):
	while forest != None:
		print(forest.getRootVal())
		preorder(forest.getChild())
		forest = forest.getBrother()
```
# Parcours en postordre d'une foret / arbre m-aire
### Slide 73
```python
def postorder(forest):
	while forest != None:
		postorder(forest.getChild())
		print(forest.getRootVal())
		forest = forest.getBrother()
```
# Parcours par niveau d'une foret / arbre m-aire
### Slide 74
```python
def niveau(forest):
	f = Queue()
	f.insert(forest)
	while not f.isEmpty():
		n = f.remove()
		while n != None:
			print(n.getRootVal())
			f.insert(n.getChild())
			n = n.getBrother()
```
