import sys
input = sys.stdin.readline

n = int(input())
good = 0
for _ in range(n):
    stack = []
    temp = list(input().rstrip())
    
    for i in range(len(temp)):
        if i == 0:
            stack.append(temp[i])
        elif i > 0:
            if not stack or temp[i] != stack[-1]:
                stack.append(temp[i])
            else:
                stack.pop()
    if not stack:
        good+=1 
print(good)