n = int(input())

vilage = list(map(int,input().split()))
vilage.sort(reverse=True)
print(sum(vilage[1:]))