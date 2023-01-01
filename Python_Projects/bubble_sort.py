def bubble(l):
    for i in range(len(l),1,-1): #stops at 2 so that it can compare 2 values
        for j in range(0,i-1): # checking values from 0 to i-1 ie 2-1 = 1 
            if l[j]>l[j+1]: 
                l[j],l[j+1]=l[j+1],l[j] #swapping 2 values
            else:
                pass
    print(l)
bubble((list(eval(input("Enter numbers- ")))))
