import sys
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

tape = 0  
node = a[0]
for i in range(1, n):
    length = a[i]-node+1
    if (length <= l):    # l은 테이프 길이
        tape +=1
    else:
        tape += (length//l + 1)
        node = a[i]

print(tape)     