# three sum 10817
string = input().split(" ")
a = int(string[0])
b = int(string[1])
c = int(string[2])
if (a <= b and b < c) or (c<=b and b<= a):
	mid = b
elif (b <= c and c < a) or (a <= c and c <= b):
	mid = c
else:
	mid = a
print(mid)