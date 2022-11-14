import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
oper = list(map(int,input().split())) # + - X //
min_v = 1000000001
max_v = -1000000001

def dfs(sidx,result):
    global min_v
    global max_v

    if sidx == n:        
        min_v = min(min_v,result)
        max_v = max(max_v,result)
        return 
    h = arr[sidx]
    
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1     
            if i == 0: # +
                dfs(sidx + 1, result + h)
            elif i == 1: # -
                dfs(sidx + 1,result - h)
            elif i == 2: # *
                dfs(sidx + 1,result * h)
            else: # //
                if result < 0:
                    dfs(sidx + 1 , -(abs(result) // h))
                else:                
                    dfs(sidx + 1 , abs(result) // h)
            oper[i] += 1
    return
dfs(1,arr[0])
print(max_v,min_v,sep = '\n')