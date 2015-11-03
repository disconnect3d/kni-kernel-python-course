## Zadania domowe do spotkania nr 2

1. Napisz funkcję, która policzy sumę elementów w podanej liście.

2. Napisz funkcję, która policzy iloczyn elementów w podanej liście.

3. Zaimplementuj grę w wisielca bazując na poniższym kodzie (zmień miejsca zawierające komentarze TODO / FIXME).
```
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
    pass

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
```python

* rozszerz grę tak, żeby wielkość liter podanych przez użytkownika nie miała znaczenia (hint: metoda `lower()` na stringu)

* rozszerz grę tak, żeby gracz nie tracił życia, jeśli poda tę samą literę kolejny raz

* dodaj walidację wejścia - jeśli użytkownik poda więcej niż jeden znak, wypisz komunikat o błędzie i poproś jeszcze raz o podanie litery (hint: funkcja wbudowana `len(...)`)

4. Zaimplementuj [szyfr cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara).
