import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))
visit_day = [0] * (N+1)

if max(visit) == 0:
    print("SAD")
    exit()
else:
    day = [0] * (N-X+1)
    for i in range(1, N+1):
        visit_day[i] = visit_day[i-1] + visit[i-1]
    for k in range(len(day)):
        day[k] = visit_day[X] - visit_day[k]
        X += 1
    print(max(day))
    print(day.count(max(day)))