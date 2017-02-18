in_n = int(input())

a = 1
b = 1
count = 3
if in_n == 1:
	c = a
elif in_n == 2:
	c = b
while count <=in_n:
	c = a+b
	a = b
	b = c
	count += 1
print(c)