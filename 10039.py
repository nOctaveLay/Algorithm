result_sum = 0
for _ in range(5):
	a = int(input())
	if a < 40:
		a = 40
	result_sum += a
print(result_sum//5)