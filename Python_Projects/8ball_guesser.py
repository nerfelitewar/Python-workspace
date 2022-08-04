import random 
import time
print('''  ______   ___.          .__  .__      ________                                          
 /  __  \  \_ |__ _____  |  | |  |    /  _____/ __ __   ____   ______ ______ ___________ 
 >      <   | __ \\__  \ |  | |  |   /   \  ___|  |  \_/ __ \ /  ___//  ___// __ \_  __ \
/   --   \  | \_\ \/ __ \|  |_|  |__ \    \_\  \  |  /\  ___/ \___ \ \___ \\  ___/|  | \/
\______  /  |___  (____  /____/____/  \______  /____/  \___  >____  >____  >\___  >__|   
       \/       \/     \/                    \/            \/     \/     \/     \/       ''')

AnsList = ['Yes', 'No', 'Never', 'Why should I tell you.', 'You Decide', 'I wont tell', 'lmao', 'No way', 'Cry all you got', 'That is funny',
           'Nevermind! Iam just a bot', 'Sorry.', 'UwU', 'Why u wanna know?!', 'I cant tell man!', 'Wait! what!?', 'Umm...i guess we never know!']

print('Hi,')
time.sleep(1)
print('Welcome to play this game!')
time.sleep(1)
print('Playing this is very easy, just ask questions and it will answer. lol')
time.sleep(3)


def function():
    input('Question : ')
    print(f'Answer: {random.choice(AnsList)}')

    playAgain = input('Want to play again? y/n: ')

    if playAgain == 'y':
        function()
    elif playAgain=='Y':
        function()
    else:  #else not working why?? WHYY :(
        print('Bye👋 ')
        exit()        


function()