'''Program to print a prime and not a prime in a list if a lst is 1 return not a prime and composite'''
#taking a sample list 
lst=[0,1,2,3,15,16,21,23]
for i in lst:
    if i == 1 or i==0: 
        print(f'{i} Neither a prime nor a composite')
        continue
    

    for j in range(2, i):
        if i % j == 0:
            print(f'{i} is not prime')
            break
    else:
        print(f'{i} is prime')
