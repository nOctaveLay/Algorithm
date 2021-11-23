import sys
a,b = sys.stdin.readline().rstrip("\n").split(" ")
a,b = int(a),int(b)
if a > b: sys.stdout.write('>')
elif a == b : sys.stdout.write('==')
else: sys.stdout.write('<')