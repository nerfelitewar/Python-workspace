###APPROACH 1
methods = str.upper, str.lower
def jumble(s):
  r = []
  n = 0
  for i in s:
    if not i.isalpha():
      r.append(i)
    else:
      r.append(methods[n](i))
      n = 1 if n == 0 else 0
  return ''.join(r)

print(jumble(input("Enter your text- ")))

###APPROACH 2 

def jumble(s):
  r = []
  n = 0
  for i in s:
    if n == 0:
        i = i.upper()
        n = 1
    else:
        i = i.lower()
        n = 0
    r.append(i)
  return ''.join(r)

print(jumble("Hello world!"))

###APPROACH 3

s='This is string'
x=s.lower()
l=list(x)
r=[]
n=""
for i in range(len(l)):
    for j in l:
        if i%2==0:
            j=j.upper()
            i+=1
        else:
            j=j.lower()
            i-=1
        r.append(j)
    break
print(n.join(r))


