import sys
input = sys.stdin.readline

def dfs(energy):
    global max_value

    if len(w) == 2:
        max_value = max(max_value,energy)
        return
    for i in range(1,len(w)-1): # 공평하게 기회를 주기
        elem = w[i]
        del w[i] #remove로 지우면 안된다. remove는 첫번째 원소를 지우는 것이기 때문...
        dfs(energy + w[i-1] * w[i])
        w.insert(i,elem)

if __name__ == "__main__":
    n = int(input())
    w = list(map(int,input().split()))
    max_value = 0
    dfs(0)
    print(max_value)