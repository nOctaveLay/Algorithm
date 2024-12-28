import sys
input=sys.stdin.readline
eq=input().rstrip()
arr = eq.split("-")
for arr_i, sub_eq in enumerate(arr):
    sub_eq_sum = sum(map(int,sub_eq.split("+")))
    arr[arr_i] = sub_eq_sum

# 뺄셈
result = arr[0]
for arr_elem in arr[1:]:
    result -= arr_elem
print(result)