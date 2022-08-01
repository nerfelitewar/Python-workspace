#A basic calculator


import time

def AddNum(X,Y):
    AddedNum=(X+Y)
    return AddedNum

def SubNum(X,Y):
    SubNum=(X-Y)
    return SubNum

def MultiplyNum(X,Y):
    MultiplyNum=(X*Y)
    return MultiplyNum

def DivNum(X,Y):
    DivNum=(X/Y)
    return DivNum

def PowNum(X,Y):
    PowNum=(X**Y)
    return PowNum


X=int(float(input('Enter first number-')))
time.sleep(1)
Y=int(float(input('Enter second number-')))

print(
    '1. Addition\n'
    '2. Subtraction\n'
    '3. Multiplication\n'
    '4. Division\n'
    '5. Power\n'
    '6.My github\n'
    '7.Exit\n'
)

def UserOperation():
    UserOP= int(input('Choose which operation you want to perform-\n'))
    if UserOP==0 or UserOP<0:
        print('***Enter a valid number again***')
        time.sleep(1)
        UserOperation()
    
    else:
        pass 
    if UserOP==1:
        print('Addition of two numbers is-',AddNum(X,Y))
        time.sleep(.5)
        UserOperation()
    if UserOP==2:
        print('Subtraction of two numbers is-',SubNum(X,Y))
        time.sleep(.5)
        UserOperation()
    if UserOP==3:
        print('Multiplication of two numbers is-',MultiplyNum(X,Y))
        time.sleep(.5)
        UserOperation()
    if UserOP==4:
        print('Division of two numbers is-',DivNum(X,Y))
        time.sleep(.5)
        UserOperation()

        
    if UserOP==5:
        print('Power of two numbers is-',PowNum(X,Y))
        time.sleep(.5)
        UserOperation()


    if UserOP==6:
        print('https://www.github.com/nerfelitewar')
        time.sleep(.5)
        UserOperation()


        
    if UserOP==7:
        print('***THANK YOU FOR USING MY CALCULATOR SEE YOU SOON***')    
        exit()

UserOperation()

