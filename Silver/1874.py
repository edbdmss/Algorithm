import sys
input = sys.stdin.readline

n = int(input())
num = []
stack = [0]
plusminus = []

for _ in range(n):
    num.append(int(input()))

i = 1
j = 0
while True:

    if num[j] == stack[-1]:
        stack.pop()
        j += 1
        plusminus.append('-')
    else:
        stack.append(i)
        plusminus.append('+')
        i += 1
    
    if j == n:
        break
    if i > n and stack[-1] != num[j]:
        break

if stack[-1] != 0:
    print('NO')
else:
    for l in plusminus:
        print(l)