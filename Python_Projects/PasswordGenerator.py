#random password generator of a length specified by the user
import random
L='1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*()_?/.+--=;:'
List=list(L)
UserInput=int(input('Enter the length of the password you want-'))
if UserInput!=0 and UserInput<0:
    pass 
else:
    print("Error kindly enter a valid password length")

for i in range(UserInput):



    RPass=random.choice(List)
    print(RPass,end='')


 






