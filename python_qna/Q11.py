'''Program to print a prime and not a prime in a list if a lst is 1 return not a prime and composite'''
#taking a sample list 
lst=[1,2,3]
num=0
x=1
while x>0:
   num+=1
   if num<=len(lst):
      pass
countNum=0
while x>0:
    for i in range(2,num):
         for LstNum in lst:
            if LstNum==1:
                print(LstNum,'Neither a prime nor a composite')
            if LstNum%i==0:
                print(LstNum,'is not prime')
            else:
                print(LstNum,'is prime')
            countNum=countNum+1
            if countNum==num:
                  pass 
         break
    break 