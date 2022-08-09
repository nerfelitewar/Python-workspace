"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

#ANSWER-
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

"""
arr=[1,2,3,4]
ans=1
for i in arr:
    ans*=i
print(ans)
