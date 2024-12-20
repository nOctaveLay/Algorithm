n=int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
grade = [1 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            grade[i] += 1
print(*grade, sep = ' ')