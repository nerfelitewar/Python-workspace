#converts word to num form  
NumLst=[0,1,2,3,4,5,6,7,8,9]
User=input('Enter number in word form\n')
UserLst=User.split()
print(UserLst)
Output=[]

for i in UserLst:
    if i=='zero':
        Output.append(NumLst[0])
    if i=='one':
        Output.append(NumLst[1])
    if i=='two':
        Output.append(NumLst[2])
    if i=='three':
        Output.append(NumLst[3])
    if i=='four':
        Output.append(NumLst[4])
    if i=='five':
        Output.append(NumLst[5])
    if i=='six':
        Output.append(NumLst[6])
    if i=='seven':
        Output.append(NumLst[7])
    if i=='eight':
        Output.append(NumLst[8])
    if i=='nine':
        Output.append(NumLst[9])
print(Output)
 
 