<img src="http://testhuddle.com/wp-content/uploads/2014/05/python-programming.jpg" height="400px"/>

<h1 align="center">Warsztat 1 <a href="../lab2/lab2.md"> >> </a></h1>

Prezentacje z zajęć można znaleźć <a href="pdfs/intro.pdf">tutaj</a>.

Instalacja Pythona pod [Windows](https://www.python.org/downloads/ "Python downloads"), dla Debiana/Ubuntu `sudo apt-get install python3`

## Typy:
- `int` - liczba całkowita
- `float` - liczba zmiennoprzecinkowa, typ ten pozwala reprezentować duży zakres, ale z ograniczoną dokładnością
- `string` - łańcuch znaków, napis
- `bool` - typ logiczny może przyjmować wartości `True` lub `False`
- `None` - specjalna stała oznaczająca brak wartości (jak `null` w C/C++, Java, lub `nil` w niektórych językach)
```python
calkowita = 7
rzeczywista = 7.5
rzeczywista = float(38)
napis = 'witaj'
napis = "witaj"
napis = "Nie martw sie o 'pojedyncze' cudzyslowy."
logiczne = True
logiczne = False
```
### Rzutowanie
W pythonie nie można zrobić `print("abc" + 5)` ponieważ obiekty nie są tego samego typu. Dlatego też operator dodawania nie ma sensu. Musimy powiedzieć jawnie, że chcemy traktować `5` jako `string`. W tym celu używamy rzutowania `print("abc" + str(5))`.

Inny przykład: `print(int("10") + 5)`, wypisze 15.

## Komentarze
Interpreter ignoruje to co znajduje się w komentarzach.
Komentarz liniowy rozpoczyna się od znaku `#`.
```python
a = "To jest kod"
# A to komentarz
```
Komentarz blokowy rozpoczynamy i kończymy `"""`
```python
"""
to
jest
komentarz
"""
```
## Funkcje
Funkcje pozwalają zamknąć i nazwać blok kodu. Umożliwia to łatwe odwoływanie się do niego i oszczędza powtórzeń.
```python
def square(x):
    return x*x 
```
Wywołanie `square(5)` zwróci 25.

Dobre nawyki: Funkcje powinny mieć jedną odpowiedzialność, robić jedną rzecz, robić ją dobrze i obsługiwać wszystkie przypadki (w miarę możliwości). Funkcje pozwalają też nazwać kawałek kodu, nazwa powinna być odczasownikowa i opisywać to co funkcja robi. Złe nazwy: `x85`, `abc`, `qwerty`. Dobre nazwy: `cutFirstElement`, `removeEverything`, `ReadPropertiesFromFile`.
#Instrukcje sterujące
###Pętle
`for` służy do iterowania po kolekcji, jako kolekcję rozumiemy **Listy**, **Krotki**, **Słowniki**, **Generatory** (O tym później).

Wbudowana funkcja `range` zwraca kolekcję zawierającą kolejne liczby.

```python
for i in range(5):
    print(i)
```
Wypisze  0, 1, 2, 3, 4

`range` może przyjmować 1, 2 lub 3 argumety, patrz [Dokumentacja](https://docs.python.org/3/library/functions.html#func-range).

```python
for i in range(10, 25, 5):
    print(i)
```
Wypisze 10, 15, 20. Możemy też podać listę z wartościami.

```python
for i in [10, 25, 5]:
    print(i)
```

`while` to pętla, która wykonuje się dopóki warunek jest prawdziwy.

```python
i=5
while i>0:
    print(i)
    i -= 1
```
Wypisze 5, 4, 3, 2, 1
### Instrukcje warunkowe
Jeśli musimy zdecydować co ma się wykonać na podstawie jakiegoś warunku używamy instrukcji `if`.
```python
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("Są równe")
```
Jest też wersja inline, wartość zmiennej `a` będzie zależeć od warunku `condition`.
```python
a = 5 if condition else 6
```

# Zadania

1. Napisz funkcję która liczy [BMI](https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a) dla podanej masy ciała.
2. Funkcja która przymuje `n` i wypisze liczby od 1 do `n`, ale zamiast liczb podzielnych przez 3 pisze "Fizz" zamiast liczb podzielnych przez 5 pisze "Buzz" dla liczb podzielnych prez 3 i 5 pisze "FizzBuzz"(Jest to oklepane i  typowe zadanie pojawiające się na rozmowach kwalifikacyjnych) np.
```
1
2
Fizz
4
Buzz
Fizz
7
8
```

[(skąd się wzieło)](https://en.wikipedia.org/wiki/Fizz_buzz)

# See Also
- [learnpython.org](http://www.learnpython.org/pl/Welcome "learnpython.org")
- [Zanurkuj w Pythonie](https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie "Zanurkuj w Pythonie")
- [practicepython.org](http://www.practicepython.org/)

