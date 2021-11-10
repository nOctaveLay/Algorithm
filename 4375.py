import sys

while True:
    try:
        n = int(sys.stdin.readline())
        least_num = 1 % n
        ans = 1

        while least_num != 0:
            ans += 1
            least_num = (least_num * 10 + 1) % n

        print(ans)
    except:
        break
