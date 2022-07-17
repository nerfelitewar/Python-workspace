# In this project there will be a dictionary in a list that will tell us students identity by the roll number given to then ie the index number of the dict in the list 

DataLst=[' ',{"Name-":"Raj","Class-":12,"Roll no.-":12,"School-":"DAV Public School","Email-":"rajdav@xyz.in"},
{"Name-":"John","Class-":12,"Roll no.-":42,"School-":"XYZ Public School","Email-":"johnxyz@xyz.in"}, {"Name-":"Mike","Class-":12,"Roll no.-":23,"School-":"Peter Public School","Email-":"mike@peter.in"}]
print('Welcome, pls press any key to continue')
input()
print("===========================================")

def function():
    roll_no= int(input("Enter roll number-")) 
    if roll_no != 0:
        print()
 
    else:
        print('Pls recheck and enter the correct roll no.')
        function()

    print(DataLst[roll_no]) 
    print("Thank you")

    again= input('Again? Type (yes/no) y/n-')
    if again == 'y':
        function()
    else:
        pass 
function()
    

