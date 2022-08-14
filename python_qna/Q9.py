'''
reverse a string 
'''


S='string'
#expected ans= 'gnirts'

#approach 1

print(S[::-1]) 

#approach 2
print("".join(reversed("string")))

#approach 3 
result = ""
for i in range(len(S)):
    result += S[len(S)-1-i]
print(result)



#approach 4
print( "".join([S[len(S)-1-i] for i in range(len(S))]))


