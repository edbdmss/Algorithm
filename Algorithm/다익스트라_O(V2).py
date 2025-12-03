import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]  # 각 노드에 연결된 노드에 대한 정보를 담은 리스트
visited = [False] * (n + 1)  # 방문 리스트
distance = [INF] * (n + 1)  # 최단 거리 테이블


for _ in range(m):
    # a 노드 -> b 노드로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드중에서, 가장 최단 거리가 짧은 노드의 번호 반환
# 한번 처리된 노드는 다시 처리 되지 않는다.
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    """시작노드 초기화"""
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    """ 메인 루프 """
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True  # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리

        """ 경로 갱신 """
        # 해당 노드와 연결되는 노드들 탐색
        for j in graph[now]:
            cost = distance[now] + j[1]
            if (
                cost < distance[j[0]]
            ):  # 만약 이 cost가 기존에 알던 최단거리보다 짧으면 갱신
                distance[j[0]] = cost


''' 실행 '''
# 다익스트라 함수 호출: distance 리스트에 모든 최단 거리가 저장됨
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
