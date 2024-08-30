from collections import Counter
def R(a:list):
    max_r = 0
    for r in range(len(a)):
        x = Counter(a[r])
        del x[0] # when sorting num, ignore 0
        # sorting
        x = list(x.items())
        x = sorted(x, key = lambda x: (x[1], x[0]))

        # max_length == 100
        if len(x) > 50: x = x[:50]

        # making a[r]
        result = list()
        for num, count in x:
            result.append(num)
            result.append(count)
        a[r] = result
        max_r = max(len(a[r]), max_r)

    # padding 0
    for r in range(len(a)):
        if len(a[r]) < max_r:
            a[r].extend([0]*(max_r - len(a[r])))
    return a

def solution(r:int, c:int, k:int, A:list):
    # initial condition
    time = 0 # elapsed time
    r, c = r - 1, c - 1
   
    # loop
    while True:
        # end_condition
        if r < len(A) and c < len(A[0]):
            if A[r][c] == k:
                return time
        if time > 100:
            return -1

        # loop_condition
        if len(A) >= len(A[0]): # row >= column
            R(A)
        else:
            A = list(map(list, zip(*A)))        
            R(A)
            A = list(map(list, zip(*A)))
        time += 1
if __name__ == "__main__":
    r, c, k = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(3)] # In Problem, A is 3x3 matrix
    result = solution(r,c,k,A)
    print(result, end='')