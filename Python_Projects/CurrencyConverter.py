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
if UserCon==1 and User==1:
    print(InrC+0,'INR')
if UserCon==1 and User==2:
    print(InrC//78,"USD") #not working why? IDK 
if UserCon==1 and User==3: #not working too idk :/
    print(InrC*20,'AED')

#PENDING PROJECT 

