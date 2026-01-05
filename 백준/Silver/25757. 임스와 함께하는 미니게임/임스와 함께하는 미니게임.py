import sys

input = sys.stdin.readline

player = set()
n, game_type = input().split()
n = int(n)

for _ in range(n):
    player.add(input().rstrip())
n_p = len(player)
if game_type == 'Y':
    print(n_p)
elif game_type == 'F':
    print(n_p//2)
elif game_type == 'O':
    print(n_p//3)