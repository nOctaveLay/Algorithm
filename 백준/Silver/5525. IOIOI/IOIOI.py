import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
arr=list(map(str,input().rstrip()))
i = 0
answer = 0
count = 0
while i < m-1:    
    # print(i,answer,count)
    if arr[i] == 'I':
        # 'IOI'가 몇 번 나왔는지 확인해준다.
        if i+2 > m-1:
            count = 0
            i += 1 
        elif arr[i+1] == 'O' and arr[i+2] == 'I': # IOI
            count += 1 # IOI
            i += 2
            if count == n: #IOI == IOI * n
                answer += 1
                count -= 1
        else:
            count = 0
            i += 1           
            
    else:
        count = 0
        i += 1           
print(answer)