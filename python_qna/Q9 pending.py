'''
reverse a string 
'''

S='string'
#expected ans= 'gnirts'
#approach 1
x=list(S)
print(x)
x.sort(reverse=True)
print(x) #pending


#approach 2 
print(S[::-1]) 
