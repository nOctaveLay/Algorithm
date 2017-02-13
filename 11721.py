#11721 split 10

string = input()
(a,b) = (0,10)
while (len(string) >b):
	print(string[a:b])
	a += 10
	b += 10
print(string[a:])