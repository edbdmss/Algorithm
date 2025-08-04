import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    n = input().split()
    if n[0] == 'push':
        stack.append(n[1])
    elif n[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif n[0] == 'size':
        print(len(stack))
    elif n[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))