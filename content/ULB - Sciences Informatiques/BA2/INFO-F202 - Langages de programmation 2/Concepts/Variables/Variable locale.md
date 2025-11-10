---
title: Variable locale
authors: Alessandro Dorigo
tags:
  - LDP2
  - Progra
---


Les variables locales normales commencent leur vie à leur déclaration et nissent leur vie à la fin de leur bloc.

Les paramètres de fonction/méthode utilisant le passage par valeur commencent leur vie à l'appel de la fonction via une copie et se terminent lorsque la fonction/méthode revient

Avec la récursivité, il peut y avoir plusieurs instances associées à une seule variable

## Exemple
```cpp
void doubleString(C x) {
	cout << "start doubleString" << endl;
	C y{x.st+x.st};
	cout << "end doubleString" << endl;
}

void demoLocal() {
	cout << "start demoLocal" << endl;
	C lv1{"lv1"};

	for (int i=0; i<5; i++) {
		C lv2{"lv2"};
	}

	cout << "loopover" << endl;
	doubleString(lv1);
	cout << "end demoLocal" << endl;
}

int main() {
	cout << "start Main" << endl;
	demoLocal();
	cout << "end Main" << endl;
}
```
