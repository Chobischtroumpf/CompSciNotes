---
title: Janvier 2024
authors: Alessandro Dorigo
tags:
  - LDP2
  - Exam
---


### 1)
Écrivez la classe `Compte` pour qu'elle fonctionne comme dans l'exemple suivant. *Ne vous inquiétez pas d'imprimer parfaitement la sortie dans des colonnes comme dans cet exemple.*
```cpp
Compte A;
A.depot("Salaire",1000);
A.retrait("Snack",7);
A.depot("Salaire",1000);
A.retrait("Loyer",850);
A.imprimerDernieresTransactions(4);
```

```cpp
Salaire      1000    1000
Snack          -7     993
Salaire      1000    1993
Loyer        -850    1143
```

```cpp
A.depot("Hertiage",1000000);
A.retrait("Maison",750000);
A.imprimerDernieresTransactions(3);
```

```cpp
Loyer        -850    1143
Hertiage  1000000 1001143
Maison    -750000  251143
```
#### Réponse
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

class Compte {
private:
    struct Transaction {
        std::string description;
        int amount;
        int balance;
    };

    std::vector<Transaction> transactions;
    int current_balance = 0;

public:
    void depot(const std::string& description, int amount) {
        current_balance += amount;
        transactions.push_back({description, amount, current_balance});
    }

    void retrait(const std::string& description, int amount) {
        current_balance -= amount;
        transactions.push_back({description, -amount, current_balance});
    }

    void imprimerDernieresTransactions(int n) const {
        int start = transactions.size() > n ? transactions.size() - n : 0;
        for (size_t i = start; i < transactions.size(); ++i) {
            std::cout << i + 1 << " "
                      << transactions[i].description << " "
                      << transactions[i].amount << " "
                      << transactions[i].balance << "\n";
        }
    }
};
```
### 2) (a)
Écrivez une fonction `selectionner` qui fonctionne comme suit
```cpp
vector<int> A={11,24,32,41,25,16,7,48};
auto B=selectionner(A,[](int x){return x%2==0;});
for (auto x:B) cout<<x<<" ";
cout<<endl;
```

```cpp
24 32 16 48
```

```cpp
vector<string> C={"bonjour","le","les","cinq","nenuphar"};
auto D=selectionner(C,[](string x){return x.size()<5;});
for (auto x:D) cout<<x<<" ";
```

```cpp
le les cinq
```
#### Réponse
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>

template <typename T, typename Predicate>
std::vector<T> selectionner(const std::vector<T>& input, Predicate predicate) {
    std::vector<T> result;
    for (const auto& element : input) {
        if (predicate(element)) {
            result.push_back(element);
        }
    }
    return result;
}
```
### 2) (b)
Considérez le code suivant. Définissez `F` pour qu'il fonctionne exactement de la même manière que dans les lignes 1 à 4 dans (a).
```cpp
F f;
vector<int> A={11,24,32,41,25,16,7,48};
auto B=selectionner(A,f);
for (auto x:B) cout<<x<<" ";
cout<<endl;
```
#### Réponse
```cpp
#include <iostream>
#include <vector>
#include <functional>

struct F {
    bool operator()(int x) const {
        return x % 2 == 0;
    }
};

template <typename T, typename Predicate>
std::vector<T> selectionner(const std::vector<T>& input, Predicate predicate) {
    std::vector<T> result;
    for (const auto& element : input) {
        if (predicate(element)) {
            result.push_back(element);
        }
    }
    return result;
}
```
### 3)
Définissez deux classes, `Seul` et `Paire`, et une fonction, `sommes`, qui fonctionnent comme dans l'exemple suivant :
```cpp
vector <Seul *> A;
A.push_back(new Seul(4));
A.push_back(new Seul(7));
A.push_back(new Paire(7,4));
A.push_back(new Seul(3));
A.push_back(new Seul(2));
A.push_back(new Paire(7,1));
A.push_back(new Paire(7,6));
A.push_back(new Paire(3,3));
for (auto p:A){
	string s{*p};
	cout<<"("<<s<<") ";
}

(*A[1])[0]=98;
(*A[5])[1]=99;
cout<<endl;
for (auto p:A){
	string s{*p};
	cout<<"("<<s<<") ";
}
cout<<endl;

auto B=sommes(A);
for (auto x:B){
	cout<<x<<" ";
}
```

