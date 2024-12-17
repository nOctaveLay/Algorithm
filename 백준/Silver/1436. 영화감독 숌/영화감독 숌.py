# 그냥 다 만들고 sort 시키면 그만임.

arr = set([666])

def make_number(arr,n):
    result = set()
    for i in range(0,10):
        for prev_n in arr:
            zero_n = n- (len(str(prev_n)+str(i)))
            result.add(int(str(i)+'0'*zero_n+str(prev_n)))
            result.add(int(str(prev_n)+'0'*zero_n+str(i)))
            result.add(int(str(prev_n)+str(i)+'0'*zero_n))
    return result

n = int(input())
i = 4
while len(arr) < n:
    arr = arr.union(make_number(arr,i)) # 할당을 해줘야 한다. 바뀌는 method가 아님...
    i += 1
arr = sorted(arr)
print(arr[n-1])