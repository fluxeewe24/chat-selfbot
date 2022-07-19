def start():
    import os
    import time
    from colorama import Fore, Back, Style
    os.system('cls')
    os.system("title slu to kox")

    print(Fore.GREEN + "Za 2 sekundy zostanie włączony selfbot (timming pisania to 5 minut)")
    time.sleep(2)
    

start()



def farm():
    import os
    import time
    import random
    from pynput.keyboard import Key, Controller
    from colorama import Fore, Back, Style 
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    slowa = random.choice(open('slowa.txt', 'r').readlines()).strip()
    keyboard1 = Controller()


    for char in slowa:
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.1)
    keyboard1.press(Key.enter)
    if keyboard1.pressed():
        print(Fore.BLUE + "[" + current_time + "]", Style.RESET_ALL + slowa)

    #na dole masz czas zjebie
    time.sleep(60)
    farm()

farm()
