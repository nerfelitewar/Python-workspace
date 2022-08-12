#hashtag generator 
s='    i love   coding    '
output = "#"

for word in s.split():
    output += word.capitalize()

    x= False if (len(s) == 0 or len(output) > 140) else output
    print(x)
