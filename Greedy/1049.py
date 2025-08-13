import sys
input = sys.stdin.readline

n, m = map(int, input().split())
package = []
each = []

for _ in range(m):
    x, y = map(int, input().split())
    package.append(x)
    each.append(y)
  
