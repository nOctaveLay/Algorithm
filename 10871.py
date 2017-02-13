# x>= number

nx = input().split(" ")
X = int(nx[1])
list_x = input().split(" ")
print_list = ''
for a in list_x:
	if (int(a) < X):
		print_list += a + " "
print(print_list)