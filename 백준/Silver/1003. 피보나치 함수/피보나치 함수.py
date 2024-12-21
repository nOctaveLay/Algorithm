t=int(input())
'''
피보나치 수를 부를 때
0 -> (1,0)
1 -> (0,1)
2 -> (1,1) = f(0) + f(1)
2 이상(n) ->  f(n-1)번 + f(n-2)번
메모이제이션으로 풀 수 있을것이라 예상
'''

arr = [[0,0] for _ in range(41)] # n의 범위가 0~40까지라고 했으므로, 총 41번
# 초기값
arr[0] = [1,0]
arr[1] = [0,1]

# 메모이제이션 arr 미리 계산
for i in range(2,41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]
for _ in range(t):
    print(*arr[int(input())], sep=' ')