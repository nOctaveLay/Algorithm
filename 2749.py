import sys

input_num = int(sys.stdin.readline())

a = 1
b = 1
count = 3
if input_num == 1:
	c = a
elif input_num == 2:
	c = b
while count <= input_num:
	c = a+b
	a = b
	b = c
	count += 1
print(c % 10 ** 6)