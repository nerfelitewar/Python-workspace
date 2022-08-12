'''
rock paper scissors 
'''

p1=input('RPS-')
p2=input('RPS-')
hand = {'rock':0, 'paper':1, 'scissors':2}
results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
print( results[hand[p1] - hand[p2]])
