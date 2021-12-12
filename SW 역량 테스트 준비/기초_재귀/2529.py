import sys
input = sys.stdin.readline
n = int(input())
inequal_sign = input().split()
num_set = list()
max_num, min_num = '', ''
visited = [False] * 10

def check(i,j,sign):
    if sign == '<':
        return i < j
    elif sign == '>':
        return i > j
    else: return False

def solve(cnt,num):
    if cnt == n + 1:
        global max_num
        global min_num
        
        if not len(min_num):
            min_num = num
        else:
            max_num = num

        return
        
    else:
        for i in range(10):
            if visited[i] == False :
                if cnt == 0 or check(int(num[-1]),i,inequal_sign[cnt-1]):
                    visited[i] = True
                    solve(cnt+1,num+str(i))
                    visited[i] = False
solve(0,'')
print(max_num,min_num)