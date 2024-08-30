import sys,itertools

n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
total_team = set(range(0,n))
answer = 1e9

def sum_arr(start_member,idx):
    
    global answer
    if len(start_member) == n//2:
        start, link = 0,0
        link_member = total_team - start_member
        
        for i,j in itertools.combinations(start_member,2):
            start += arr[i][j] + arr[j][i]

        for i,j in itertools.combinations(link_member,2):
            link += arr[i][j] + arr[j][i]
        answer = min(answer,abs(start - link))
        return
    else:
        for i in range(idx,n):
            start_member.add(i)
            sum_arr(start_member,i + 1)
            start_member.remove(i)

sum_arr(set(),0)

sys.stdout.write(str(answer))