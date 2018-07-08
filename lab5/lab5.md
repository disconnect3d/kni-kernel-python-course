<h1 align="center"><a href="../lab3/lab3.md"> << </a>Warsztat 5</h1>

Na zajęciach rozwiązywaliśmy jedno z zadań typu crackme/hackme ze strony www.pwnable.kr (większość zadań stamtąd wymaga wiedzy z C/różnych niskopoziomowych rzeczy).

Zadanie polega na rozwiązaniu zagadki serwowanej nam przez serwer znajdujący się na pwnable.kr:9007.

Z takim serwerem możemy połączyć się na systemie linux przez program netcat (`nc` w konsoli):

```bash
nc pwnable.kr 9007
```

Ciekawostka: programem netcat możemy także stawiać serwer, czy tez przesłać pojedynczy plik, np:

```bash
# w jednej konsoli stawiamy serwer na porcie 4444
# zeby dowiedziec sie wiecej o flagach nc: man nc
nc -l -p 4444


# w innej konsoli laczymy sie z serwerem
# jako ze serwer postawilismy sami dla siebie mozemy polaczyc sie z 'localhost'
#(jest to alias na 127.0.0.1 - co zreszta mozemy znalezc w pliku `/etc/hosts`)
nc localhost 4444
```


W dużym skrócie - zagadka polega na tym, że mamy X monet oraz Y prób ważenia ich. Wiemy, że moneta waży 10 jednostek, ale jedna z nich jest oszukana i waży 9. Musimy znaleźć indeks tej oszukanej (jeśli monet mamy 5, to ich indeksy to 0, 1, 2, 3, 4).

Zadanie to należy rozwiązać metodą wyszukiwania binarnego - idea jest bardzo podobna do szukania wartości w tablicy ( https://pl.wikipedia.org/wiki/Wyszukiwanie_binarne ). Tutaj, dzielimy indeksy monet na pół, ważymy monety z lewej oraz z prawej strony, następnie sprawdzamy średnią wagę monety w monetach z lewej oraz z prawej, jeśli średnia jest różna od 10, to znaczy, że w tym przedziale jest wadliwa momneta. Kolejno dzielimy ten obszar na pół i tak dalej, aż znajdziemy wadliwą monetę.

Problemem w rozwiązaniu zagadki ręcznie jest fakt, że czas jest ograniczony, dane wejściowe potrafią być dość duże (np. 713 monet i 10 prób), a zagadkę trzeba rozwiązać 100 razy - stąd trzeba napisać do tego bota.

Zaczęliśmy pisać skrypt takiego bota - `solver.py` (wykorzystuje moduł [`socket`](https://docs.python.org/3/howto/sockets.html)):

```python
#!/usr/bin/env python

import socket

# tworzymy gniazdo sieciowe `s`, którym będziemy mogli wysyłać i odbierać pakiety
# (AF_INET oraz SOCK_STREAM to stałe które są potrzebne, żeby gniazdo wykorzystywało protokół TCP/IP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'pwnable.kr'
port = 9007
s.connect((host, port))

def recv():
    # s.recv zwraca tzw. 'bytes' - string surowych bajtów (znaków)
    # dekodujemy go do zwykłego stringa
    msg = s.recv(2048).decode()
    return msg

def parse_game_start(msg):
    # msg zawiera np. "N=4 C=2\n", wiec obcinamy znak '\n'
    msg = msg[:-1]
    # teraz, dzielimy string na pol w miejscu znaku ' ', dostaniemy ['N=4', 'C=2']
    left, right = msg.split(' ')
    # dzielimy 'N=4' na pol (['N', '4']) i wyciagamy drugi element - '4', a nastepnie zamieniamy go na int
    coins_count = int (left.split('=')[1])
    # to sam co wyzej
    weight_tries = int (right.split('=')[1])
    return coins_count, weight_tries

recv()
coins_count, weight_tries = parse_game_start(recv())
print(coins_count, weight_tries)

coins_indexes = list(range(coins_count))
half_index = coins_count // 2
left_coins = coins_indexes[:half_index]
right_coins = coins_indexes[half_index]
msg = ' '.join(map(str, left_coins))
```

Poza tym, na zajęciach zostały wytłumaczone takie pojęcia jak iterator, generator oraz 'list comprehension' (`[i for i in range(20)]`).

Napisaliśmy też prosty przykład nieskończonego generatora za pomocą funkcji i słowa kluczowego yield.

Przykład:

```python
def gen():
    i = 0
    while True:
        i += 1
        if i%2:
            yield 3
        else:
            yield 5

for i in gen():
    print(i)
```

## Zadanie domowe

Dokończyć skrypt tak, żeby przeszedł zagadkę z pwnable.kr.

UWAGA: Prawdopodobnie gdy skrypt włączymy lokalnie, to z uwagi na czas połączenia z serwerem pwnable.kr nie będzie on w stanie wygrać 100 gier w ciągu 30 sekund. W zadaniu na pwnable.kr jest napisane, żeby ewentualnie włączyć skrypt z serwera (inne zadania wymagają logowanie się na niego przez ssh, więc bawiąc się tam, mamy do niego dostęp).

Jeśli ktoś chce włączyć skrypt z poziomu pwnable.kr, to niech do mnie napisze.

Jeśli będą jakieś problemy/pytania dot. zadania domowego, to piszcie.
