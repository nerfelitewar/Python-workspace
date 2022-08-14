'''
search duplicates numbers in a list and return the number  with index no.
'''
L=[1,1,2,3,4,5,6,7,5,9]
for idOfDub, i in enumerate(L):
    if L.count(i)!=1:
        print(i,idOfDub, end='<---INDEX ')
