import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    result = 0b0
    for _ in range(n):
        command_line = input().rstrip("\n").split(" ")
        command = command_line[0]
        if len(command_line) == 2 :
            elem = int(command_line[1])
            if command == 'add':
                result = result | (0b1<<elem)
            elif command == 'remove':
                result = result & ~(0b1<<elem)
            elif command == 'check':
                print(1 if (result&(0b1 << elem)) else 0)
            elif command == 'toggle':
                result = result ^ (0b1 << elem)
        else:
            if command == 'all':
                result = 0b111111111111111111111
            else:
                result = 0b0