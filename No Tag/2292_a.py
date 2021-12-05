#that is runtime error.
#recursive code
goal = int(input())
def h_house(number):
	if number == 1:
		return 1
	else:
		return h_house(number-1)+6*(number-1)
count = 1
while h_house(count) <goal:
	count +=1
print(count)
