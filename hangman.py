def game():
    progress = True
    word = ['фонарик'] #Привет это Гоша.Сегодня четверг девятого ноября 2023 16:44.Ну ок 16.11.2023
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(template)

    while progress:
        user_guess = input("введите букву ")
        template = build_template(template, word_in_play, user_guess)
        progress = check_win(template)

        if not check_mistake(word_in_play, user_guess):
            lifes = lifes - 1
            print(f'Осталось {lifes} попытки')
        if lifes == 0:
            print('Поражение!' )
            break
        if not progress:
            print('Вы победили!')

def build_template(t, w, g=''):
    t = list(t)
    for I in range(len(w)):
        if w[I] == g:
            t[I] = g

    print (t) 
    return t

def welcome_speech(t):
    print(f'''Загаданное слово состоит из {len(t) } букв {t}''')

def start_template(w):
    return len(w) * '_'

def get_word(w):
    return w[0]

def check_win(t):
    if '_' in t:
        return True
    else: 
        return False
    
def check_mistake(w, g):
    if g in w:
        return True
    else:
        return False

game()
#ghbdtn это гоша сегодня 16 11 23                    16 34время.Ну ок 23.11.2023 15:46
#ctqxfc 23 11 dhtvz 16:41.Ну ок 07.12.2023 15:46
# сейчас 16:39     07.12. я исправил твои 3 ошибки!
