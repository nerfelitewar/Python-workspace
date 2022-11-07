my_list=[1,2,3,4,5,6,7,8,15]
prime=[]
composite=[]

for i in my_list :
    c=0
    for j in range(1,i): #iterate from 1 as 1 and 0 are not prime or composites
        if i%j==0:
            c+=1
    if c>1:
        composite.append(i)
    if c==1:
        prime.append(i)
print('primes-',prime)
print('composites-',composite)
