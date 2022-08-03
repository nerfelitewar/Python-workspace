#gives a random number form 1 to 100
import random
import time

input("Enter to see your lucky number!!!")

Num=random.randint(0,100)
l=print('Loading [#######        10% ]')
time.sleep(.3)
l2=print('Loading [###########        30%]')
time.sleep(.5)
l3=print('Loading [#################       50%]')
time.sleep(1)
l4=print('Loading [#########################     90%]')
time.sleep(2)
l5=print('Loading [############################# 100%]')
time.sleep(1)
print('Your Lucky Number is 🌟',Num)




    


