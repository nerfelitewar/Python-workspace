#making very basic calculator
#with functions like- 
'''Addition, Sub, multiply, divison , power, root, trignometric, logratimic, matrix, determinatant, etc'''
from time import sleep
#from tkinter import* #try making it work in GUI
Number1=int(input('Enter first number-'))
sleep(1)
Number2=int(input('Enter second number-'))

def AddNum(Number1,Number2):
    AddedNum=eval(Number1+Number2)
    return AddedNum

def SubNum(Number1,Number2):
    SubNum=eval(Number1-Number2)
    return SubNum

def MultiplyNum(Number1,Number2):
    MultiplyNum=eval(Number1*Number2)
    return MultiplyNum

def DivNum(Number1,Number2):
    DivNum=eval(Number1/Number2)
    return DivNum

Operators=print(
    '1. Addition\n'
    '2. Subtraction\n'
    '3. Multiplication\n'
    '4. Division\n'
    '5. Quit\n'
)

   


