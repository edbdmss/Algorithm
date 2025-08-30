import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
num =''

if '0' not in n:
    print(-1)
else:
    for i in n:
        num += i
    num = int(num)
    if num%3==0:
        print(num)
    else:
        print(-1)