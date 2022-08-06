#print max number in a list 
L=[232323,42,42,2,32,4,2,3,12,1,9,9,9,9,999999]
def MaxNum(L):
    Max=max(L)
    return Max
print(MaxNum(L))

#approach 2 
def MaxNUM(L):
    sort=sorted(L)
    x=sort[-1]
    return x
print(MaxNUM(L))


#O/P- 999999 