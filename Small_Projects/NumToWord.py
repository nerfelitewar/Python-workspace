#converts number to word form

WordNumList=['zero','one','two','three','four','five','six','seven','eight','nine']
User=input('Enter numbers-')

Userlst=list(User)
Output=[]

for NumInLst in Userlst:
        if NumInLst=='0':
            Output.append(WordNumList[0])
        if NumInLst=='1':
            Output.append(WordNumList[1])
        if NumInLst=='2':
            Output.append(WordNumList[2])
        if NumInLst=='3':
            Output.append(WordNumList[3])
        if NumInLst=='4':
            Output.append(WordNumList[4])
        if NumInLst=='5':
            Output.append(WordNumList[5])
        if NumInLst=='6':
            Output.append(WordNumList[6])
        if NumInLst=='7':
            Output.append(WordNumList[7])
        if NumInLst=='8':
            Output.append(WordNumList[8])
        if NumInLst=='9':
            Output.append(WordNumList[9])
print( Output)