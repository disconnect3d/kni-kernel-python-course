## Zadania domowe do spotkania nr 2

1. Napisz funkcję, która policzy sumę elementów w podanej liście.

2. Napisz funkcję, która policzy iloczyn elementów w podanej liście.

3. Zaimplementuj grę w wisielca bazując na poniższym kodzie (zmień miejsca zawierające komentarze TODO / FIXME).
```python
max_guesses = 9
lives = max_guesses
secret_word = 'pythoniczny kod'
displayed_word = ['_'] * len(secret_word)


def welcome():
    print("Witaj w grze wisielec. Masz {} zyc.".format(lives))

def get_letter():
    # TODO / FIXME: return letter taken as input from the user

def bad_guess():
    # TODO / FIXME: inform user that he failed his guess and take one of his lives
    # hint: use `global` Python keyword

def print_word():
    msg = "Slowo ktore zgadujesz: {} ({} znakow)"
    word = ''.join(displayed_word)
    print(msg.format(word, len(displayed_word)))

def unhide_letter(letter):
    # TODO / FIXME: unhide all occurences of `letter` from `secret_word` in `displayed_word`
    # hint: use buildin function `enumerate` in a for loop, e.g. `for index, element in enumerate(['a', 'b', 'c']):`

def play():
    unhide_letter(' ')
    welcome()

    while lives and ''.join(displayed_word) != secret_word:
        print_word()
        letter = get_letter()

        if letter not in secret_word:
            bad_guess()
        else:
            unhide_letter(letter)

    # skoro lives != 0, to znaczy ze gracz wygral
    if lives:
        print("Wygrales! Slowo to: {}".format(secret_word))
        print("Udalo ci sie tego dokonac w {} probach!".format(max_guesses-lives))
    else:
        print("Przegrales! Szukane slowo to: {}".format(secret_word))


play()
```

Przykładowy "gameplay":
```
python3 hangman.py 
Witaj w grze wisielec. Masz 9 zyc.
Slowo ktore zgadujesz: ___________ ___ (15 znakow)
Podaj literke: p
Slowo ktore zgadujesz: p__________ ___ (15 znakow)
Podaj literke: y
Slowo ktore zgadujesz: py________y ___ (15 znakow)
Podaj literke: a
Podales zla literke! Zostalo ci 8 zyc.
Slowo ktore zgadujesz: py________y ___ (15 znakow)
Podaj literke: p
Slowo ktore zgadujesz: py________y ___ (15 znakow)
Podaj literke: a
Podales zla literke! Zostalo ci 7 zyc.
Slowo ktore zgadujesz: py________y ___ (15 znakow)
Podaj literke: t
Slowo ktore zgadujesz: pyt_______y ___ (15 znakow)
Podaj literke: h
Slowo ktore zgadujesz: pyth______y ___ (15 znakow)
Podaj literke: o
Slowo ktore zgadujesz: pytho_____y _o_ (15 znakow)
Podaj literke: n
Slowo ktore zgadujesz: python___ny _o_ (15 znakow)
Podaj literke: k
Slowo ktore zgadujesz: python___ny ko_ (15 znakow)
Podaj literke: d
Slowo ktore zgadujesz: python___ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: c
Slowo ktore zgadujesz: python_c_ny kod (15 znakow)
Podaj literke: z
Slowo ktore zgadujesz: python_czny kod (15 znakow)
Podaj literke: i
Wygrales! Slowo to: pythoniczny kod
Udalo ci sie tego dokonac w 2 probach!
```

* rozszerz grę tak, żeby wielkość liter podanych przez użytkownika nie miała znaczenia (hint: metoda `lower()` na stringu)

* rozszerz grę tak, żeby gracz nie tracił życia, jeśli poda tę samą literę kolejny raz

* dodaj walidację wejścia - jeśli użytkownik poda więcej niż jeden znak, wypisz komunikat o błędzie i poproś jeszcze raz o podanie litery (hint: funkcja wbudowana `len(...)`)

4. Zaimplementuj [szyfr cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara).
