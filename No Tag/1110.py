#init
init_num = int(input())
count = 0
add = init_num
#while
while add != init_num or count == 0:
	a = add // 10
	b = add % 10
	c = (a+b) % 10
	a = b
	b = c
	add = a * 10 + b
	count += 1
print(count)