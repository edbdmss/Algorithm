import sys
input = sys.stdin.readline


def search(num, x, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    
    if num[mid] == x:
        return 1
    elif num[mid] > x:
        return search(num, x, start, mid-1)
    else:
        return search(num, x, mid+1, end)


n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
target = list(map(int, input().split()))

for i in target:
    print(search(num, i, 0, n-1))