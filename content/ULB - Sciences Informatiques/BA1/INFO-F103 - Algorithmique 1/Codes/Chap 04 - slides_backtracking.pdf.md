---
title: Chap 04 - slides_backtracking.pdf
authors: Alessandro Dorigo
tags:
  -
---

# L’énumération de tous les mots de cinq lettres
### Slide 8
```python
def mots():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word_length = 5
    word = [' '] * word_length

    for letter1 in alphabet:
        word[0] = letter1
        for letter2 in alphabet:
            word[1] = letter2
            for letter3 in alphabet:
                word[2] = letter3
                for letter4 in alphabet:
                    word[3] = letter4
                    for letter5 in alphabet:
                        word[4] = letter5
                        print(''.join(word))

```
# Mots booléens
### Slide 13
```python
class MotsBool:
    def __init__(self, size):
        self.size = size
        self.word = [False] * self.size
        self.generate_words(0)

    def generationMots(self, index):
        if index == self.size:
            print(self.word)
        else:
            self.word[index] = True
            self.generate_words(index + 1)
            self.word[index] = False
            self.generate_words(index + 1)
```
# Mots alphabétiques
### Slide 18
```python
class Mots:
    def __init__(self, size):
        self.size = size
        self.word = [' '] * self.size
        self.generate_words(0)

    def affiche(self):
        print(''.join(self.word))

    def generationMots(self, index):
        if index == self.size:
            self.display()
        else:
            for char in "abcdefghijklmnopqrstuvwxyz":
                self.word[index] = char
                self.generate_words(index + 1)
```
