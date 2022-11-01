

## prime composite number function from a list.
# x=int(input('Enter numbers-'))
# x=list(x)
x=[1,2,3,4,5,6,7,13,15,20,21]
def prime_comp(list):
    primes=[]
    composites=[]
    count=0
    for num in list:
        # num=num
    
        i=1
        while i<=len(x):
            if i%num==0:
                count=count+1
            i=i+1

            if count==2:
                return 'Prime numbers-', primes.append(num)
            elif count!=2:
                return 'Composite numbers-', composites.append(num)
            else:
                return 'Neither prime nor composite numbers-',num


prime_comp(x)

### THIS SHIT IS BROKEN AHHHHHHHHHHHHH HELP ME BRUH

            


