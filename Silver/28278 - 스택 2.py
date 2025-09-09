import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    ord = input().rstrip().split()
    o = ord[0]
    if o == '1': stack.append(int(ord[1]))
    elif o == '2':
        if stack: print(stack.pop())
        else: print(-1)
    elif o == '3': print(len(stack))
    elif o == '4': 
        if stack: print(0)
        else: print(1)
    elif o == '5':
        if stack: print(stack[-1])
        else: print(-1)