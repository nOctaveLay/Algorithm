#이 문제는 조금 복잡했다. 입력받는 값은 결국 h를 구성한다.
# recursive를 이용한 문제.

h = int(input())
#h는 입력받은 값으로서, 여기에서는 높이를 의미한다.

w = 2*h + 1
#w는 가로길이를 규정한다. 이 삼각형을 3*5의 직사각형으로 봤을 때 width의 값이다.
#array는 여기에서 출력할 리스트로 한다. 이 방법을 쓰지 않고 STRING으로 했을 때엔 너무 복잡해진다.
array = []
#array의 초기값은 " "로 한다. 그러는 것이 훨씬 초기화의 면에서 낫기 때문이다.
for y in range(h):
	array.append([])
	for x in range(w):
		array[y].append(" ")
#print_star는 리스트에 있는 값을 나타내준다. python3에서는 리스트를 그냥 출력하면 리스트의 형태로 출력되므로, 이를 스트링으로 나타내 주기 위해서 join이라는 함수를 썼다.
def print_star(array):
	for y in range(h):
		print("".join(array[y]))

def star(array,x,y,h,offset):
#pad는 여기에서 앞에서부터 시작되는 여백값이다. 이는 h-1-y를 따른다.
	pad = offset-y
	# h == 3일때가 기본형이 나오므로, 이 때에 기본형 값을 list에 저장해둔다. 일반적으로 이중 리스트는 바깥부터 접촉하므로, 바깥을 아까 위에서 높이값으로 지정했고, 안의 값을 너비로 지정했다. 따라서 y와 x의 순서는 바뀌어야 한다.	
	if h == 3:
		array[y][x+pad] = "*"
		array[y+1][x+pad-1] = "*"
		array[y+1][x+2+pad-1] = "*"
		for i in range(5):
			array[y+2][x+i+pad-2] = "*"
	else:
		star(array,x+h,y+h//2,h//2,offset)#삼각형의 오른쪽 변
		star(array,x,y+h//2,h//2,offset)#삼각형의 왼쪽 변
		star(array,x,y,h//2,offset)#삼각형의 윗변
star(array,0,0,h,h-1)
print_star(array)
