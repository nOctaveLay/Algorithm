h = int(input())
w = 2*h + 1
array = []
for y in range(h):
	array.append([])
	for x in range(w):
		array[y].append(" ")

def print_star(array):
	for y in range(h):
		print("".join(array[y]))

def star(array,x,y,h,offset):
	pad = offset-y
	if h == 3:
		array[y][x+pad] = "*"
		array[y+1][x+pad-1] = "*"
		array[y+1][x+2+pad-1] = "*"
		for i in range(5):
			array[y+2][x+i+pad-2] = "*"
	else:
		star(array,x+h,y+h//2,h//2,offset)
		star(array,x,y+h//2,h//2,offset)
		star(array,x,y,h//2,offset)
star(array,0,0,h,h-1)
print_star(array)