```cpp
(4) (7) (7 4) (3) (2) (7 1) (7 6) (3 3)
(4) (98) (7 4) (3) (2) (7 99) (7 6) (3 3)
4 98 11 3 2 106 13 6
```
#### Réponse
```cpp
#include <iostream>
#include <vector>
#include <string>

class Seul {
protected:
    int value;

public:
    Seul(int val) : value(val) {}

    virtual int& operator[](size_t index) {
        if (index != 0) throw std::out_of_range("Index out of range for Seul");
        return value;
    }

    virtual std::string toString() const {
        return std::to_string(value);
    }

    virtual int somme() const {
        return value;
    }

    virtual ~Seul() = default;
};

class Paire : public Seul {
    int second;

public:
    Paire(int first, int second) : Seul(first), second(second) {}

    int& operator[](size_t index) override {
        if (index == 0) return value;
        if (index == 1) return second;
        throw std::out_of_range("Index out of range for Paire");
    }

    std::string toString() const override {
        return std::to_string(value) + " " + std::to_string(second);
    }

    int somme() const override {
        return value + second;
    }
};

std::vector<int> sommes(const std::vector<Seul*>& vec) {
    std::vector<int> result;
    for (const auto& obj : vec) {
        result.push_back(obj->somme());
    }
    return result;
}
```
### 4)
Cette question concerne l'arithmétique modulaire, c'est-à-dire les mathématiques effectuées modulo un entier positif $n$. Pour rappel, le modulo $x \mod n$ en mathématiques (`x%n` en C++) est le reste de la division euclidienne de $x$ par $n$. Étant donné $n$ et $x$, considérons la valeur de $xi \mod n$, où $i$ varie de $0$ à $n - 1$. Par exemple, quand $n = 7$ et $x = 5$:
$$5 \cdot 0 \mod 7 = 0$$
$$5 \cdot 1 \mod 7 = 5$$
$$5 \cdot 2 \mod 7 = 3$$
$$5 \cdot 3 \mod 7 = 1$$
$$5 \cdot 4 \mod 7 = 6$$
$$5 \cdot 5 \mod 7 = 4$$
$$5 \cdot 6 \mod 7 = 2$$
Votre tâche est d'écrire le code de `Modular` pour que, étant donné $n$ et $x$, il produise tous les
$xi \mod n$ pour $i$ entre $0$ et $n - 1$, comme dans le code suivant:

```cpp
void DemoModular(int n,int x){
	cout<<"n:"<<n<<" x:"<<x<<" :: ";
	for (auto i:Modular(n,x))
		cout<< i <<" ";
		cout<<endl;
}

DemoModular(10,1);
DemoModular(10,2);
DemoModular(10,3);
DemoModular(7,5);
DemoModular(7,6);
```

