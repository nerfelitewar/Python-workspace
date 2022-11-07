#enter ur currency type  
    #Enter ur amount in that currency 

# select conversion type 
   #get output 

#ask again and etc.


print('Enter your currency type\n')
print('1.(India)INR\n''2.(USA)USD\n''3.(UAE)AD\n''4.(RUSSIA)ROUBLE\n''5.(JAPAN)YEN\n')

User= int(input('Enter your currency type-'))
if User<=0:
    print('Error pls retry')
elif User==1:
    InrC=int(input('Enter your currency in INR-'))
elif User==2:
    UsdC=int(input('Enter your currency in USD-'))
elif User==3:
    UaeC=int(input('Enter your currency in AD-'))
elif User==4:
    RoubleC=int(input('Enter your currency in Rouble-'))
elif User==5:
    YenC=int(input('Enter your currency in Yen-'))
else:
    print('Pls retry')
print('************************************************')
print('Convert to- ')

print('1.(India)INR\n''2.(USA)USD\n''3.(UAE)AD\n''4.(RUSSIA)ROUBLE\n''5.(JAPAN)YEN\n')


UserCon=int(input('Enter your conversion type-'))
if UserCon<=0:
    print('Error pls retry')

if  User==1 and UserCon==1:
    print(InrC,'INR')
if User==1 and UserCon==2:
    print(InrC*0.012,'USD')
if User==1 and UserCon==3:
    print(InrC*0.045,'AED')
if User==1 and UserCon==4:
    print(InrC*0.75,'RUB')
if User==1 and UserCon==5:
    print(InrC*1.79,'YEN')

if User==2 and UserCon==1:
    print(UsdC/0.012,'INR')
if User==2 and UserCon==2:
    print(UsdC,'USD')
if User==2 and UserCon==3:
    print(UsdC*3.67,'AED')
if User==2 and UserCon==4:
    print(UsdC*61.40,'RUB')
if User==2 and UserCon==5:
    print(UsdC*146.54,'YEN')



if User==3 and UserCon==1:
    print(UaeC/0.045,'INR')
if User==3 and UserCon==2:
    print(UaeC//0.012,'USD')
if User==3 and UserCon==3:
    print(UaeC,'AED')
if User==3 and UserCon==4:
    print(UaeC//0.012,'RUB')
if User==3 and UserCon==5:
    print(UaeC//0.012,'YEN')

if User==4 and UserCon==1:
    print(RoubleC//0.012,'INR')
if User==4 and UserCon==2:
    print(RoubleC//0.012,'USD')
if User==4 and UserCon==3:
    print(RoubleC//0.012,'AED')
if User==4 and UserCon==4:
    print(RoubleC,'RUB')
if User==4 and UserCon==5:
    print(RoubleC//0.012,'YEN')



if User==5 and UserCon==1:
    print(YenC//0.012,'INR')
if User==5 and UserCon==2:
    print(YenC//0.012,'USD')
if User==5 and UserCon==3:
    print(YenC//0.012,'AED')
if User==5 and UserCon==4:
    print(YenC//0.012,'RUB')
if User==5 and UserCon==5:
    print(YenC,'YEN')

### LOGIC IS CORRECT BUT NEED TO FIX CURRENCY CONVERSION THING








