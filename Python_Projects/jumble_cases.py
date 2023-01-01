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

###OR 

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
