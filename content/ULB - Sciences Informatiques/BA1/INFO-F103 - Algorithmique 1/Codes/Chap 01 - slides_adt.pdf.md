---
title: Chap 01 - slides_adt.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Liste chaînée réalisée a l'aide des nœuds:
### slide 10
```Python
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self) :
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext
```
### slide 11
```Python
class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		base.setNext(temp)

	def length(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = None
		current = self.head
		found = False
		while current != None and not found:
			if current is base:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous != None :
				previous.setNext(base.getNext())
			else:
				self.head = base.getNext()
```
# Liste bidirectionnelle réalisée a l'aide des nœuds:
### Slide 24
```Python
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.previous = None # New var

	def getData(self):
		return self.data

	def getNext(self) :
		return self.next

	def getPrevious(self):
		return self.previous

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

	def setPrevious(self, newprevious): # New func
		self.next = newprevious
```
### Slide 26
```Python
class UnorderedList:
	def __init__(self):
		self.head = None
		self.count = 0 # New var

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		if self.head != None: # New cond + logic for count
			self.head.setPrevious(temp)
		self.head = temp
		self.count = self.count + 1

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		temp.setNext(base.getNext())
		if base.getNext() != None: # New cond + logic for count (again)
			base.getNext().setPrevious(temp)
		base.setNext(temp)
		self.count = self. count + 1

	def length(self):
		return self.count # Simplified since count is a class var now

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, base): # Rebuilt using references to 'previous'
		previous = base.getPrevious()
		current = self.head
		if base.getNext() != None:
			base.getNext().setPrevious(previous)
		if previous != None:
			previous.setNext(base.getNext())
		else:
			self.head = base.getNext()
		self.count = self.count − 1
```
# Liste circulaire réalisée a l'aide des nœuds:
*Node class definition is identical to the linked list's Node class*
### Slide 30
```Python
class UnorderedList:
	def __init__(self):
		self.head = Node(-1)
		self.head.setNext(self.head)
		self.count = 0

	def isEmpty(self):
		return self.head.getNext() == self.head

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head.getNext())
		self.head.setNext(temp)
		self.count = self.count + 1

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		base.setNext(temp)
		self.count = self.count + 1

	def length(self):
		return self.count

	def search(self, item):
		current = self.head.getNext()
		found = False
		while current != self.head and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = self.head
		current = self.head.getNext()
		found = False
		while current != self.head and not found:
			if current is base:
				found = True
			else:
				previous = current
				current = current.getNext()
			if found:
				previous.setNext(base.getNext())
				self.count = self.count − 1
```
# Pile (sans Node)
### Slide 40
```Python
class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def top(self):
		return self.items[0]

	def size(self):
		return len(self.items)
```
# Pile (avec Node)
### Slide 42
```Python
class Stack:
	def __init__(self):
		self.head = None
		self.n = 0

	def isEmpty(self):
		return self.head == None

	def top(self):
		return self.head.getData()

	def size (self):
		return self.n

	def push(self, item):
		p = Node(item)
		p.setNext(self.head)
		self.head = p
		self.n += 1

	def pop(self):
		res = self.head.getData()
		self.head = self.head.getNext()
		self.n −= 1
		return res
```
# File (sans Node)
### Slide 58
```Python
class Queue:
	def __init__(self):
		self.items = []

	def head(self):
		return self.items[len(self.items) − 1]

	def isEmpty(self):
		return self.items == []

	def insert(self, item):
		self.items.insert(0, item)

	def remove(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
```
# File (avec Node)
### Slide 59
```Python
class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.n = 0

	def isEmpty(self):
		return self.first == None

	def size(self):
		return self.n

	def head(self):
		return self.first.getData()

	def insert(self, item):
		p = Node(item)
		if self.isEmpty():
			self.first = p
			self.last = p
		else:
			self.last.setNext(p)
			self.last = p
		self.n += 1

	def remove(self):
		res = self.first.getData()
		self.first = self.first.getNext()
		self.n −= 1
		return res
```
