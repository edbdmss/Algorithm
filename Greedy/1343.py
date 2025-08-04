import sys

board = list(sys.stdin.readline().strip().split('.'))
for i in board:
    if i == '':
        board.remove(i)
print(board)
for i in board:
    if len(i)%2 != 0:
        print(-1)
        break
    else:
        m = len(i)//4 
        n = len(i)%4
        result = 'AAAA'*m + 'BB'*n
        board = i.replace(i, result)

for i in board:
    print(i, end='.')
        