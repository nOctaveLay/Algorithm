import sys
input=sys.stdin.readline
n,r,c=map(int,input().split())

# 2**15 약= 32000
# 32000 * 32000 = 3*10**5 * 3* 10 **5 = 9 * 10 ** 10...
# 메모리 부족 날 만 했네. 뭔가 다른 규칙성이 필요해 보이는데

# 우리가 구하고자 하는 것 arr[r][c]

answer = 0
while n != 0:
    n -= 1
    r_q = r // 2**n
    c_q = c // 2**n

    # 만약 나눠졌을 때 몫이 1인지 0인지에 따라 있는 위치가 달라짐
    if r_q == 0: 
        if c_q == 0: # (0,0) -> 오리지널
            answer += 0
        else:
            answer += (2 ** n * 2 ** n)
            c -= 2 ** n
    else:
        if c_q == 0:
            answer += (2**n * 2 ** n)*2
            r -= 2 ** n
        else:
            answer += (2**n * 2 ** n)*3
            r -= 2 ** n
            c -= 2 ** n
print (answer)