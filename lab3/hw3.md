## Zadania domowe do spotkania nr 3

0. Jeśli nie zrobiliśmy zadań z warsztatu 2, to wracamy je zrobić ;p.

1. Problem odpalania funkcji z skryptu, gdy jest on importowany.

  Skrypty Pythona mają kilka 'magicznych' zmiennych, które czasem są pomocne.
  
  Jedną z takich zmiennych jest zmienna `__name__`, która w momencie gdy włączymy skrypt bezpośrednio (np. `python3 skrypt.py`) ma wartość `__main__`.

  W przypadku gdy dany skrypt jest importowany z innego, wartość tej zmiennej jest inna - sam sprawdź jaka.

  * napisz skrypt `main.py`, który zaimportuje funkcję `play` z gry wisielca z poprzedniego warsztatu - następnie zrób tak, żeby skrypt wisielca wywoływał funkcję `play` tylko wtedy, gdy jest włączany bezpośrednio ([przykład](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts))

3. Napisz grę w kółko i krzyżyk dla dwóch graczy

  * planszą powinna być lista list (np. `board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]`)
  * w kodzie powinny znaleźć się takie funkcje jak:

    * `draw_board` - która rysuje planszę "przyjazną dla oka"
    * `game_loop` - w której będzie główna pętla gry
    * funkcja sprawdzająca, czy któryś z graczy wygrał grę

  * dodatkowo: napisz drugą wersję gry, w której jednym z graczy jest komputer wykonujący losowy ruch (należy wykorzystać funkcję z modułu `random`)

  Ważna uwaga: uczymy się pisać kod po angielsku, który będzie łatwy do zrozumienia dla postronnych.

