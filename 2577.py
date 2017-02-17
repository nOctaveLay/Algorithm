a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
result = [0 for _ in range(10)]
for x in mul:
	result[int(x)] += 1
for x in result:
	print(x)