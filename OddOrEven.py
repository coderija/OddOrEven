vec = []
summ = 0
n = int(input("enter your number: "))

for i in range(0, n):
	element = int(input())
	vec.append(element)
print(vec)

for i in range(0, n):
	summ = summ + vec[i]
if summ % 2 == 0:
	print ('even')
else:
	print ('odd')
