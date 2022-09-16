from collections import deque
import sys
'''
드레곤 커브를 구현한 것이다.
x,y,d,g
x,y : 시작점
d : 시작 방향
g : 세대
list에서 결과 뽑아낼 때는 거꾸로 써야 함에 주의
'''
def make_is_curved(x,y,d,g):
    next_move = deque()
    next_move.append(d)
    # 첫 지점은 무조건 드레곤 커브의 지점이다.
    isCurved[y][x] = 1 

    # 드레곤 커브의 세대가 거듭될 수록 드레곤 커브는 자기 복제를 계속하여 형태를 만든다.
    # 따라서 next_move에 next_move를 90도 회전한 것이 붙는데, 붙을 때 끝 점부터 붙으므로
    # next_move에도 next_move를 90도 이전한 것을 끝점부터 붙여줘야 한다.
    for _ in range(g):
        for i in reversed(range(len(next_move))):
            next_move.append((next_move[i] + 1) % 4)
    
    # arr에 직접 붙여주기, dx,dy를 이용해 붙여준다.
    # 조심해야 할 점은 x축으로 이동할 때는 column으로, y축으로 이동할 때에는 row로 이동한다는 점을 명심하자
    while next_move:
        movement = next_move.popleft()
        dx,dy = d_dict[movement]
        nx,ny = x + dx, y+dy
        isCurved[ny][nx] = 1
        x, y = nx, ny

def return_cnt_is_all_dragoncurve():
    cnt = 0
    for i in range(max_length-1):
        for j in range(max_length-1):
            if isCurved[j][i] and isCurved[j][i+1] and isCurved[j+1][i] and isCurved[j+1][i+1]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    max_length = 101
    d_dict = {0:(1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)}

    # 드레곤 커브인지 아닌지 알려주는 list
    isCurved = [[0 for _ in range(max_length)] for _ in range(max_length) ]
    for _ in range(n):
        x,y,d,g = map(int,input().split())
        make_is_curved(x,y,d,g)
    print(return_cnt_is_all_dragoncurve())