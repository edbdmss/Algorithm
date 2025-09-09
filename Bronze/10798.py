import sys
input = sys.stdin.readline

ch = []

for _ in range(5):
    x = list(input().strip())
    ch.append(x)


for i in range(15):   # i=열   **최대 15글자 나열 가능!
    for j in range(len(ch)):   # j=행
        if (i < len(ch[j])):
            print(*ch[j][i], end="")    