```cpp
n:10 x:1 :: 0 1 2 3 4 5 6 7 8 9
n:10 x:2 :: 0 2 4 6 8 0 2 4 6 8
n:10 x:3 :: 0 3 6 9 2 5 8 1 4 7
n:7 x:5 :: 0 5 3 1 6 4 2
n:7 x:6 :: 0 6 5 4 3 2 1
```
#### Réponse
```cpp
class Modular {
public:
    Modular(int n, int x) : n(n), x(x) {}

    class Iterator {
    public:
        Iterator(int current, int n, int x) : current(current), n(n), x(x) {}

        Iterator& operator++() {
            current++;
            return *this;
        }

        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }

        int operator*() const {
            return (current * x) % n;
        }

    private:
        int current;
        int n;
        int x;
    };

    Iterator begin() const {
        return Iterator(0, n, x);
    }

    Iterator end() const {
        return Iterator(n, n, x);
    }

private:
    int n;
    int x;
};
```
#### Réponse logique
```cpp
#include <vector>

std::vector<int> Modular(int n, int x) {
    std::vector<int> result;
    for (int i = 0; i < n; i++) {
        result.push_back((x * i) % n);
    }
    return result;
}
```
### 5)
Considérez le code suivant :
```cpp
class Drawable{
	int id;
public:
	Drawable(int id):id{id}{cout<<"Constructing "<<id<<endl;}
	int getID() const {return id;}
	virtual void draw() const {cout<<"Drawing nothing"<<endl;}
};

class Text : public virtual Drawable {
	int x,y;
	string text;
public:
	Text(int id,int x,int y,string text):Drawable{id},x{x},y{y},text{text}{};
	void draw() const {
		cout<<"Drawing Text ID:"<<getID()<<endl;
	}
};

class Circle : public virtual Drawable {
	int x,y,r;
public:
	Circle(int id,int x,int y,int r):Drawable{id},x{x},y{y},r{r}{};
	void draw() const {
		cout<<"Drawing Circle ID:"<<getID()<<endl;
	}
};

class CircleText : public virtual Circle, public virtual Text {
public:
	CircleText(int id,int x,int y,int r,string text):
		Drawable(id),Circle(id,x,y,r),Text(id,x,y,text){}
	void draw() const {Circle::draw();Text::draw();}
};
```
### 5) (a)
Que produit le code de démonstration suivant ?
```cpp
Drawable *d=new CircleText{10,26,32,44,"Chose"};
d->draw();
```
#### Réponse
```cpp
Constructing 10
Drawing Circle ID:10
Drawing Text ID:10
```
### 5) (b)
Si la fonction `draw` n'est plus virtuelle :
- Il compile et le code de démonstration donne la même sortie
- Il compile et le code de démonstration donne une sortie différente. Veuillez écrire la nouvelle sortie.
- Il ne compile pas. Expliquez pourquoi.
#### Réponse
- Il compile et le code de démonstration donne une sortie différente. Veuillez écrire la nouvelle sortie.
```cpp
Constructing 10
Drawing nothing
```
### 5) (c)
Considérez le code suivant. Les modifications par rapport au code précédent sont notées dans
les commentaires :
```cpp
class Drawable{
	int id;
public:
	Drawable(int id):id{id}{cout<<"Constructing "<<id<<endl;}
	int getID() const {return id;}
	void draw() const {cout<<"Drawing nothing"<<endl;} //pas de virtual
};

class Text : public Drawable { //pas de virtual
	int x,y;
	string text;
public:
	Text(int id,int x,int y,string text):Drawable{id},x{x},y{y},text{text}{};
	void draw() const {
		cout<<"Drawing Text ID:"<<getID()<<endl;
	}
};

class Circle : public Drawable { //pas de virtual
	int x,y,r;
public:
	Circle(int id,int x,int y,int r):Drawable{id},x{x},y{y},r{r}{};
	void draw() const {
		cout<<"Drawing Circle ID:"<<getID()<<endl;
	}
};

class CircleText : public Circle, public Text { //pas de virtual
public:
	CircleText(int id,int x,int y,int r,string text):
	Circle(id,x,y,r),Text(id,x,y,text){} // Aucun appel à Drawable
	void draw() const {Circle::draw();Text::draw();}
};
```

Considérez ce code :
```cpp
CircleText *d=new CircleText{10,26,32,44,"Chose"}; // CircleText, pas Drawable!
d->draw();
```

- Il compile et le code de démonstration donne la même sortie que (a)
- Il compile et le code de démonstration donne une sortie différente. Veuillez écrire la nouvelle sortie.
- Il ne compile pas. Expliquez pourquoi.
#### Réponse
- Il compile et le code de démonstration donne une sortie différente. Veuillez écrire la nouvelle sortie.
```cpp
Constructing 10
Constructing 10
Drawing Circle ID:10
Drawing Text ID:10
```
