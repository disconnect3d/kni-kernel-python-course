# parametry programu
max_guesses = 9
lives = max_guesses
secret_word = 'pythoniczny kod'
displayed_word = ['_'] * len(secret_word)




def welcome():
    print("Witaj w grze wisielec. Masz {} zyc.".format(lives))

def get_letter():
    return input("Podaj literke: ")[0]

def bad_guess():
    global lives
    lives -= 1
    print("Podales zla literke! Zostalo ci {} zyc.".format(lives))

def print_word():
    msg = "Slowo ktore zgadujesz: {} ({} znakow)"
    word = ''.join(displayed_word)
    print(msg.format(word, len(displayed_word)))

def unhide_letter(letter):
    for index, element in enumerate(secret_word):
        if element == letter:
            displayed_word[index] = letter

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
        print("Udalo ci sie tego dokonac w {} probach!"
              .format(max_guesses-lives))
    else:
        print("Przegrales! Szukane slowo to: {}".format(secret_word))
    

play()

