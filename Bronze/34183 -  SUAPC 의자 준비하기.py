import sys
input = sys.stdin.readline

N, M, A, B = map(int, input().split())
result = (3*N - M) * A + B
if result <=0: print(0)
elif 3*N-M <=0: print(0)    # 3 9 5 20 인 경우를 고려해야함.
else: print(result)