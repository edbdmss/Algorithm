import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while True:
    if len(s) == len(t):
        break
    end = len(t)-1
    if t[end] == 'A':
        t.pop()
    elif t[end] == 'B':
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)