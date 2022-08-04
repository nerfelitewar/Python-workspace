#guess correct number under 5 chance and make it y/n too 

import random

def MainGame():
    print('Guess random number between 1-100')
    print('You have 5 chance to guess. Good Luck!')
    Num=random.randint(1,100)
    for i in range(0,5):
        User=input('Enter your guessed number-')
        if User==Num:
            print('Correct')
        else:
            print('Wrong')
        pass 
    print('Correct answer-',Num)

    Again=input('Want to play again Yes(Y)/No(N)-')
    if Again=='y'or'Y'or'Yes'or'yes':
        MainGame()
    else:
        print('**Thank you for playing!\nGoodbye! :)')
        exit()




