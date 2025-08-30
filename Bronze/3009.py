xdot = []
ydot = []

for _ in range(3):
    x, y = map(int, input().split())
    xdot.append(x) 
    ydot.append(y)

for i in xdot:
    if xdot.count(i) == 1:
        print(i, "", end='')
for i in ydot:
    if ydot.count(i) == 1:
        print(i)