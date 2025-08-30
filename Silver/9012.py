import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    stack = []
    if s[0] == ')':
        print('NO')
        #continue
    
    else:
        for i in s:
            if i == '(':
                stack.append(i)
            else:       # ')'
                if stack:
                    stack.pop()
                else:
                    print('NO')
                    break
        else: 
            if stack:
                print('NO')
            else:
                print('YES')
                
                